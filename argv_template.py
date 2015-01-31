#!/usr/bin/python

import sys

option_dict = {}

def get_file_content(file_path):
    f = open(file_path, 'r')
    file_content = f.read()
    f.close()
    return file_content

def write_to_file(file_path, file_content):
    f = open(file_path, 'w')
    f.write(file_content)
    f.close()

    
def parse_option_dict(argv):
    i = 0
    while i < len(argv):
        if argv[i] == '-v' or argv[i] == '--verbose':
            option_dict['-v'] = True
        elif argv[i] == '-t' or argv[i] == '--test':
            option_dict['-t'] = True
        i += 1
    return

def print_help():
    print('Usage:')
    print('  ./PROGRAM_NAME.py test')
    print('  ./PROGRAM_NAME.py help')

def test():
    print('This is a test.')
    

def run_command(argv):

    parse_option_dict(argv)
    
    if len(argv) <= 1:
        print_help()
    elif argv[1] == 'test':
        test()
    else:
        print_help()

run_command(sys.argv)
