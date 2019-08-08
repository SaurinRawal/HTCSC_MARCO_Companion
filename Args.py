#!/usr/bin/python
from argparse import ArgumentParser
from gooey import GooeyParser
from gooey import Gooey


@Gooey(program_name='HTCSC MARCO Companion',
       image_dir='./images',
       header_bg_color='#adb2ff',
       )

def set_args():
    parser = GooeyParser()
    parser.add_argument('PATH',
                        type=str,
                        help='Path to image directory.',
                        widget='DirChooser'
                        ) # path to image directory or containing sub directories.
    parser.add_argument('MODEL_PATH',
                        type=str,
                        help='File path to the tensorflow model',
                        widget='DirChooser')
    parser.add_argument('CSV_PATH',
                        type = str,
                        help = 'The directoy where where results csv are written to',
                        widget='DirChooser')
    parser.add_argument('HITS_PATH',
                        type = str,
                        help = 'Directory where crystal images are stored',
                        widget='DirChooser')
    parser.add_argument('COCKTAIL_PATH',
                        type = str,
                        help = 'Path to cocktails csv',
                        widget ='FileChooser')
    parser.add_argument('--LOUD',
                        type=bool,
                        default='False',
                        help='If set to true plays a tone when program completes',
                        )

    return vars(parser.parse_args())
