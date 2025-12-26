from datetime import datetime
import os
import shutil
import sys

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
GRAY = "\033[90m"

#this fun gets the date of the last modification
def	get_lmdate(backup_path: str) -> datetime:
	lst_mmtime = os.path.getmtime(backup_path)
	lst_mdate = datetime.fromtimestamp(lst_mmtime)
	return lst_mdate

def delete_old_backups(backup_path: str, current_date: datetime):
	print(F"{GRAY}Current date: {current_date}{RESET}")
	for file in os.listdir(backup_path):
		if file.endswith(".zip"):
			file_path = os.path.join(backup_path, file)
			file_date = get_lmdate(file_path)
			result = current_date - file_date
			print(result)
			if result.days >= 7:
				os.remove(file_path)

def create_backup(src_path: str) -> str:
	backup_path = "/mnt/c/Users/Bruno/Documents/img_backup/"
	os.makedirs(backup_path, exist_ok=True)
	current_date = datetime.now()
	tmp_date = current_date.strftime("%Y-%m-%d_%H-%M")
	new_backup_path = f"{backup_path}backup_{tmp_date}"
	if os.path.exists(src_path):
		delete_old_backups(backup_path, current_date)
	cpy_path = shutil.make_archive(new_backup_path, 'zip', src_path)
	return cpy_path
			

if __name__ == "__main__":
	new_backup_path = create_backup("/mnt/c/Users/Bruno/Pictures")
	if new_backup_path:
		print(f"{GREEN}Success: Backup created successfully.{RESET}")
	else:
		print(f"{RED}Error: Backup could not be created.{RESET}")
