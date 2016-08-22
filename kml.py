from pykml.factory import KML_ElementMaker
from lxml import etree
from geopy.geocoders import GoogleV3
from datetime import datetime
import time
import re
import unicodedata


class KML(object):
    GEOCODES_PER_SECOND = 15
    SLEEP_TIMEOUT = 1

    @staticmethod
    def slugify(value):
        '''
        Django's "slug" function, taken from SO

        Normalizes string, converts to lowercase, removes non-alpha characters,
        and converts spaces to hyphens.
        '''
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
        value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
        value = re.sub('[-\s]+', '-', value)
        return value

    def __init__(self, filename=None, test=False):

        if filename is None:
            filename = u'UPLOAD' + datetime.now().strftime('%Y%m%d%H%M%S')

        self.KML = ''
        self.name = filename
        self.save_location = './' + self.slugify(filename) + '.kml'
        self.TEST = test
        self.geolocater = GoogleV3()

    def generate_from_listings(self, listings):
        self.KML = KML_ElementMaker.Folder()

        # we only have X amount of calls/sec and /day, so we need to throttle
        # ourselves.
        geocode_count = 0
        listings_to_process = True
        geocode_failures = []
        failures = 0
        FAILURE_LIMIT = 1000  # stop trying after this many failures

        while listings_to_process:
            if len(geocode_failures) > 0:
                listings = geocode_failures
                geocode_failures = []

            for listing in listings:
                if geocode_count > KML.GEOCODES_PER_SECOND:
                    print 'sleeping...'
                    time.sleep(KML.SLEEP_TIMEOUT)
                    geocode_count = 0
                try:
                    if self.TEST:
                        location_str = '40.0, 40.0'
                    else:
                        location = self.geolocater.geocode(listing.address)
                        location_str = str(location.longitude) + ',' + \
                            str(location.latitude)

                    geocode_count += 1

                    self.KML.append(KML_ElementMaker.Placemark(
                        KML_ElementMaker.name(
                            listing.sale_price.format('en_US')),
                        KML_ElementMaker.description(
                                listing.to_kml_description()),
                        KML_ElementMaker.Point(
                                KML_ElementMaker.coordinates(location_str))
                    ))
                except Exception as e:
                    print 'Error encountered:'
                    print e

                    geocode_failures.append(listing)
                    failures += 1

                    if failures >= FAILURE_LIMIT:
                        listings_to_process = False
                        print 'Too many failed attempts to geolocate. ' + \
                            'Program will shut down without finishing.'

                        break

            if len(geocode_failures) == 0:
                listings_to_process = False

            self.save()

    def save(self):
        with open(self.save_location, 'w') as saved_KML:
            saved_KML.write(etree.tostring(self.KML))
