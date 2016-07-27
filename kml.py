from pykml.factory import KML_ElementMaker
from lxml import etree
from geopy.geocoders import GoogleV3

from listingsample import Listing


class KML(object):

    def __init__(self, name, directory):
        self.KML = ''
        self.name = name
        self.save_directory = directory
        self.geolocater = GoogleV3()

    def GenerateFromListing(self, listing):
        location = self.geolocater.geocode(Listing.address)

        self.KML = KML_ElementMaker.Placemark(
            KML_ElementMaker.name(self.name),
                KML_ElementMaker.Point(
                    KML_ElementMaker.coordinates(str(location.longitude) + ',' +
                        str(location.latitude))
                )
            )

        self.Save()

    def Save(self):
        with open(self.save_directory + 'FILE_TO_UPLOAD.kml', 'w') as saved_KML:
            saved_KML.write(etree.tostring(self.KML))

if __name__ == '__main__':
    kml = KML('Some TESTIN\' UPINDAPIECE', './')
    kml.GenerateFromListing(Listing)
