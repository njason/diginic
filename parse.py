#!/usr/bin/env python

import argparse
import re
from datetime import date, datetime
from money import Money

from bs4 import BeautifulSoup

from listingsample import Listing


def itol(iter):
    '''
    really BS? have to manually turn listiterator to list to use indexes?
    '''
    list = []
    for i in iter:
        list.append(i)
    return list


def parse_string(node, label):
    return node.getText().replace(label, '').strip()


def parse_date(node):
    '''
    keep it DRY bro
    '''
    return datetime.strptime(node.find(text=re.compile(
        '\d{1,2}/\d{1,2}/\d{4}')).strip(), '%m/%d/%Y').date()


def parse_money(node, label):
    return Money(node.getText().replace(label + '$', '').replace(',', ''),
                 'USD')


def parse_sqft(node):
    return float(node.find(text=re.compile('\d{1,}\.\d{1,}')).strip())


def parse_node(node):
    children = itol(node.children)
    chillen = itol(children[0])
    in_ = itol(children[1])
    da = itol(children[3])
    club = itol(children[4])
    bottle = itol(children[4])
    full = itol(children[5])
    of_bub = itol(children[6])

    listing = Listing()

    # first row
    listing.mlb = chillen[0].find_all(text=re.compile('\d{8}'))[0].strip()
    listing.status = parse_string(chillen[1], 'Status: ')
    ginz = chillen[2].find_all(text=re.compile('\d*'))
    listing.dom = int(ginz[1].strip())
    listing.dto = int(ginz[3].strip())
    listing.sale_price = parse_money(chillen[3], 'Sale Price: ')
    listing.list_price = parse_money(chillen[4], 'List Price: ')

    # second row
    address1 = in_[0].getText()
    listing.list_sqft = parse_sqft(in_[1])
    listing.sale_date = parse_date(in_[2])
    listing.list_date = parse_date(in_[3])

    # third row
    address2 = da[0].getText()
    listing.address = address1 + ' ' + address2
    listing.sold_sqft = parse_sqft(da[1])
    listing.off_mkt_date = parse_date(da[2])
    listing.orig_price = parse_money(da[3], 'Orig. Price:  ')

    # fourth row
    listing.style = parse_string(club[0], 'Style: ')


parser = argparse.ArgumentParser()
parser.add_argument('file')

params = parser.parse_args()

soup = BeautifulSoup(open(params.file), 'html.parser')

the_piece = soup.findAll(text='MLS #:')

for chillin in the_piece:
    node = chillin.parent.parent.parent.parent
    parse_node(node)
