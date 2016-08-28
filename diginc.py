#!/usr/bin/env python

import argparse

from parse import parse_listing_file
from kml import KML

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--test', action='store_true', help='If flag is '
                    'present, does not run geocode lookup.')
parser.add_argument('file')

params = parser.parse_args()
file = open(params.file)

listings = parse_listing_file(file)

kml_generator = KML(test=params.test)
kml_generator.generate_from_listings(listings)
