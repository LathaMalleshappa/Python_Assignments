import requests
import json

url = "http://localhost:8000/post_display/"
resp = requests.post(url,json={'cust_name':"Arav",'cust_address':"New York",'cust_dept':"Security"})
print(resp.json(),resp.status_code)

url = "http://localhost:8000/get_display/1"
resp=requests.put(url,data={'cust_address':'Pleasanton'})
print(resp.json())

resp=requests.delete(url)
print(resp.json())

resp=requests.get(url)
print(resp.json())

