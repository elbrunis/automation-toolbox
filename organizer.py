"""
File organizer automation tool.

Scans a target directory and categorises files into subfolders
(Images, Documents, Videos, Compressed, Executables, Installers)
based on their file extension.

@requires os, shutil
@example
    python organizer.py
"""

# --- Extension-to-Category Mapping ---
# Maps each destination folder name to a list of accepted file extensions.
EXTENSIONS_MAP = {
	"Images":       [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
	"Documents":    [".pdf", ".txt", ".docx", ".doc", ".xlsx", ".pptx", ".csv"],
	"Videos":       [".mp4", ".avi", ".mov", ".mkv", ".flv"],
	"Compressed":   [".zip", ".rar", ".7z", ".tar", ".gz"],
	"Executables":  [".exe", ".msi", ".bat", ".sh", ".app"],
	"Installers":   [".deb", ".rpm", ".iso"]
}


def organize_directory(target_path):
	"""
	Organise files inside the given directory into category-based subfolders.

	Expands the user path, validates it, creates missing category directories,
	then moves each file into the appropriate subfolder based on its extension.
	Files with unrecognised extensions are skipped and reported.

	@param {str} target_path - Directory path to scan and organise (supports ~).
	@returns {void}
	@throws {PermissionError} If files cannot be moved due to insufficient permissions.
	@throws {OSError} If subdirectory creation fails.
	"""
	folder_path = os.path.expanduser(target_path)

	if not os.path.exists(folder_path):
		print(f"❌ Error: The folder '{folder_path}' does not exist.")
		return

	for directory in EXTENSIONS_MAP.keys():
		directory_path = os.path.join(folder_path, directory)
		if not os.path.exists(directory_path):
			os.mkdir(directory_path)

	for file in os.listdir(folder_path):
		file_path = os.path.join(folder_path, file)

		if not os.path.isfile(file_path):
			continue

		extension = os.path.splitext(file)[1].lower()
		moved = False

		for key, valid_extensions in EXTENSIONS_MAP.items():
			if extension in valid_extensions:
				key_path = os.path.join(folder_path, key)

				try:
					shutil.move(file_path, key_path)
					moved = True
					print(f"\033[92m✓ Moved: {file} -> {key}\033[0m")
					break
				except Exception as e:
					print(f"⚠️ Error: {e}")
					moved = False

		if not moved:
			print(f"\033[90m- Skipped: {file} (Unknown type)\033[0m")


if __name__ == "__main__":
	"""
	Entry point. Runs the organiser on the default Downloads directory.

	@example
	    python organizer.py
	"""
	organize_directory("/mnt/c/Users/Bruno/Downloads")

