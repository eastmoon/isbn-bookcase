# coding=UTF-8
# Import configure
import conf
# Import library
from lib.webservice.apax import Apax

if __name__ == '__main__':
    print("Apax test")
    apax = Apax()
    try:
        result = apax.execute({
            "type": "get",
            "result": "text",
            "url": "https://github.com/eastmoon/isbn_bookcase/blob/master/README.md"
        })
        print(">>> APAX result")
        print(result)
    except ConnectionError as e:
        print(">>> APAX error : ", e, sep="\n")
    print("Next step")
