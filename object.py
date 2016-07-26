from datetime import date

from money import Money

class Listing(object):
    mls = '71933254'
    address = '32 Sciarappa St U:1 Cambridge, MA:East Cambridge 02141'
    style = 'Condo - Low-Rise'
    rooms = 2
    garage = 0
    remarks = 'Beautiful Snug Smart Studio a 4 minute walk to Lechmere T station, 2 minutes to Bus line to Harvard & Tufts and just a few blocks to the Tech Hub & Kendall square. This 2-room smart plan with plenty of natural light allows a renovated kitchen with handsome tall Cherry cabinets, Stainless Steel appliances, black granite counter and breakfast bar, as well as a living space with built-ins closets, Murphy Bed and book shelves. Wood floorings & recessed lightings. Tiled bathroom with tub and window. 3 closets in unit & big private storage room in basement. A wonderful opportunity for a City pied-a-terre, investment or first home (pay less than rent). It feels larger than the square footage indicates with a phenomenal use of the space.'
    status = 'SLD'
    beds = 0
    parking = 0
    dom = 29
    dto = 18
    list_sqft = 891.92
    sold_sqft = 841.75
    baths = '1f 0h'
    pets = '--'
    sale_price = Money(amount='250000', 'USD')
    sale_date = date(2016, 1, 27)
    off_mkt_date = date(2015, 12, 15)
    outdoor_space = 'No'
    living_area = 297
    year_built = 1900
    list_price = Money(amount='264900', 'USD')
    list_date = date(2015, 11, 16)
    orig_price = Money('264900', 'USD')
    assoc_fee = Money('107.90', 'USD')
    tax = Money('1251.98', 'USD')
    fy = 15
