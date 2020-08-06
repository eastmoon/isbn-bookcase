# coding=UTF-8
# Import configure
import conf
# Import library
from lib.webservice.apax import Apax

if __name__ == '__main__':
    print("Apax test")
    apax = Apax()
    result = apax.execute({
        "type": "get",
        "url": "https://github.com/eastmoon/isbn_bookcase/blob/master/README.md"
    })
    print(result)
