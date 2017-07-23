"""remove big file with argparse"""
import os,sys
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-f','--file', type=str, required=True)
ap.add_argument('-s','--size', type=float, required=True)
args = ap.parse_args()
for i in os.listdir(args.file):  
    x = int(os.stat(i).st_size)
    if x > (args.size * 1024):
        if raw_input("do you want to remove this big file %s ?" %(i)) == "yes" :
            os.remove(i)