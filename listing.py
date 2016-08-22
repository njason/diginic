from datetime import date
from money import Money


class Listing(object):
    def __init__(self, sample=False):
        if sample:
            self.mls = '71933254'
            self.address = '32 Sciarappa St U:1 Cambridge, MA:East Cambridge \
            02141'
            self.style = 'Condo - Low-Rise'
            self.rooms = 2
            self.garage = 0
            self.remarks = 'Beautiful Snug Smart Studio a 4 minute walk to ' +\
                'Lechmere T station, 2 minutes to Bus line to Harvard &' +\
                'Tufts and just a few blocks to the Tech Hub & Kendall ' +\
                'square. This 2-room smart plan with plenty of natural ' +\
                'light allows a renovated kitchen with handsome tall ' +\
                'Cherry cabinets, Stainless Steel appliances, black ' +\
                'granite counter and breakfast bar, as well as a living ' +\
                'space with built-ins closets, Murphy Bed and book ' +\
                'shelves. Wood floorings & recessed lightings. Tiled ' +\
                'bathroom with tub and window. 3 closets in unit & big ' +\
                'private storage room in basement. A wonderful ' +\
                'opportunity for a City pied-a-terre, investment or ' +\
                'first home (pay less than rent). It feels larger than ' +\
                'the square footage indicates with a phenomenal use of ' +\
                'the space.'
            self.status = 'SLD'
            self.beds = 0
            self.parking = 0
            self.dom = 29
            self.dto = 18
            self.price_sqft_list = Money('891.92', 'USD')
            self.price_sqft_sold = Money('841.75', 'USD')
            self.baths = '1f 0h'
            self.pets = '--'
            self.sale_price = Money('250000', 'USD')
            self.sale_date = date(2016, 1, 27)
            self.off_mkt_date = date(2015, 12, 15)
            self.outdoor_space = 'No'
            self.living_area = 297
            self.year_built = 1900
            self.list_price = Money('264900', 'USD')
            self.list_date = date(2015, 11, 16)
            self.orig_price = Money('264900', 'USD')
            self.assoc_fee = Money('107.90', 'USD')
            self.tax = Money('1251.98', 'USD')
            self.fy = 15
        else:
            self.mls = None
            self.address = None
            self.style = None
            self.rooms = None
            self.garage = None
            self.remarks = None
            self.status = None
            self.beds = None
            self.parking = None
            self.dom = None
            self.dto = None
            self.price_sqft_list = None
            self.price_sqft_sold = None
            self.baths = None
            self.pets = None
            self.sale_price = None
            self.sale_date = None
            self.off_mkt_date = None
            self.outdoor_space = None
            self.living_area = None
            self.year_built = None
            self.list_price = None
            self.list_date = None
            self.orig_price = None
            self.assoc_fee = None
            self.tax = None
            self.fy = None

    def to_kml_description(self):
        return 'Time: ' + 'DOM: ' + str(self.dom) + ', DTO: ' +\
                str(self.dto) + '\n' + 'Sale Price: ' +\
                self.sale_price.format('en_US') + '\n' +\
                'Sale Date: ' + str(self.sale_date) + '\n' + 'Address: ' +\
                self.address + '\n' + u'Sqft: ' +\
                str(round(self.sale_price.amount /
                          self.price_sqft_sold.amount)) + '\n' +\
                'Type: ' + self.style + '\n' + '$/Sqft: list - ' +\
                self.price_sqft_list.format('en_US') + ', sold - ' +\
                self.price_sqft_sold.format('en_US') + '\n' +\
                'Year Built: ' + str(self.year_built) + '\n' +\
                'Parking: ' + str(self.parking) + '\n' + 'Garage: ' +\
                str(self.garage) + '\n\n' + unicode(self.remarks)
