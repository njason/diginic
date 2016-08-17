#!/usr/bin/env python

import argparse

from parse import parse_listing_file
from kml import KML

parser = argparse.ArgumentParser()
parser.add_argument('file')

params = parser.parse_args()
file = open(params.file)

listings = parse_listing_file(file)
listings.sort(key=lambda x: x.sale_price)

kml_generator = KML()
kml_generator.generate_from_listings(listings)
