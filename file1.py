import os
from os.path import join, getsize
for root, dirs, files in os.walk('rsync project'):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))