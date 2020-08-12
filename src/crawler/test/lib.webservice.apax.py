# coding=UTF-8
# Import configure
import conf
# Import library
from lib.webservice.apax import Apax

if __name__ == '__main__':
    print("> Apax is a webservice tool for retrieve web page text or retrieve webAPI json data.")
    apax = Apax()
    try:
        result = apax.execute({
            "type": "get",
            "result": "text",
            "url": "https://jsonplaceholder.typicode.com/users/1"
        })
        print(">>> APAX result 1")
        print(result)
    except ConnectionError as e:
        print(">>> APAX error : ", e, sep="\n")

    try:
        result = apax.execute({
            "type": "get",
            "result": "text",
            "url": "https://jsonplaceholder.test.typicode.com/users/1"
        })
        print(">>> APAX result")
        print(result)
    except ConnectionError as e:
        print(">>> APAX error : ", e, sep="\n")
    print("> END TEST")
