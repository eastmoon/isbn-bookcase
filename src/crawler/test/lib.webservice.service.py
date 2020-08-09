# coding=UTF-8
# Import configure
import conf
# Import library
from lib.webservice.service import Service
import inspect

class TestService(Service):
    @staticmethod
    def text():
        return {
            'type': 'get',
            'result': 'text',
            'url': 'https://jsonplaceholder.typicode.com/users/1',
        }
    @staticmethod
    def json(id):
        return {
            'type': 'get',
            'result': 'json',
            'url': "https://jsonplaceholder.typicode.com/todos/" + id,
        }

if __name__ == '__main__':
    print("> Service is a webservice tool for setting request information, It will integrate setting request method and ensure use apax to send request.")
    print(">>> Static method retrun request setting.")
    print(TestService.text())
    print(TestService.json("1"))
    print(">>> Instance object method will execute service and return promise object.")
    test = TestService()
    print(inspect.getmembers(test, inspect.isfunction))
    test.text().then(lambda res : print(res))
    test.json("1").then(lambda res : print(res))
    print("> END TEST")
