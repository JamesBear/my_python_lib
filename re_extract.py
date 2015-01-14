#!/usr/bin/python
import re
import sys

def get_file_content(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return content

pattern = sys.argv[1]
source_path = sys.argv[2]

#pattern = '^([A-bZ_]+)'
flags = re.MULTILINE
r = re.compile(pattern, flags)

source_str = get_file_content(source_path)

for i in r.finditer(source_str):
    print(i.group(1))

