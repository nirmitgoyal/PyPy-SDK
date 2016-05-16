import requests
import json
import time


class CloudApp:
    app_id = None
    client_key = None
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json'}

    def __init__(self, id, key):
        '''initialize with app id & key'''
        self.app_id = id
        self.client_key = key
        # self.time = time.strftime("%c")
        print "Your CloudApp object", "with app id:", self.app_id

    def __str__(self):
        print "Your CloudApp object", "with app id", self.app_id

    def save(self, table_name, column_name, column_value):
        url = "http://api.cloudboost.io/data/" + self.app_id + "/" + table_name
        payload = {
            "key": self.client_key,
            "document": {"_type": "custom",
                         "expires": None,
                         column_name: column_value,
                         "_modifiedColumns": ["createdAt",
                                              "updatedAt",
                                              "ACL",
                                              "expires",
                                              column_name],
                         "_tableName": table_name,
                         "ACL": {
                             "write": {
                                 "allow": {
                                     "role": [],
                                     "user": ["all"]
                                 },
                                 "deny": {
                                     "role": [],
                                     "user": []
                                 }
                             },
                             "read": {
                                 "allow": {
                                     "role": [],
                                     "user": ["all"]
                                 },
                                 "deny": {
                                     "role": [],
                                     "user": []
                                 }
                             }
                         },
                         "_isModified": True}
        }
        # p=json.loads(payload)
        # print p
        r = requests.put(
            url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def fetch(self, table_name, id_of_object_to_fetch):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/find"
        payload = {
            "key": self.client_key,
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
        r = requests.post(
            url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def initTable(self, name):
        print "Table name %s" % name

    def find(self):
        ''''''
        pass


obj = CloudApp("anuchdiujlug", "ff59f960-5982-479c-81dc-e3b1f7856a96")

response=obj.fetch("User", "6RU07TZv")
print response
response=obj.save("User", "a1", "hello")
print response
response=obj.save("User", "a2", 100)
print response


# Use self to refer to instance variables and methods from other instance
# methods. Also put self as the first parameter in the definition of
# instance methods.

# A example:

# class MyClass(object):

#     my_var = None

#     def my_method(self, my_var):
#          self.my_var = my_var
#          self.my_other_method()

#     def my_other_method(self):
#          # do something...
