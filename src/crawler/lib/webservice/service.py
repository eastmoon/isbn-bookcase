# Service :
# It is a class which will create class function by static method, and class function will call static method to retrieve request body and send request by APAX.
# Every class function will return a promise class, and promise first will call APAX, and resolve or reject by APAX result.
#
# Reference :
# Python3: How to inspect a function’s type : https://medium.com/solomons-tech-stack/9999eeb31c0b

# import package
import inspect
from promise import Promise
# Import webservice package
from .apax import Apax

class Service:
    # class constructor
    def __init__(self):
        self.__apax = Apax()
        methods = self.__class__.__dict__
        for method_name in methods:
            if type(methods.get(method_name)) == staticmethod:
                if method_name == 'common':
                    # setting common info, if find a method name 'common'.
                    commonInfo = getattr(self.__class__, method_name)()
                    self.__apax.common(commonInfo)
                else:
                    # create and package method.
                    setattr(self, method_name, self.__buildMethod(method_name))


    # dynamic build method
    def __buildMethod(self, methodName):
        def executeMethod(*args):
            # defined method
            # method will execute an asynchronous connection with target web API.
            # it will return a promise object.
            def callService(resolve, reject):
                method = getattr(self.__class__, self.__methodName)
                try:
                    resolve(self.__apax.execute(method(*self.__methodArgs)))
                except Exception as inst:
                    reject(inst)

            # setting info
            self.__methodName = methodName
            self.__methodArgs = args
            return Promise(callService)
        return executeMethod
