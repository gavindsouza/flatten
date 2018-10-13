"""
third party imports must be contained in a single package
import optimization to be done!!!
"""
# imports - standard imports
import os

# imports - module imports
from flatten.compress import Compress
from flatten.app.parser import get_parser_args
from flatten.app import USAGE_INSTR

# imports - third party imports
from matplotlib.pyplot import imread, imsave


def app():
    code = 0
    """
    everything will go in this method
    :return:
    """
    args = get_parser_args()

    img_path = args.src

    # if img src is provided
    if img_path not in [None, '', ' ']:
        # convert src img to numpy.ndarray to handle images
        img = imread(img_path)

        print("Soft Compression applied")
        imsave('soft_compressed_image.{}'.format(img_path.split('.')[-1]), Compress(img).compress_soft())

        print("Okay Compression applied")
        imsave('okay_compressed_image.{}'.format(img_path.split('.')[-1]), Compress(img).compress_okay())

        print("Hard Compression applied")
        imsave('hard_compressed_image.{}'.format(img_path.split('.')[-1]), Compress(img).compress_hard())

    # if img src not provided
    else:
        print(USAGE_INSTR)

    return code
