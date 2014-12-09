#!/usr/bin/python

import os

source_file = 'floor_bricks.png'
prefix = 'floor_brick'
separator = '_'
extension = '.png'
start_index = 0
max_range = 1000

target_path = ''

for i in range(start_index, max_range):
    cur_path = prefix + separator + str(i) + extension
    if not os.path.exists(cur_path):
        target_path = cur_path
        break

cmd = 'cp ' + source_file + ' ' + target_path
cmd += '\nopen ' + target_path

print ('cmd', ' is: ', cmd)

os.system(cmd)
