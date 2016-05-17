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

    def delete(self, table_name, id_of_object_to_delete):
        url = "http://api.cloudboost.io/data/" + self.app_id + "/" + table_name
        payload = {
            "key": self.client_key,
            "document": {
                "_type": "custom",
                "_version": 0,
                "_id": id_of_object_to_delete,
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
                }
            },
            "method": "DELETE",
        }
        r = requests.put(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def index_for_search(self, table_name, column_name, column_value):
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
                         "_isModified": True,
                         "isSearchable": True
                         }
        }
        r = requests.put(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def query_equal_to(self, table_name, column_name, column_value):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/find"
        payload = {
            "key": self.client_key,
            "limit": 10,
            "sort": {
            },
            "select": {
            },
            "query": {
                "$includeList": [],
                "$include": [],
                column_name: column_value
            },
            "skip": 0
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def query_not_equal_to(self, table_name, value):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/find"
        payload = {
            "key": self.client_key,
            "limit": 10,
            "sort": {
            },
            "select": {
            },
            "query": {
                "$includeList": [],
                "$include": [],
                "name": {
                    "$ne": value
                }
            },
            "skip": 0
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def query_exists(self, table_name, column_name):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/find"
        payload = {
            "key": self.client_key,
            "sort": {
            },
            "select": {},
            "query": {
                "$includeList": [],
                "$include": [],
                column_name: {
                    "$exists": True
                }
            },
            "skip": 0
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def query_doesnot_exists(self, table_name, column_name):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/find"
        payload = {
            "key": self.client_key,
            "sort": {
            },
            "select": {},
            "query": {
                "$includeList": [],
                "$include": [],
                column_name: {
                    "$exists": False
                }
            },
            "skip": 0
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)


obj  = CloudApp("anuchdiujlug", "ff59f960-5982-479c-81dc-e3b1f7856a96")

response = obj.query_doesnot_exists("User", "username")
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
