import requests
print("requests version:", requests.__version__)
# https://requests.readthedocs.io/en/master/
print("GET http://www.google.com:", requests.get('http://www.google.com'))
print(requests.get('https://raw.githubusercontent.com/hughbagan/CMPUT404Wi21-lab1/master/lab1.py').text)
