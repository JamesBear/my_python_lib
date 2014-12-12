#!/usr/bin/python
# coding: utf-8

import os
import re


def get_file_content(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return content

def download_single(abs_url):
    #print('Downloading ', abs_url)
    cmd = 'wget --load-cookies cookies.txt --save-cookies cookies.txt --keep-session-cookies -E -H -k -p ' + abs_url
    os.system(cmd)

url_source_file = 'url_source.txt'
base_url = 'wiki.happyelements.net'
url_pattern = 'href="([^">].*?)"'

url_source_str = get_file_content(url_source_file)
r = re.compile(url_pattern)

def is_legal(relative_url):
    if relative_url == '#':
        return False

    return True

file_count = 0

for i in r.finditer(url_source_str):
    relative_url = i.group(1)
    if is_legal(relative_url):
        abs_url = base_url + relative_url
        print('Downloading file', file_count, ' ' + abs_url)
        download_single(abs_url)

