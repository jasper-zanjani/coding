#!/usr/bin/python
import requests
import json

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

data = {
    "model": "mistral",
    "stream": False,
    "prompt": "Why is the sky blue?"
}

res = requests.post(url, headers=headers, data=json.dumps(data))

if res.status_code == 200:
    print(res.text)
else:
    print("Error:", res.status_code, res.text)
