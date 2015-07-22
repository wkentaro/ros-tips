#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re


def get_rst_h1(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    h_pattern = re.compile('[-=\^]')
    for i, line in enumerate(lines):
        if h_pattern.match(line):
            if i == 0:
                title = lines[i+1].strip()
            if line[i-1].strip() != '':
                title = lines[i-1].strip()
            else:
                title = lines[i+1].strip()
            break
    return title


def main():
    files = os.listdir('.')
    pattern = re.compile('^\d{4,4}-\d{1,2}-\d{1,2}-.*')

    for file_ in files:
        if not (os.path.isdir(file_) and pattern.match(file_)):
            continue
        filename = os.path.join(file_, 'README.rst')
        title = get_rst_h1(filename)
        print('* `{label} <{url}>`_'.format(label=title, url=filename))


if __name__ == '__main__':
    main()