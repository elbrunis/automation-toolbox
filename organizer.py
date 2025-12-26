import os
import shutil

# ===============================================================
#  FILE ORGANIZER AUTOMATION
#  Description: Scans a directory and organizes files into 
#  folders based on their extensions.
# ===============================================================

# Library of types
EXTENSIONS_MAP = {
	"Images":		[".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
	"Documents":	[".pdf", ".txt", ".docx", ".doc", ".xlsx", ".pptx", ".csv"],
	"Videos":		[".mp4", ".avi", ".mov", ".mkv", ".flv"],
	"Compressed":	[".zip", ".rar", ".7z", ".tar", ".gz"],
	"Executables":	[".exe", ".msi", ".bat", ".sh", ".app"],
	"Installers":	[".deb", ".rpm", ".iso"]
}


def	organize_directory(target_path):
	
	# Returns target path
	folder_path = os.path.expanduser(target_path)

	# validate path
	if not os.path.exists(folder_path):
		print(f"❌ Error: The folder '{folder_path}' does not exist.")
		return

	# Create subdirectories if they don't exist
	for directory in EXTENSIONS_MAP.keys():
		directory_path = os.path.join(folder_path, directory)
		if not os.path.exists(directory_path):
			os.mkdir(directory_path)

	#Main Loop: Iterate through files
	for file in os.listdir(folder_path):
		file_path = os.path.join(folder_path, file)

		# Skip directories, handle only files
		if not os.path.isfile(file_path):
			continue
		
		# Get extension (lowercase for comparison)
		extension = os.path.splitext(file)[1].lower()

		moved = False

		# Inner Loop: Check categories
		for key, valid_extensions in EXTENSIONS_MAP.items():
			if extension in valid_extensions:
				key_path = os.path.join(folder_path, key)

				try:
					shutil.move(file_path, key_path)
					moved = True
					print(f"\033[92m✓ Moved: {file} -> {key}\033[0m")
					break # Stop checking other categories once moved
				except Exception as e:
					print(f"⚠️ Error: {e}")
					moved = False
		
		# Check if file was not moved
		if not moved:
			print(f"\033[90m- Skipped: {file} (Unknown type)\033[0m")
			

if __name__ == "__main__":
	# Point this to your actual downloads folder
    # For WSL users accessing Windows:
	organize_directory("/mnt/c/Users/Bruno/Downloads")

