# OpenEAN
Library to use the api of the Open EAN/GTIN Database

serves as API wrapper for the api of [this EAN/GTIN database service](https://opengtindb.org/)

## Getting started
Install the library from pypi via `pip install openean`

Then you need an user_id for the service; [more info how you get that](https://opengtindb.org/userid.php)

There is also an id for small tests: "400000000" as described here https://opengtindb.org/faq.php#g

```python
from openean.OpenEAN import OpenEAN


userID = 400000000  #user your own id here

openean = OpenEAN(userID)

barcode_num = 1111 #barcode number of you product

items = openean.parse(barcode_num)
#items is a list of possible products associated with the code
# the properties of each item are described here https://opengtindb.org/api.php

#only to show you structure of working results
#not needed for use
from pprint import pprint
for item in items:
    pprint(vars(item))
```

## Thanks to
The creators of the API for making this possible and please consider donating to ["Kueste gegen Plastik"](https://www.kueste-gegen-plastik.de/unterstuetzen/) if you like this service to help the creators of the database running it.