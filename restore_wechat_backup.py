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

# Script to restore wechat backup on mac.

from os.path import exists
from shutil import copytree
from threading import Thread

from wechat_backup_utils import select_conf_file, colorize, RED, GREEN, show_spinner

src, dst, conf_path = select_conf_file()

if src is None or dst is None:
    exit(colorize("we can't find source directory or target directory on " + conf_path, fg=RED))

if exists(src):
    exit(colorize(
        "the src directory['" + src + "']is exist, if you want to restore, please remove the src directory first",
        fg=RED))

if not exists(dst):
    exit(colorize("we can't find backup files on " + dst, fg=RED))

print colorize("start restore " + dst + " to " + src, fg=GREEN)

thread = Thread(target=copytree, args=[dst, src])
thread.start()
show_spinner(thread)

print 'everything is done!'
