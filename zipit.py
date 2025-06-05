#!/bin/python3
import os
import math
import random
import time

zippers=["xz","gzip","bzip2","lzip","lzma","lzop","zstd"]
og_files=["rand",'IMG7110.jpg','lmms.AppImage']

iterations=16

outs=[]

data=[]

def run(cmd):
    print("   > "+cmd)
    os.system(cmd)

def zip_file(file,zipper,i):
    inp=f"{file}.{zipper}.{i}"
    out=f"{file}.{zipper}.{i+1}"
    #run(f"cp '{file}' '{inp}'")
    run(f"{zipper} --stdout {inp} > {out}")
    outs.append(out)
    return out

def run_zips(og,zipper,iters):
    run(f"cp {og} {og}.{zipper}.0")
    for i in range(iters):
        start=time.perf_counter()
        out=zip_file(og,zipper,i)
        end=time.perf_counter()
        data.append({
            "file":og,
            "out":out,
            "zipper":zipper,
            "iter":i+1,
            "time":end-start,
            "size":os.path.getsize(out)
        })

#run_zips("flowers-d.rwp","lzop",3)

for f in og_files:
    for z in zippers:
        run_zips(f,z,iterations)

with open('data.2.csv','w') as f:
    keys=list(data[0].keys())
    for k in keys:
        f.write(k+",")
    f.write("\n")
    for d in data:
        for k in keys:
            f.write(str(d[k])+',')
        f.write('\n')

if input('clean up?')=='y':
    for o in outs:
        run('rm '+o)
