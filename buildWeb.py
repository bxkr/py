from os import listdir
from os.path import isfile, join
from os import path
from os import popen
from json import dumps
cur_path = path.dirname(path.abspath(__file__))
file = path.basename(__file__)
files = [f for f in listdir(cur_path) if isfile(join(cur_path, f))]
del files[files.index(file)]
files_outputs = dict()
for filename in files:
    out = popen('python {f} {p}'.format(f=filename, p=cur_path)).read()
    files_outputs[filename] = out.strip()
with open('html/outputs.js', 'w') as data:
    data.write('const outputs = {}'.format(dumps(files_outputs)))