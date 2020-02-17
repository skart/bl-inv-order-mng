from rauth import OAuth1Service
from bl_web import app
from bl_web.config import *
import urllib
import json

class ApiClient:
    def __init__(self):
        self.service = OAuth1Service(name='bricklink',
                                     consumer_key=CONSUMER_KEY,
                                     consumer_secret=CONSUMER_SECRET,
                                     base_url='https://api.bricklink.com/api/store/v1/')
        self.session = self.service.get_session((ACCESS_TOKEN, ACCESS_TOKEN_SECRET))

    def request(self, method, url, params):
        if method in ('POST', 'PUT', 'DELETE'):
            response = self.session.request(method, url, True, '', data=json.dumps(params), headers={'Content-Type': 'application/json'}).json()
        else:
            response = self.session.request(method, url, True, '', params=params).json()
        app.logger.info("REQUEST " + str(method) + ": " +str(url) + " : " + str(params))
        app.logger.info("RESPONSE: " + str(response))
        return response

    def get(self, url, params={}):
        return self.request('GET', url, params)

    def post(self, url, params={}):
        return self.request('POST', url, params)

    def put(self, url, params={}):
        return self.request('PUT', url, params)

    def delete(self, url, params={}):
        return self.request('DELETE', url, params)