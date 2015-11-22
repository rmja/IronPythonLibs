ip_path = r'C:\Program Files (x86)\IronPython 2.7'
pyc_path = ip_path + r'\Tools\Scripts'
stdlib_path = ip_path + r'\Lib'

import sys
sys.path.append(pyc_path)

import os, fnmatch
import pyc

# Find all py files recursively.
files = []
for root, dirnames, filenames in os.walk(stdlib_path):
    for filename in fnmatch.filter(filenames, '*.py'):
        files.append(os.path.join(root, filename))

# Remove multiprocessing files as they fails to compile.
files = [file for file in files if not 'multiprocessing' in file]

# Concatenate with pyc arguments.		
args = ['/target:dll', '/out:StdLib27'] + files 

# Run pyc.
pyc.Main(args)