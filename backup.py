from datetime import datetime
import os
import shutil

"""
Automated backup script with retention policy.

Creates timestamped .zip archives of a source directory and automatically
removes backups older than a configurable number of days.

@requires os, shutil, datetime
@example
    python backup.py
"""

# --- Configuration ---
SOURCE_DIR = "/mnt/c/Users/Bruno/Pictures"
BACKUP_DIR = "/mnt/c/Users/Bruno/Documents/img_backup"
DAYS_LIMIT = 7

# --- ANSI Color Constants ---
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
GRAY = "\033[90m"


def get_file_age_days(file_path) -> int:
	"""
	Calculate the age of a file in days since its last modification.

	Uses os.path.getmtime() to retrieve the last modification timestamp
	and computes the difference from the current system time.

	@param {str} file_path - Absolute or relative path to the target file.
	@returns {int} Number of full calendar days since the file was last modified.
	@throws {FileNotFoundError} If the file does not exist at the given path.
	"""
	timestamp = os.path.getmtime(file_path)
	last_modified = datetime.fromtimestamp(timestamp)
	age = datetime.now() - last_modified
	return age.days


def delete_old_backups():
	"""
	Remove all .zip backups in BACKUP_DIR that exceed the retention limit.

	Iterates over the backup directory, filters for .zip archives, and deletes
	those whose age in days is >= DAYS_LIMIT. Skips non-zip files silently.
	Does nothing if BACKUP_DIR does not exist.

	@returns {void}
	@throws {PermissionError} If the process lacks delete permissions on a file.
	"""
	if not os.path.exists(BACKUP_DIR):
		return

	for file in os.listdir(BACKUP_DIR):
		if not file.endswith(".zip"):
			continue

		file_path = os.path.join(BACKUP_DIR, file)
		day = get_file_age_days(file_path)

		if day >= DAYS_LIMIT:
			try:
				os.remove(file_path)
				print(f"{RED}🗑️  Deleted old backup: {file} ({day} days old){RESET}")
			except Exception as e:
				print(f"{RED}⚠️  Error deleting {file}: {e}{RESET}")


def create_backup() -> str:
	"""
	Create a new timestamped .zip backup of the configured SOURCE_DIR.

	Ensures the backup directory exists, purges outdated archives, then
	compresses the source directory into a zip file named backup_<timestamp>.zip.

	@returns {str} Absolute path to the newly created archive, or None on failure.
	@throws {OSError} If the source directory is inaccessible or disk space is insufficient.
	"""
	os.makedirs(BACKUP_DIR, exist_ok=True)

	delete_old_backups()

	tmp_date = datetime.now().strftime("%Y-%m-%d_%H-%M")
	new_backup_path = os.path.join(BACKUP_DIR, f"backup_{tmp_date}")

	print(f"\n📦 Creating backup for: {SOURCE_DIR}...")
	try:
		cpy_path = shutil.make_archive(new_backup_path, 'zip', SOURCE_DIR)
		return cpy_path
	except Exception as e:
		print(f"{RED}❌ Compression failed: {e}{RESET}")
		return None


if __name__ == "__main__":
	"""
	Entry point. Validates SOURCE_DIR, runs the backup, and reports results.

	@example
	    python backup.py
	"""
	if not os.path.exists(SOURCE_DIR):
		print(f"{RED}❌ Error: Source folder '{SOURCE_DIR}' not found.{RESET}")
	else:
		new_backup_path = create_backup()

		if new_backup_path:
			size_mb = os.path.getsize(new_backup_path) / (1024 * 1024)

			print(f"{GREEN}✅ Success! Backup created successfully.{RESET}")
			print(f"   📂 Path: {new_backup_path}")
			print(f"   💾 Size: {size_mb:.2f} MB")
		else:
			print(f"{RED}❌ Error: Backup could not be created.{RESET}")
