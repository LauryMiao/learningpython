#!/usr/bin/python

#
# Backup the specific files.
#"""

import os
import re
import time
import shutil


def FileBackup(file_kind, destination_directory):

    file_list = [f for f in os.listdir('.') if f.endswith(file_kind)]

    for file in file_list:
        t_backup = time.strftime('%Y_%m_%d', time.localtime(time.time()))
    new_file_name = destination_directory + t_backup + file
    shutil.copy2(file, new_file_name)

FileBackup('.py', 'E:/test/')
FileBackup('.rar', 'E:/test/')
FileBackup('.zip', 'E:/test/')
print("All the files have been backuped!")
