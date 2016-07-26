#!/usr/bin/env python

import argparse
import re

from bs4 import BeautifulSoup

# really BS?
def iter_to_list(iter):
    list = []
    for i in iter:
        list.append(i)

    return list

def parse_node(node):
    chillen = node.children.next()
    in_ = node.children.next()
    da = node.children.next()
    club = node.children.next()
    bottle = node.children.next()
    full = node.children.next()
    of_bub = node.children.next()

    # first row
    chillen = iter_to_list(chillen)
    mlb = ''

parser = argparse.ArgumentParser()
parser.add_argument('file')

params = parser.parse_args()

soup = BeautifulSoup(open(params.file), 'html.parser')

the_piece = soup.findAll(text='MLS #:')

for chillin in the_piece:
    node = chillin.parent.parent.parent.parent
    parse_node(node)
