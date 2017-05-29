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
import re
from os import environ

from os.path import exists

import sys

import time

RESET = '\033[0m'
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def termcolor(fg=None, bg=None):
    codes = []
    if fg is not None: codes.append('3%d' % fg)
    if bg is not None: codes.append('10%d' % bg)
    return '\033[%sm' % ';'.join(codes) if codes else ''


def colorize(message, fg=None, bg=None):
    return termcolor(fg, bg) + message + RESET


NO_HOME_PATH = re.compile(r'~/(.*)')
home_path = environ['HOME']


def handle_home_case(path):
    path = path.strip()
    if path.startswith('~/'):
        path = home_path + '/' + NO_HOME_PATH.match(path).groups()[0]
    return path


def select_conf_file():
    src_value_re = re.compile(r'src *= *(.*)')
    dst_value_re = re.compile(r'target *= *(.*)')

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

        src_re = src_value_re.match(line)
        if src_re is not None:
            src_value = src_re.groups()[0]
            if src_value is not None:
                src = handle_home_case(src_value)
                print 'the source directory is assigned to ' + colorize(src, fg=BLACK, bg=GREEN)
                continue

        dst_re = dst_value_re.match(line)
        if dst_re is not None:
            dst_value = dst_re.groups()[0]
            if dst_value is not None:
                dst = handle_home_case(dst_value)
                print 'the target directory is assigned to ' + colorize(dst, fg=BLACK, bg=GREEN)
                continue

        print colorize('unknown line on conf file: ' + line)

    conf_file.close()

    return src, dst, conf_path

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def show_spinner(thread):
    spinner = spinning_cursor()
    while thread.isAlive():
        sys.stdout.write(spinner.next())
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
