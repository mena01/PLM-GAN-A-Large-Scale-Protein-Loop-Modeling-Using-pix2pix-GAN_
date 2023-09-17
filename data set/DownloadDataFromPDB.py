#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:16:15 2021

@author: menanagy
"""
#https://github.com/collinarnett/protein_gan

from pathlib import Path
from urllib import request
from tqdm import tqdm

train_folder = Path("/download_dir_proteinsPDB")
train_list = Path('/train_ids.txt').read_text().splitlines()
 
train_folder.mkdir(exist_ok=True)

for ids in tqdm(test_list):
    p = test_folder / f'{ids}.pdb'
    if not p.exists():
        request.urlretrieve(f"http://files.rcsb.org/download/{ids}.pdb", p)
 
    
