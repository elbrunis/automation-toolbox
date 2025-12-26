import os
import shutil

# ===============================================================
#    dejar bonito el codigo y limpiarlo para subirlo a linkedin 
# ===============================================================

def organizar_descargas(download= "~/Descargas"):
	# Returns Download path

	download_path = os.path.expanduser(download)
	# Library of types

	types = {
		"imagenes": [".jpg", "jpeg", ".png", ".gif"],
		"documentos": [".pdf", ".txt", ".docx"],
		"videos": [".mp4", ".avi", ".mov"],
		"comprimidos": [".zip", ".rar", ".7z"],
		"ejecutables": [".exe", ".com", ".bat", ".msi"] # son solo ejecutables de windous

	}

	# Search directories and create them if they don't exist
	for directory in types.keys():
		directory_path = os.path.join(download_path, directory)
		if not os.path.exists(directory_path):
			os.mkdir(directory_path)

	# Organize folders
	for file in os.listdir(download_path):
		file_path = os.path.join(download_path, file)
		# If it is a file, we check its type
		if os.path.isfile(file_path):
			ext = os.path.splitext(file)[1]
			for key, val in types.items():
				i = 0
				moved = False
				while i < len(val):
					if ext == val[i]:
						key_path = os.path.join(download_path, key)
						shutil.move(file_path, key_path)
						moved = True
						print(f"\033[92m✓ Movido: {file} -> {key}\033[0m")
					if moved:
						break
					i += 1
				if moved:
					break
			if not moved:
				print(f"\033[91mX No movido: {file} no esta especificado el tipo\033[0m")
			

if __name__ == "__main__":
	organizar_descargas(download= "/mnt/c/Users/Bruno/Downloads")

