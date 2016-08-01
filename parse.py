import re
from datetime import datetime
from money import Money

from bs4 import BeautifulSoup

from listing import Listing


def itol(iter):
    '''
    really BS? have to manually turn listiterator to list to use indexes?
    '''
    list = []
    for i in iter:
        list.append(i)
    return list


def parse_string(node, label):
    '''
    keep it DRY bro
    '''
    return node.getText().replace(label, '').strip()


def parse_int(node, label):
    return int(parse_string(node, label))


def parse_date(node):
    return datetime.strptime(node.find(text=re.compile(
        '\d{1,2}/\d{1,2}/\d{4}')).strip(), '%m/%d/%Y').date()


def parse_money(node, label):
    str = node.getText().replace(label + '$', '').replace(',', '')
    if str == '':
        return Money('0', 'USD')

    return Money(str, 'USD')


def parse_sqft(node):
    return float(node.find(text=re.compile('\d{1,}\.?\d{1,}?')).strip())


def parse_node(node):
    children = itol(node.children)

    listing = Listing()

    try:

        # first row
        chillen = itol(children[0])
        listing.mlb = chillen[0].find_all(text=re.compile('\d{8}'))[0].strip()
        listing.status = parse_string(chillen[1], 'Status: ')
        ginz = chillen[2].find_all(text=re.compile('\d*'))
        listing.dom = int(ginz[1].strip())
        listing.dto = int(ginz[3].strip())
        listing.sale_price = parse_money(chillen[3], 'Sale Price: ')
        listing.list_price = parse_money(chillen[4], 'List Price: ')

        # second row
        in_ = itol(children[1])
        address1 = in_[0].getText()
        listing.list_sqft = parse_sqft(in_[1])
        listing.sale_date = parse_date(in_[2])
        listing.list_date = parse_date(in_[3])

        # third row
        da = itol(children[3])
        address2 = da[0].getText()
        listing.address = address1 + ' ' + address2
        listing.sold_sqft = parse_sqft(da[1])
        listing.off_mkt_date = parse_date(da[2])
        listing.orig_price = parse_money(da[3], 'Orig. Price:  ')

        # fourth row
        club = itol(children[4])
        listing.style = parse_string(club[0], 'Style: ')
        listing.outdoor_space = parse_string(club[1], 'Outdoor Space: ')
        listing.assoc_fee = parse_money(club[2], 'Assoc.Fee: ')

        # fifth row
        bottle = itol(children[6])
        listing.rooms = parse_int(bottle[0], 'Rooms: ')
        listing.beds = parse_int(bottle[1], 'Beds: ')
        listing.baths = parse_string(bottle[2], 'Baths: ')
        listing.living_area = parse_int(bottle[3], 'Living Area: ')
        listing.tax = parse_money(bottle[4], 'Tax: ')

        # sixth row
        full = itol(children[8])
        listing.garage = parse_int(full[0], 'Garage: ')
        listing.parking = parse_int(full[1], 'Parking: ')
        listing.pets = parse_string(full[2], 'Pets: ')
        listing.year_built = parse_int(full[3], 'Year Built: ')
        listing.fy = parse_int(full[4], 'Fy: ')

        # seventh row
        of_bub = itol(children[10])
        listing.remarks = parse_string(of_bub[0], 'Remarks: ')
    except:
        pass

    return listing


def parse_listing_file(file):
    soup = BeautifulSoup(file, 'html.parser')

    the_piece = soup.findAll(text='MLS #:')

    listings = []

    for chillin in the_piece:
        node = chillin.parent.parent.parent.parent
        listings.append(parse_node(node))

    return listings
