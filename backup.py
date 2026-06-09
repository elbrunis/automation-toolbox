from datetime import datetime
import os
import shutil

# ===============================================================
#  AUTOMATED BACKUP SCRIPT
#  Description: Creates a .zip backup of a directory and 
#  removes backups older than X days.
# ===============================================================

# --- Configuration ---
SOURCE_DIR = "/mnt/c/Users/Bruno/Pictures"
BACKUP_DIR = "/mnt/c/Users/Bruno/Documents/img_backup"
DAYS_LIMIT = 7

# --- Colors ---
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
GRAY = "\033[90m"


def	get_file_age_days(file_path) -> int:
	"""
    Returns the age of a file in days.
    """
	timestamp = os.path.getmtime(file_path)
	last_modified = datetime.fromtimestamp(timestamp)
	age = datetime.now() - last_modified
	return age.days


def delete_old_backups():
	"""
    Scans for backups older than DAYS_LIMIT and deletes them.
    """
	if not os.path.exists(BACKUP_DIR):
		return

	for file in os.listdir(BACKUP_DIR):

		# if its not a .zip, continue
		if not file.endswith(".zip"):
			continue
		
		#if is older than 7 days, delete 
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
    Creates a new zip backup of the SOURCE_DIR.
    """
	# Ensure backup directory exists
	os.makedirs(BACKUP_DIR, exist_ok=True)

	# Cleanup old backups first
	delete_old_backups()

	tmp_date = datetime.now().strftime("%Y-%m-%d_%H-%M")
	new_backup_path = os.path.join(BACKUP_DIR, f"backup_{tmp_date}")

	print(f"\n📦 Creating backup for: {SOURCE_DIR}...")
	try:
		# shutil.make_archive automatically adds .zip extension
		cpy_path = shutil.make_archive(new_backup_path, 'zip', SOURCE_DIR)
		return cpy_path
	except Exception as e:
		print(f"{RED}❌ Compression failed: {e}{RESET}")
		return None
			

if __name__ == "__main__":
	if not os.path.exists(SOURCE_DIR):
		print(f"{RED}❌ Error: Source folder '{SOURCE_DIR}' not found.{RESET}")
	else:
		new_backup_path = create_backup()

		if new_backup_path:
			#calculate Megabytes backupsyze
			size_mb = os.path.getsize(new_backup_path) / (1024 * 1024)

			print(f"{GREEN}✅ Success! Backup created successfully.{RESET}")
			print(f"   📂 Path: {new_backup_path}")
			print(f"   💾 Size: {size_mb:.2f} MB") # <--- Imprimimos el tamaño bonito
		else:
			print(f"{RED}❌ Error: Backup could not be created.{RESET}")
