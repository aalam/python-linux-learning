#04Jan
#started with Admin task like path, os: https://docs.python.org/3/library/pathlib.html

from pathlib import Path
p = Path('.')
[x for x in p.iterdir() if x.is_dir()]

list(p.glob('**/*.py'))
p = Path('/etc')
q = p / 'init.d' / 'reboot'
q
q.resovle()

#Opening a file 
with q.open() as f: f.readline()
