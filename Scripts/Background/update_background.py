#!/bin/python3
from pathlib import Path
import os
from typing import List, Dict
import subprocess

simple_map: Dict[str, str] = {
'/home/archdrema/Workspace': 'Images/StarDestroyer.jpg',
'/': 'Images/Tatooine.jpg',
'/home/archdrema/Workspace/BaumanSemester3': 'Images/Hyperjump.jpg'
}

wd = '/home/archdrema/Workspace/Archlinux/Scripts/Background'

cur_d = os.getcwd()

def get_img(cur_path: str):
    cur: Path = Path(cur_path)
    path_keys: List[str] = []
    for el in simple_map:
        path_keys.append(el)
    for root_path in sorted(path_keys, key=lambda path: os.path.normpath(path).count('/'), reverse=True):
        root = Path(root_path)
        #print(f'{root_path} {root == cur} {root_path == cur_path} {root in cur.parents}')
        if root == cur or root in cur.parents:
            return simple_map[root_path]
    return None

new_bg = get_img(cur_d)

if new_bg is not None:
    #subprocess.run(['setbg', new_bg], stdout=subprocess.DEVNULL, cwd=wd)
    subprocess.run(['setbg', new_bg], cwd=wd)
