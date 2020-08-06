# Asynchronous Python and XML

# import package
from http.cookiejar import CookieJar
import requests

# declare class
class Apax:
    # common variable
    commonURL = ''
    commonCookies = None
    commonHeaders = None
    # class constructor
    #@staticmethod
    def common(self, info):
        # retrieve common url
        if 'url' in info:
            self.commonURL = info['url']

        # retrieve common cookies
        self.commonCookies = None
        if 'cookies' in info:
            self.commonCookies = info['cookies']

        # retrieve common headers
        self.commonHeaders = None
        if 'headers' in info:
            self.commonHeaders = info['headers']

    # class method
    #@staticmethod
    def execute(self, info):
        # create cookies controller object
        cookiesJar = CookieJar()
        #   result = requests.get(info['url'], cookies=info['cookies'], headers=info['headers'], params=info['params'], data=info['data'])
        # retrieve url
        requestURL = ''
        if 'url' in info:
            requestURL = self.commonURL + info['url']
        # retrieve request type : GET, POST, PUT, DELETE, etc.
        requestType = None
        if 'type' in info:
            requestType = info['type']

        # retrieve result type : text, json
        requestResult = None
        if 'result' in info:
            requestResult = info['result']

        # retrieve data
        requestCookies = {}
        if 'cookies' in info:
            requestCookies = info['cookies']
        if self.commonCookies != None:
            requestCookies.update(self.commonCookies)

        # retrieve headers
        requestHeaders = {}
        if 'headers' in info:
            requestHeaders = info['headers']
        if self.commonHeaders != None:
            requestHeaders.update(self.commonHeaders)

        # [GET Only] retrieve params
        requestParams = {}
        if 'params' in info:
            requestParams = info['params']

        # [POST, PUT] retrieve data
        requestData = {}
        if 'data' in info:
            requestData = info['data']

        # Execute asynchronous connection with requests tools.
        result = None
        if requestType == None:
            raise Exception('Request type can not empty.')
        if requestType == 'get':
            result = requests.get(requestURL, cookies=requestCookies, headers=requestHeaders, params=requestParams)
        if requestType == 'post':
            result = requests.post(requestURL, cookies=requestCookies, headers=requestHeaders, data=requestData)

        # Return result by difference data structure.
        if requestResult == 'json':
            return result.json()
        elif requestResult == 'text':
            return result.text
        else:
            return result
