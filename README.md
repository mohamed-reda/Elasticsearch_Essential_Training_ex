#Running all tests:

the 4 main categories data types in elasticsearch:
---
1 core: text, numeric, boolean, Binary, and range

2 complex: array, object, nested array of JSON objects

3 Geo: geo_shape or geo_point data types for strong latitude and longitude

4 specialized: for handling things like IP addresses, auto-complete suggestions on a website, tokens as a string


---












-------------

cd tests

pytest


----
The -x flag: stop after first failure:

pytest -x

----
Run the test class TestRowToList :

pytest data/test_processing_helpers.py::TestRowToList

----
Run the unit test fun():

pytest data/test_preprocessing_helpers.py::TestRowToList::fun

----
Supports Python logical operators (run all in TestSplit but not fun):

pytest -k "TestSplit and not fun"

----

to run jupyter:

jupyter notebook

(Use Control-C to stop this server)
----
pip install -r requirements.txt

pip install notebook

python -m notebook

---
memory profile:

@memory_profiler.profile

python -m memory_profiler main.py

---

from line_profiler_pycharm import profile

@profile

python -m line_profiler main.py.lprof > results.txt

Elasticsearch endpoint

https://my-deployment-3f8516.es.us-central1.gcp.cloud.es.io

Created API key 'kibana02#'

(Copy this key now. You will not be able to view it again):

Base64

clI1SkZJY0JQdmpLNW84UWZmNTQ6aGtGZzlPci1SZ2kzQS0zbHRZdDB4UQ==

ZEdBcUZZY0JRNmJZaVluMXhGQUc6WUdNbXJHeFJRUldNZjFXRDJOSi1RUQ==

{"id":"dGAqFYcBQ6bYiYn1xFAG",
"name":"kibana",
"api_key":"YGMmrGxRQRWMf1WD2NJ-QQ","encoded":"ZEdBcUZZY0JRNmJZaVluMXhGQUc6WUdNbXJHeFJRUldNZjFXRDJOSi1RUQ=="}

{"id":"rx5AFYcBPvjK5o8QTP7V",
"name":"ApiKey",
"api_key":"9_QKBY_uTPu7Je8XNOcUbQ","encoded":"cng1QUZZY0JQdmpLNW84UVRQN1Y6OV9RS0JZX3VUUHU3SmU4WE5PY1ViUQ=="}

{"id":"gGCqFYcBQ6bYiYn1ZVBh",
"name":"api_key","api_key":"9ua0FghQSV2G2027L0aJSA",
"encoded":"Z0dDcUZZY0JRNmJZaVluMVpWQmg6OXVhMEZnaFFTVjJHMjAyN0wwYUpTQQ=="}