#!/usr/bin/env python

import argparse

from parse import parse_listing_file
from kml import KML

parser = argparse.ArgumentParser()
parser.add_argument('file')

params = parser.parse_args()
file = open(params.file)

listings = parse_listing_file(file)

# kml_generator = KML('dinic', './')
# kml_generator.GenerateFromListings(listings)
