#!/usr/bin/env python

import argparse

from parse import parse_listing_file
from kml import KML

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('filename')

params = parser.parse_args()
file = open(params.file)

listings = parse_listing_file(file)

kml_generator = KML(unicode(params.filename, 'utf8'))
kml_generator.generate_from_listings(listings)
