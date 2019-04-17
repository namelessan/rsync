#!/usr/bin/env python3
import os
import stat
import difflib

#
def getInfo(file):
    # file: input is a file descriptor or a path
    stats = os.stat(file)
    file_info = {}
    file_info['mode'] = stat.S_IMODE(stats.st_mode)
    file_info['atime'] = stats.st_atime
    file_info['mtime'] = stats.st_mtime
    file_info['ctime'] = stats.st_ctime
    # Return file_info is a dictionary of mode, access time, modification time, last metadata change time
    return file_info


def syncFileToFile(source, dest, update=False):
    if update = False:
        with open(source, "r") as source_file, open(dest, "w+") as dest_file:
            source_text = source_file.read()
            dest_file.write(source_text)
    elif update = True:
        #write code here
        pass

# file_info = getFileInfo("file1.py")
# print(file_info)
# print(syncFileToFile("file1.py", "astar_maze_ia"))
with open('file1.py', 'r') as source_file:
    source_text = source_file.read()
with open('copiedfromfile1.py', 'w+') as dest_file:
    dest_file.write(source_text)