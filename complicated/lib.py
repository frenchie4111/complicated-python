try:
    from urllib import urlencode
except Exception as e:
    from urllib.parse import urlencode

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

def changeComplication( api_key, complication_type, new_value, alert=None, push=None, push_changed=None ):
    """
    Updates given complication with new value

    params:
        api_key: your api key (ge in app)
        complication_type: The complication type to update
        new_value: The new value of the complication
        alert: optional string to send push notification with (only works when enabled in app)
        push: optional set true to notify with new value (only works when enabled in app)
        push_changed: optional set true to notify if value is different than previous (only works when enabled in app)
    """

    data = { 'value': new_value }
    
    if alert is not None:
        data['alert'] = alert
    if push is not None and push:
        data['push'] = 'true'
    if push_changed is not None and push_changed:
        data['push_changed'] = 'true'

    encoded_value = urlencode( data )
    print(encoded_value)
    update_url = BASE_URL + api_key + '/' + complication_type + '?' + encoded_value
    requests.get( update_url )
