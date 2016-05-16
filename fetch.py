import requests
import json

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('http://httpbin.org/get', params=payload)
# r = requests.get('https://api.github.com/events')
# print r
# r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# print r.text
# print r.json(	)
# print r.json()

# r = requests.get('https://api.github.com/user', auth=('nirmitgoyal', 'q123456'))
# print r.status_code
# print r.headers['content-type']
# print json.loads(r.text)
# print r.json()

app_id = "anuchdiujlug"
client_key = "ff59f960-5982-479c-81dc-e3b1f7856a96"
table_name="User"
url="http://api.cloudboost.io/data/"+app_id+"/"+table_name+"/find"
id_of_object_to_fetch="6RU07TZv"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = {
    "key": client_key,
    "limit": 1,
    "sort": {
    },
    "select": {
    },
    "query": {
        "$includeList": [],
        "$include": [],
        "_id": id_of_object_to_fetch
    },
    "skip": 0,
}

r = requests.post(url, json=payload,headers=headers)
print r
print r.text