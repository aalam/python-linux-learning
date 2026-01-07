#04Jan
#back to basic: https://labex.io/learn/python
# https://github.com/ckan/ckan - this calim Govt of Canada has larget dataset available
# https://python-memo.fabrice-salvaire.fr/examples/snippets/sysadmin.html Is this memo good for SysAdmin?
#started with Admin task like path, os: https://docs.python.org/3/library/pathlib.html
#https://labex.io/pythoncheatsheet/ CheatSheet?
#

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
