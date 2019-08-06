import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import colors
from PIL import Image
import numpy as np
import seaborn as sns
import csv
import os
import math
from mpl_toolkits.mplot3d import Axes3D



def make_picks(picks_dir, cocktails, filename='picks.csv'):
    image_paths = os.listdir(picks_dir)
    images = [os.path.basename(image).split('.')[0] for image in image_paths]

    try:
        cocktail_dict = {}
        with open(cocktails) as cock:
            cock_reader = csv.reader(cock)
            for line in cock_reader:
                cocktail_dict[line[0]] = line[1:-1]

        with open(filename, 'w') as filename:
            for image in images:
                row = '{},{}\n'.format(image, cocktail_dict[image])
                filename.write(row)
                print(row)

    except FileNotFoundError as e:
        return e
'''
make_picks('/home/ethan/Documents/github/models/research/marco/158_screen/round_3/hits/picks',
'/home/ethan/Documents/github/models/research/marco/17_C1536_B.csv',
'/home/ethan/Documents/github/models/research/marco/158_screen/round_3/hits/picks/picks.csv'  )
'''


def find_clusters(well_list):
    '''
    Takes list of well numbers are returns lists of closely
    clusterd wells
    '''
    well_ints = [int(well) for well in well_list]
    well_ints.sort()


def extract_xtal_confidence(csv_results):
    plate_size = 1536
    try:
        with open(csv_results) as marco:
            well_list = [0 for x in range(0, plate_size)]
            results = csv.DictReader(marco, delimiter = ',', quotechar = '"')
            for result in results:
                well_list[int(result['Well'])-1] = result['Crystal']  # assigns crystal confidence to correct index
                # subtract 1 to avoid index errors
        return np.asarray(well_list, dtype='float').reshape(32, 48)

    except FileNotFoundError as e:
        return e

def linear_plate_to_matrix_location(index, rows=32, columns=48):
    row_index = math.floor(index / columns)
    column_index = index - (row_index * columns)

    return tuple([row_index, column_index])



def scatter_plot_hits(csv_file, threshold=.94, alpha=1, title='Title'):
    '''
    uses marco results csv to make scatter plot of the xtal
    hits above a given threshold
    '''
    x = []
    y = []
    plate = extract_xtal_confidence(csv_file).flatten()

    for i, well in enumerate(plate):
        if well >= threshold:
            x_cor, y_cor = linear_plate_to_matrix_location(i)
            x.append(x_cor)
            y.append(y_cor)

    plt.scatter(x, y, alpha=alpha)
    plt.suptitle(title)
    plt.xlabel("x-label")
    plt.ylabel("y-label")
    plt.show()



def overlayed_hits(csv_files, threshold=10):
    '''
    uses marco results csv from the three peptides and
    overlays the results. For this plot to make sense csv
    files should all be from the same screening run time.
    '''
    for csv_file in csv_files:
        scatter_plot_hits(csv_file)
    plt.show()


def make_crystal_map(MARCO_CSV, show=False):

    np_wells = extract_xtal_confidence(MARCO_CSV)

    title = os.path.basename(MARCO_CSV.split('.')[0] + ' Crystal Confidence')
    ax = sns.heatmap(np_wells, linewidth=0, cmap = 'jet', )
    ax.set_title(title)
    if show is True:
        plt.show()
    return ax

#make_crystal_map('/home/ethan/Documents/github/models/research/marco/159_screen/round_3/159_MARCO_round_3.csv', True)

def get_best_factors(items):
    factors = []
    for i in range(1,num+1):
        if num%i==0:
            factors.append(i)



def image_plots(image_dir):
    files = os.listdir(image_dir)
    files = [file for file in files if 'jpg' in file]

    print('This is file length')
    print(len(files))

    fig, axes = plt.subplots(32, 47)
    i = 0
    for ax in axes.flat:
        image = Image.open(os.path.join(image_dir, files[i]))
        well = os.path.basename(files[i]).split('.')[0]

        image.thumbnail((500, 500), Image.ANTIALIAS)
        im = ax.imshow(image)
        #ax.text(1, 1, well, horizontalalignment='right',
        #     verticalalignment='top', transform=ax.transAxes)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.set_aspect('equal')
        i+= 1
        print(i)

    figure = plt.gcf() # get current figure
    figure.set_size_inches(12, 8)
    # when saving, specify the DPI
    plt.savefig('/home/ethan/Documents/IMCA-CAT/test_pig', dpi=1000)


image_plots('/home/ethan/Documents/github/models/research/marco/X000015685-jpg/X000015685201907121609-jpg')


def multiplot(csv_list, rows=3, columns=3, title='Multiplot'):
    '''
    ploting method designed to plot multible MARCO heatmaps
    with one color bar.
    Number of rows and columns must make sense with length of
    the csv_list
    '''
    fig, axes = plt.subplots(rows, columns)
    i = 0
    subtitle_list = ['P158: 12 hrs', 'P158: 24 hrs', 'P158: 1 Week', 'P158'
                     'P159: 12 hrs', 'P159: 24 hrs', 'P159: 1 Week',
                     'P160: 12 hrs', 'P160: 24 hrs', 'P160: 1 Week']

    for ax in axes.flat:
        im = ax.imshow(extract_xtal_confidence(csv_list[i]),cmap='Oranges')
        ax.set_title(subtitle_list[i])
        i += 1

    plt.tight_layout()
    #fig.suptitle(title)
    fig.colorbar(im,
                 ax=axes.ravel().tolist(),
                 orientation='vertical',
                 fraction=.1)
    plt.show()

rounds_160 = [
'/home/ethan/Documents/github/models/research/marco/158_screen/round_1/158_round_1.csv',
'/home/ethan/Documents/github/models/research/marco/158_screen/round_2/158_round_2.csv',
'/home/ethan/Documents/github/models/research/marco/158_screen/round_3/158_round_3.csv',
'/home/ethan/Documents/github/models/research/marco/159_screen/round_1/159_round_1.csv',
'/home/ethan/Documents/github/models/research/marco/159_screen/round_2/159_round_2.csv',
'/home/ethan/Documents/github/models/research/marco/159_screen/round_3/159_round_3.csv',
'/home/ethan/Documents/github/models/research/marco/160_screen/round_1/160_round_1.csv',
'/home/ethan/Documents/github/models/research/marco/160_screen/round_2/160_round_2.csv',
'/home/ethan/Documents/github/models/research/marco/160_screen/round_3/160_round_3.csv'
]

#overlayed_hits([rounds_160[2], rounds_160[5], rounds_160[8]])
multiplot(rounds_160)
