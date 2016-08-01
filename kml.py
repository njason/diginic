from pykml.factory import KML_ElementMaker
from lxml import etree
from geopy.geocoders import GoogleV3
import time

from listing import Listing


class KML(object):
    __GEOCODES_PER_SECOND = 50

    def __init__(self, name, directory):
        self.KML = ''
        self.name = name
        self.save_directory = directory
        self.geolocater = GoogleV3()

    def GenerateFromListings(self, listings):
        self.KML = KML_ElementMaker.Folder()

        # we only have X amount of calls/sec and /day, so we need to throttle
        # ourselves
        geocode_count = 0

        for listing in listings:
            if geocode_count < KML.__GEOCODES_PER_SECOND:
                try:
                    location = self.geolocater.geocode(listing.address)

                    geocode_count += 1

                    self.KML.append(KML_ElementMaker.Placemark(
                        KML_ElementMaker.name(self.name),
                            KML_ElementMaker.description(listing.remarks),
                            KML_ElementMaker.Point(
                                KML_ElementMaker.coordinates(
                                    str(location.longitude) + ',' +
                                    str(location.latitude))
                            )
                        )
                    )
                except Exception as e:
                    # probably went over the Google geocode request limit
                    print 'Error encountered:'
                    print e
            else:
                print 'sleeping...'
                time.sleep(1)
                geocode_count = 0

        self.Save()

    def Save(self):
        with open(self.save_directory + 'FILE_TO_UPLOAD.kml', 'w') as saved_KML:
            saved_KML.write(etree.tostring(self.KML))

if __name__ == '__main__':
    kml = KML('Some TESTIN\' UPINDAPIECE', './')
    kml.GenerateFromListings([Listing])
