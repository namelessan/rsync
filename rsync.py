#!/usr/bin/env python3

import argparse
import os
import stat
import difflib


""" os.path module
    os.difflib module
    os.open, os.read, os.write, os.sendfile, os.lseek
    os.mkdir
    os.stat module
    os.symlink(create a symlink to source), os.link(create a hard link to source), os.readlink
    os.scandir
    os.unlink
    os.utime(set the atime and mtime), os.chmod(change mode of dest)"""


def handleArgs():
    """config the usage of rsync and arguments"""
    parser = argparse.ArgumentParser(prog='./rsync.py',
        description="Sync the Destination file with the Source file")
    parser.add_argument('SOURCE', action='store', help='Source file name to sync')
    parser.add_argument("DESTINATION", action='store',
                        help='Destination file name to be synced')
    parser.add_argument('-c', action='store_true', default=False,
                        dest='checksum', help='Check sum mode')
    parser.add_argument('-u', action='store_true', default=False,
                        dest='update', help='Update mode')
    parser.add_argument('-r', action='store_true', default=False,
                        dest='recursive', help='recursive mode')
    return parser.parse_args()


def isHardlink(file):
    '''Input file is a path or file descriptor'''
    # Return True is file has hardlink
    return os.lstat(file).st_nlink > 1


def isUpdated(source, dest):
    '''Input: source, dest is a path or file descriptor'''
    # Return True if source and dest have same size and access time
    source_stats = os.stat(source)
    dest_stats = os.stat(dest)
    return source_stats.st_size == dest_stats.st_size and\
        source_stats.st_mtime == dest_stats.st_mtime


def rsyncPermission(source, dest):
    '''Input: source, dest is folder, file path or descriptions'''
    try:
        # Get permission of the source
        source_stats = os.stat(source)
        source_permission = stat.S_MODE(source_stats.st_mode)
        # Change permission of the destination
        os.chmod(dest, source_permission)
        return 'Success: rsync permission'
    # Return message if get any errors
    except Exception:
        return 'Unsuccess: rsync permission due to some errors'


def rsyncTime(source, dest):
    try:
        s = os.stat(source)
        # Change atime and mtime of the destination
        os.utime(dest, (s.st_atime, s.st_mtime))
        return "Success: rsync time"
    # Return message if get any errors:
    except Exception:
        return 'Unsuccess: rsync time due to some errors'


def rsyncFileToFile(source, dest):
    # Rewrite all the content of the dest
    with open(source, 'r') as file1, open(dest, 'w+') as file2:
        source_content = file1.read()
        file2.write(source_content)


# def rsyncSymlinktoSymlink(source, dest):



if __name__ == '__main__':
    args = handleArgs()
    # Get source input and destination input
    source = args.SOURCE
    dest = args.DESTINATION

    # If source doesn't exists
    if not os.access(source, os.F_OK):
        # Print out error
        print("rsync: link_stat {} failed: No such file or directory"
                .format(os.path.join(os.getcwd(), source)))
        print("rsync error: some files/attrs were not transferred")

    # If source doesn't have read permission
    elif not os.access(source, os.R_OK):
        # Print out error
        print("rsync: send_files failed to open {}: Permission denied"
                .format(os.path.join(os.getcwd(), source)))
        print("rsync error: some files/attrs were not transferred")

    # If source exists and have read permission
    else:
        # If destination doesn't exists
        if not os.access(dest, os.F_OK):
            # If dest is a folder name
            if '/' in dest:
                os.mkdir(dest, 0o664)
            # If dest is a file name
            else:
                file = os.open(dest, 'w')
                file.close()
        # If destination is not directory and  doesn't have read and write permission
        if not os.path.isdir(dest) and  not os.access(dest, os.R_OK or os.W_OK):
            # Save dest permission
          dest_stats = os.stat(dest)
          dest_permission = stat.S_MODE(dest_stats.st_mode)
          # Change dest permission
          os.chmod(dest, 0o777)
          pass

        # If source is directory
        if os.path.isdir(source):
            if not recursive:
                print('skiping directory')
            else:
                pass

        # If source is file
        elif os.path.isfile(source):
            pass

        # If source is symlink
        elif os.path.islink(source):
            # do something
            pass

        # If source is hardlink
        elif isHardLink(source):
            pass
