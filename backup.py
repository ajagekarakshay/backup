#!/usr/bin/python

import shutil, os

def main():
	drives = ["Movies & Games", "Softwares", "Entertainment"]
	src_drives = []
	dest_drives = []
	for drive in drives:
		src_drives.append("/media/root/"+drive)
		dest_drives.append("/media/root/AKSHAY AJAGEKAR/My Backup/"+drive)

	for i in range(3):
		print "* Backing up " + drives[i]
		backup(src_drives[i], dest_drives[i])
	
def list_files(path):
	files = []
	for name in os.listdir(path):
		files.append(os.path.join(path, name))
	return files

def backup(src, dest):
	src_items = list_files(src)
	dest_items = list_files(dest)
	for item in src_items:
		if item not in dest_items:
			if os.path.isfile(item):
				shutil.copy(item, dest)
			else
				shutil.copytree(item, )

if __name__ == '__main__':
	main()

