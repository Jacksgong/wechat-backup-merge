#!/usr/bin/python -u

"""
Copyright 2017, Jacksgong(https://blog.dreamtobe.cn)
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Script to merge and migrate wechat backup on mac.
# Some case like you can merge and migrate wechat backup files to the Dropbox auto-backup folder to make it on cloud.

import sys
import time
import filecmp
import re
from os import walk, makedirs, remove, environ
from os.path import join, exists, getsize
from shutil import copyfile
from threading import Thread

from wechat_backup_utils import colorize, YELLOW, RED, GREEN, BLACK, handle_home_case, select_conf_file, show_spinner

__version__ = '1.0.0'


def replace_file(src_path, dst_path, name):
    print colorize('replace the file: ' + name, fg=YELLOW)
    remove(dst_path)
    copyfile(src_path, dst_path)


def merge():
    if not exists(dst_file_path):
        if not exists(dst_subdir):
            makedirs(dst_subdir)
        copyfile(src_file_path, dst_file_path)
        print colorize('copy the new file: ' + file_name, fg=RED)
    else:
        # compare the file size
        src_file_size = getsize(src_file_path)
        dst_file_size = getsize(dst_file_path)

        if src_file_size != dst_file_size:
            replace_file(src_file_path, dst_file_path, file_name)
        else:
            # compare the file
            if not filecmp.cmp(src_file_path, dst_file_path):
                replace_file(src_file_path, dst_file_path, file_name)
            else:
                print colorize('no need to replace ' + file_name, fg=GREEN)


src, dst, conf_path = select_conf_file()

if src is None or dst is None:
    exit(colorize("we can't find source directory or target directory on " + conf_path))

RELATE_DIR = re.compile(r'' + src + '/(.*)')
for src_subdir, dirs, files in walk(src):
    for file_name in files:
        if file_name == '.DS_Store':
            continue

        if src_subdir == src:
            continue

        relate_dir = RELATE_DIR.match(src_subdir).groups()[0]
        dst_subdir = dst + '/' + relate_dir

        src_file_path = join(src_subdir, file_name)
        dst_file_path = join(dst_subdir, file_name)
        print 'compare ' + file_name + ' on ' + relate_dir

        thread = Thread(target=merge)
        thread.start()

        show_spinner(thread)

print 'everything is done!'
