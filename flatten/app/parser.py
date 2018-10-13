# imports - module imports
from flatten.__attr__ import __version__, __description__

# imports - standard import
import argparse

USAGE_INSTR = ("\nIf image source is not mentioned app will exit"
               "\nThe bare minimum for its usage is as:"
               "\npython -m flatten --src 'IMG_PATH'"
               "\nFor further help see --help or -h")


def get_parser():
    parser = argparse.ArgumentParser(
        description=__description__ + USAGE_INSTR

    )

    # if problems occur, it's the line below <--------------------------------------------------------------- :)
    parser.parse_args()

    parser.add_argument("-s", "--src",
                        action="store_true",
                        help="add source of image to be compressed"
                        )

    parser.add_argument("-V", "--verbose",
                        action="store_true",
                        help="Display verbose output"
                        )

    parser.add_argument("-v", "--version",
                        action="version",
                        version=__version__
                        )

    return parser


def get_parser_args():
    parser = get_parser()
    args, _ = parser.parse_known_args()

    return args
