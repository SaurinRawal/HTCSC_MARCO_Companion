#!/usr/bin/python
import argparse

def set_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--PATH', type=str,default='./images', help='path to image directory. Recursively finds all image files in directory and  sub directories') # path to image directory or containing sub directories.
    parser.add_argument('--MODEL_PATH', type=str, default='./savedmodel',help='the file path to the tensorflow model ')
    parser.add_argument('--CSV_PATH', type = str, default = './imageresults.csv',help = 'the csv file where results are written to')
    parser.add_argument('--HITS_PATH', type = str, default = './crystal_hits',help = 'Directory where hit images are stored')
    parser.add_argument('--COCKTAIL_PATH', type = str, default ='./17_C1536_B.csv', help = 'Directory where cocktail data is stored')

    return vars(parser.parse_args())
