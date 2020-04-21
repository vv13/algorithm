import shutil
import os

src = '../leetcode'
for _dir in os.listdir(src):
    if '.' not in _dir:
        continue
    
    _from = os.path.join(src, _dir, 'relation.json')
    if os.path.exists(_from):
      _target = os.path.join(src, _dir, 'information.json')
      shutil.move(_from, _target)

