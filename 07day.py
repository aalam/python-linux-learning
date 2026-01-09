#2026Jan07 - system admin
#completed labex.io  - numeric, strings, boolean, operatos, type conversion

#https://python-memo.fabrice-salvaire.fr/examples/snippets/sysadmin.html
import os
import re
import subprocess
import tempfile


with tempfile.TemporaryFile() as fh:
    fh.write(b'Hello world!')
    fh.seek(0)
    print(fh.read())

with tempfile.TemporaryDirectory() as temp_directory:
    print('Created temporary directory', temp_directory)

#Create a filesystem hierarchy
with tempfile.TemporaryDirectory() as tmp_directory:
    print('Created temporary directory', tmp_directory)
    for directory in ('.', 'subdir'):
        directory_path = os.path.join(tmp_directory, directory)
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)
        for name in ('file1.txt', 'file.txt'):
            path = os.path.join(directory_path, name)
            with open(path, 'w') as fh:
                fh.write('...')
