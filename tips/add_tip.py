#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import datetime


def escape_for_filename(string):
    string = string.replace("'", '-dash-')
    string = string.replace(' ', '-')
    return string


def prepare_tip_dir(tip_dir, title=None):
    # create dir
    if os.path.exists(tip_dir):
        raise ValueError('{} already exists'.format(tip_dir))
    os.mkdir(tip_dir)
    # create README file
    with open(os.path.join(tip_dir, 'README.rst'), 'w') as f:
        if (title is not None) and (title.strip() != ''):
            lines = ['='*len(title), title, '='*len(title)]
            f.write('\n'.join(lines))
    # create image dir
    os.mkdir(os.path.join(tip_dir, 'images'))


def main():
    # date
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    print('created at:', date)
    # title
    title = raw_input('title?: ')
    # tip_dir
    tip_dir = '{}-{}'.format(date, escape_for_filename(title.lower()))
    print('tip_dir:', tip_dir)
    prepare_tip_dir(tip_dir, title=title)
    print('created dir at:', os.path.abspath(tip_dir))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass