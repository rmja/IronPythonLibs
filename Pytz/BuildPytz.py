pyc_path = r'C:\Program Files (x86)\IronPython 2.7\Tools\Scripts'
pytz_path = r'pytz-2015.7'
zoneinfo_path = r'pytz-2015.7\pytz\zoneinfo'

import sys
sys.path.append(pyc_path)

import os, fnmatch
import pyc

# Find all py files recursively.
files = []
for root, dirnames, filenames in os.walk(pytz_path):
    for filename in fnmatch.filter(filenames, '*.py'):
        files.append(os.path.join(root, filename))

# Concatenate with pyc arguments.		
args = ['/target:dll', '/out:Pytz'] + files 

# Run pyc.
pyc.Main(args)