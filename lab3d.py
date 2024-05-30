#!/usr/bin/env python3
'''Lab 3 Part 4 function free_space'''
# Author ID: Jad Kaai

import subprocess

def free_space():
    result = subprocess.run(['df', '-h'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').split('\n')
    root_line = [line for line in output if line.endswith('/')]
    if root_line:
        free_space = root_line[0].split()[3]
        return free_space.strip()

if __name__ == '__main__':
    print(free_space())
