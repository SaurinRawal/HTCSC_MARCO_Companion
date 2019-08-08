#!/usr/bin/python
# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
import os
import sys
import tensorflow as tf
import operator
import csv
import math
from os import listdir
from os.path import isfile, join
from shutil import copyfile
from File_Chem_Converter import *


def verify_location(location, dir=True):
    '''
    Tests if a path that is to be written to already exists or not. By defualt,
    assumes the path is a directory (dir=True). If path is to a file dir should
    be set to false and the path to the file will be created if it does not exist
    but the file will not be written.
    '''
    file_name = ''
    if dir is False:
        file_name = os.path.basename(location)
        location = location.replace(location, '')  # should add method to make sure remove last instance
    if os.path.exists is True:
        return True
    else:
        if dir is True: os.makedirs(location)


def test_write_locations(csv_path, hit_path):
    '''
    Tests if the write locations exist by calling verify_location. If location
    already exists will return True.
    '''
    write_locations = [(csv_path, False), (hit_path, True)]
    try:
        for location in write_locations:
            loc, dir = location
            verify_location(loc, dir)
    except FileExistsError:
        return True


def get_images(images_path):
    '''
    returns a list of all file paths contained in the given directory.
    '''
    allowed_file_types = ['.png', '.jpeg', '.jpg', '.bmp', '.gif']
    files = [os.path.join(images_path,f) for f in listdir(images_path)]
    for file in files:
        if os.path.splitext(file)[-1] not in allowed_file_types:
            files.remove(file)
    return files


def load_images(file_list):
    '''
    Loads images from a list of paths (should be from get_images) in format
    that can be read by the tensorflow package
    '''
    for i in file_list:
        files = open(i,'rb')
        yield {"image_bytes":[files.read()]},i


def run_model(tf_predictor, size, cocktail_dict, image_iterator):
    '''
    Runs the MARCO model on a collection of processed images. Returns a list of
    lists, each of which contains the information which will be written to the
    output csv files
    '''
    csv_output = []
    k = 0
    print('\nClassifying Images')
    for _ in range(size):
        k+=1
        data, name = next(image_iterator)
        sys.stdout = open(os.devnull, "w")
        results = tf_predictor(data)
        sys.stdout = sys.__stdout__

        vals = results['scores'][0]
        classes = results['classes'][0]
        dictionary = dict(zip(classes, vals))
        prediction = max(dictionary.items(), key=operator.itemgetter(1))[0]  # gets max confidence prediction
        well_number = get_well_number(str(name))
        cocktail = cocktail_dict[well_number]

        csv_output.append([name,(str(prediction))[2:-1],
                          str(dictionary[b'Crystals']),
                          str(dictionary[b'Other']),
                          str(dictionary[b'Precipitate']),
                          str(dictionary[b'Clear']),
                          well_number,
                          cocktail])
    return csv_output

def csv_validation(csv_path):
    DEFAULT_NAME = 'MARCO_results.csv'
    base = os.path.basename(csv_path)

    if csv_path.split('.')[-1] is not 'csv':
        return os.path.join(base, DEFAULT_NAME)
    else:
        return DEFAULT_NAME



def write_csv(csv_data, csv_path):
    '''
    Writes csv file from the csv_output created when run_model is executed
    '''
    
    print('\nFinishing up')
    with open(csv_path, 'w') as csvfile:
        writer = csv.writer(csvfile,
                            delimiter=',',
                            quotechar=' ',
                            quoting=csv.QUOTE_MINIMAL)
        # Write the header row for easier reading later
        writer.writerow(['Image path',
                        'Prediction',
                        'Crystal',
                        'Other',
                        'Precipitate:',
                        'Clear',
                        'Well',
                        'Cocktail'])
        print('\nWriting results')
        size = len(csv_data)
        for i, line in enumerate(csv_data):
            progress_bar(i, size)
            writer.writerow(line)
        print('\n')


def get_crystal_predictions(csv_path, hit_path):
    '''
    After the Csv with all results is writtn by write_csv, goes back and extract
    the images that were classified as a crystal. These images are then copied to
    a new directory and a csv file with their information is written to the
    same location.
    '''
    if not os.path.exists(hit_path):
        os.makedirs(hit_path)

    high_cons = []
    try:
        with open(csv_path) as results:

            results_reader = csv.DictReader(results, delimiter = ',', quotechar = '"')
            for result in results_reader:
                if result['Prediction'] == 'Crystals' and float(result['Crystal']) >= .70:
                    image = str(result['Well']) + '.jpg'

                    copyfile(result[' Image  path '], os.path.join(hit_path, image))
                    high_cons.append(str(result['Well']) + ',' + str(result['Cocktail']) + '\n')
                    # want to rewrite filename or add somekind of log file ti interpret
    except FileNotFoundError:
        print('File not found at get_crystal_predictions')

    with open(os.path.join(hit_path, 'X-tal_hits_cocktails.csv'), 'w') as xtal_hits:
        for line in high_cons:
            xtal_hits.write(line)


def play_sound():
    '''
    Plays a fun chime
    '''
    duration = 0.1  # seconds
    freq = [450,400,500,700,1200]  # Hz
    for f in freq:
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, f))


def progress_bar(prog, size_work):
    '''
    Prints a progess bar, total size will always be =*16. Should not be interpreted
    as exact and is mostly there to give you something to look at while the
    method it is contained within runs.
    '''
    NUM_TICKS = 16
    sys.stdout.write('\r')
    current_ticks = math.ceil(prog*NUM_TICKS/size_work)
    percent = str(current_ticks / NUM_TICKS * 100) + '%'
    sys.stdout.write("Progress: |{}{}| {}".format('='*current_ticks, ' '*(NUM_TICKS-current_ticks), percent))
