import requests
import json


def do(method,data={},id=10,is_json=True):
    if is_json:
        data = json.dumps(data)
    r = requests.request(method,http+"?id="+str(id),data=data)
    print(r.text)
    return r