import urllib

import requests

BASE_URL = 'https://customcomplication.mikelyons.org/complicated/set/'

class COMPLICATION_TYPES():
    MODULAR_SMALL = 'modularSmall'
    MODULAR_LARGE = 'modularLarge'
    UTILITARIAN_SMALL = 'utilitarianSmall'
    UTILITARIAN_LARGE = 'utilitarianLarge'
    CIRCULAR_SMALL = 'circularSmall'
    EXTRA_LARGE = 'extraLarge'
    GRAPHIC_CORNER = 'graphicCorner'
    GRAPHIC_RECTANGULAR = 'graphicRectangular'
    GRAPHIC_BEZEL = 'graphicBezel'

    @staticmethod
    def getValidComplciationTypes():
        keys = [ attr for attr in dir( COMPLICATION_TYPES ) if not callable( getattr( COMPLICATION_TYPES, attr ) ) and not attr.startswith( '__' ) ]
        return [ getattr( COMPLICATION_TYPES, key ) for key in keys ]

def changeComplication( api_key, complication_type, new_value ):
    encoded_value = urllib.urlencode( { 'value': new_value } )
    update_url = BASE_URL + api_key + '/' + complication_type + '?' + encoded_value
    requests.get( update_url )
