import os
import os.path

path1 = os.path.abspath('.')
print(path1)

path2 = os.path.splitext('md_os.py')
print(path2)

# os.mkdir('G:/py_crawler/os/testdir')
# os.rmdir('G:/py_crawler/os/testdir')
dirs = os.listdir('.')
for name in dirs :
    if os.path.splitext(name)[1] == '.py':
        print(name)