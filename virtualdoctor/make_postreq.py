import requests
import json

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data={'username':'shantanu4', 'phone':'8989101730', 'usertype':'Doctor',  'name':'baba','password':'dafa', 'repassword':'dafa', 'lat':20, 'lon':20, 'email':'GA'}

r=requests.post(url='http://localhost:8000/register/', headers=headers, data=json.dumps(data))

"""
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data={'username':'shantanu2', 'password':'dafa'}

r=requests.post(url='http://localhost:8000/login/', headers=headers, data=json.dumps(data))
"""
print r