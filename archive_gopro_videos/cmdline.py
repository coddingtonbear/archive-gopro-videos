from __future__ import print_function

import sys

import argparse
import six

from . import exceptions
from .main import copy_files_from_to


def main():
    parser = argparse.ArgumentParser(
        description='Archives folder from a mounted volume.'
    )
    parser.add_argument('volume_name', type=six.text_type)
    parser.add_argument('destination', type=six.text_type)

    args = parser.parse_args()

    try:
        copy_files_from_to(args.volume_name, args.destination)
    except exceptions.VolumeNotPresent:
        print("Volume not present")
        sys.exit(0)
    except exceptions.DestinationNotPresent:
        print("Volume not present")
        sys.exit(0)
