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

RESET = '\033[0m'
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def termcolor(fg=None, bg=None):
    codes = []
    if fg is not None: codes.append('3%d' % fg)
    if bg is not None: codes.append('10%d' % bg)
    return '\033[%sm' % ';'.join(codes) if codes else ''


def colorize(message, fg=None, bg=None):
    return termcolor(fg, bg) + message + RESET


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


def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


NO_HOME_PATH = re.compile(r'~/(.*)')
home_path = environ['HOME']


def handle_home_case(path):
    path = path.strip()
    if path.startswith('~/'):
        path = home_path + '/' + NO_HOME_PATH.match(path).groups()[0]
    return path


SRC_VALUE = re.compile(r'src *= *(.*)')
DST_VALUE = re.compile(r'target *= *(.*)')

conf_path = 'example_path.conf'
if exists('path.conf'):
    conf_path = 'path.conf'
    print colorize("we will read config from path.conf file.", fg=GREEN)
else:
    print "we can't find path.conf file, so we using the example_path.conf file as the config file."

src = None
dst = None

conf_file = open(conf_path, 'r')
for line in conf_file:
    if line.startswith('#') or line.startswith('//'):
        continue
    unknown_line = True
    src_re = SRC_VALUE.match(line)
    if src_re is not None:
        src_value = src_re.groups()[0]
        if src_value is not None:
            src = handle_home_case(src_value)
            unknown_line = False
            print 'the source directory is assigned to ' + colorize(src, fg=BLACK, bg=GREEN)
    else:
        dst_re = DST_VALUE.match(line)
        if dst_re is not None:
            dst_value = dst_re.groups()[0]
            if dst_value is not None:
                dst = handle_home_case(dst_value)
                unknown_line = False
                print 'the target directory is assigned to ' + colorize(dst, fg=BLACK, bg=GREEN)

    if unknown_line:
        print colorize('unknown line on conf file: ' + line)
conf_file.close()

if src is None or dst is None:
    exit(colorize("we can't find source directory or target directory on " + conf_path))

RELATE_DIR = re.compile(r'' + src + '/(.*)')
spinner = spinning_cursor()
for src_subdir, dirs, files in walk(src):
    for file_name in files:
        if file_name == '.DS_Store':
            continue

        relate_dir = RELATE_DIR.match(src_subdir).groups()[0]
        dst_subdir = dst + '/' + relate_dir

        src_file_path = join(src_subdir, file_name)
        dst_file_path = join(dst_subdir, file_name)
        print 'compare ' + file_name + ' on ' + relate_dir

        thread = Thread(target=merge)
        thread.start()

        while thread.isAlive():
            sys.stdout.write(spinner.next())
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')

print 'everything is done!'
