import json
import requests
import os

# path to API_KEY
home = os.path.expanduser("~")
path = home +'/.API_KEYS/machinist.json'
f = open(path)
json_data = json.load(f)

data = json_data['keys']
Authorization_str = 'Bearer'+ ' ' + data['API_KEY']

# make header
req_header = {
    'Content-Type': 'application/json',
    'Authorization': Authorization_str,
}

# make data
req_data = json.dumps(
{
  "agent": "Home",
  "metrics": [
    {
      "name": "temperature",
      "namespace": "Environment Sensor",
      "data_point": {
        "value": 30.6
      }
    }
  ]
})
# url
url_machinist = "https://gw.machinist.iij.jp/endpoint"

# post with header
req = requests.post(url_machinist, data=req_data, headers=req_header)

# print status
print("data posted." + " status:", req.status_code)
print("check status? 200->ok! 4**->bad!")