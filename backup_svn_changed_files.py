#!/usr/bin/python
# coding: utf-8

import os
import re
import datetime
import shutil

now = datetime.datetime.now()
str_time = now.strftime('%Y%m%d_%H%M%S')
backup_dir = '../../backup_' + os.path.basename(os.path.abspath('.')) + '/' + str_time
print ('backup_dir is', backup_dir )


def backup(src):
    if os.path.isfile(src):
        parent =  os.path.dirname(src)
        dest_parent = backup_dir + '/' + parent
        os.makedirs(dest_parent, exist_ok = True)
        shutil.copy(src, dest_parent)
    elif os.path.isdir(src):
        dest = backup_dir + '/' + src
        os.makedirs(dest, exist_ok = True)
    else:
        print("Can't handle: ", src)
        return False

    return True


a = os.popen('svn status', 'r').read()
p = '[?MAD]\s*(.*)'
r = re.compile(p)
for i in r.finditer(a):
    #print(i.groups())
    target = i.group(1)
    if backup(target):
        print(target)
    #print(os.path.dirname(i.group(1)))
