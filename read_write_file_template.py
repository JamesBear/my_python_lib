#!/usr/bin/python

def get_file_content(file_path):
    f = open(file_path, 'r')
    file_content = f.read()
    f.close()
    return file_content

def write_to_file(file_path, file_content):
    f = open(file_path, 'w')
    f.write(file_content)
    f.close()

