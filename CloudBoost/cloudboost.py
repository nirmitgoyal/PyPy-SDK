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
        # print "Your CloudApp object", "with app id", self.app_id

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

    def query_get(self, table_name, id):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/find"
        payload = {
            "key": self.client_key,
            "limit": 10,
            "sort": {
            },
            "select": {},
            "query": {
                "$includeList": [],
                "$include": [],
                "_id": id
            },
            "skip": 0
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def query_count(self, table_name, column_name, column_value):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/count"
        payload = {
            "key": self.client_key,
            "limit": 100,
            "sort": {
            },
            "select": {},
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

    def query_distinct(self, table_name, column_name):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/distinct"
        payload = {
            "key": self.client_key,
            "limit": 10,
            "sort": {
            },
            "select": {},
            "query": {
                "$includeList": [],
                "$include": [],
                column_name: None
            },
            "skip": 0
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def query_paginate(self, table_name, page_no, total_items_per_page):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/find"
        payload = {
            "key": self.client_key,
            "limit": total_items_per_page,
            "sort": {
            },
            "select": {
            },
            "query": {
                "$includeList": [],
                "$include": []
            },
            "skip": (page_no * total_items_per_page) - total_items_per_page
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def search_search_on(self, table_name, column_name, query):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/search"
        payload = {
            "key": self.client_key,
            "limit": 10,
            "sort": [],
            "query": {
                "filtered": {
                    "query": {
                        "bool": {
                            "must_not": [],
                            "should": [{
                                "match": {
                                    column_name: {
                                        "query": query
                                    }
                                }
                            }],
                            "must": []
                        }
                    },
                    "filter": {
                    }
                }
            },
            "skip": 0,
            "collectionName": table_name
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def search_equal_to(self, table_name, column_name, data):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/search"
        payload = {
            "key": self.client_key,
            "limit": 10,
            "sort": [],
            "query": {
                "filtered": {
                    "query": {
                    },
                    "filter": {
                        "bool": {
                            "must_not": [],
                            "should": [],
                            "must": [{
                                "term": {
                                    column_name: data
                                }
                            }]
                        }
                    }
                }
            },
            "skip": 0,
            "collectionName": table_name
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def search_notequal_to(self, table_name, column_name, data):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/search"
        payload = {
            "key": self.client_key,
            "limit": 10,
            "sort": [],
            "query": {
                "filtered": {
                    "query": {
                    },
                    "filter": {
                        "bool": {
                            "must_not": [{
                                "term": {
                                    column_name: data
                                }
                            }],
                            "should": [],
                            "must": []
                        }
                    }
                }
            },
            "skip": 0,
            "collectionName": table_name
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def search_greater_than(self, table_name, column_name, data):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/search"
        payload = {
            "key": self.client_key,
            "limit": 10,
            "sort": [],
            "query": {
                "filtered": {
                    "query": {
                    },
                    "filter": {
                        "bool": {
                            "must_not": [],
                            "should": [],
                            "must": [{
                                "range": {
                                    column_name: {
                                        "gt": data
                                    }
                                }
                            }]
                        }
                    }
                }
            },
            "skip": 0,
            "collectionName": table_name
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def search_less_than(self, table_name, column_name, data):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/search"
        payload = {
            "key": self.client_key,
            "limit": 10,
            "sort": [],
            "query": {
                "filtered": {
                    "query": {
                    },
                    "filter": {
                        "bool": {
                            "must_not": [],
                            "should": [],
                            "must": [{
                                "range": {
                                    column_name: {
                                        "lt": data
                                    }
                                }
                            }]
                        }
                    }
                }
            },
            "skip": 0,
            "collectionName": table_name
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def search_or(self, table_name, column_name, value1, value2):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/search"
        payload = {
            "key": self.client_key,
            "limit": 10,
            "sort": [],
            "query": {
                "filtered": {
                    "query": {
                    },
                    "filter": {
                        "bool": {
                            "must_not": [],
                            "should": [],
                            "must": [{
                                "term": {
                                    column_name: value1
                                }
                            },
                                {
                                "term": {
                                    column_name: value2
                                }
                            }]
                        }
                    }
                }
            },
            "skip": 0,
            "collectionName": table_name
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def search_order_by_asc(self, table_name, column_name):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/search"
        payload = {
            "key": self.client_key,
            "limit": 10,
            "sort": [{
                column_name: {
                    "order": "asc"
                }
            }],
            "query": {
                "filtered": {
                    "query": {
                    },
                    "filter": {
                    }
                }
            },
            "skip": 0,
            "collectionName": table_name
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def search_order_by_desc(self, table_name, column_name):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/search"
        payload = {
            "key": self.client_key,
            "limit": 10,
            "sort": [{
                column_name: {
                    "order": "desc"
                }
            }],
            "query": {
                "filtered": {
                    "query": {
                    },
                    "filter": {
                    }
                }
            },
            "skip": 0,
            "collectionName": table_name
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def search_set_limit(self, table_name, limit):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/search"
        payload = {
            "key": self.client_key,
            "limit": limit,
            "sort": [],
            "query": {
                "filtered": {
                    "query": {
                    },
                    "filter": {
                    }
                }
            },
            "skip": 0,
            "collectionName": table_name
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text

        def search_set_skip(self, table_name, skip):
            url = "http://api.cloudboost.io/data/" + \
                self.app_id + "/" + table_name + "/search"
            payload = {
                "key": self.client_key,
                "limit": 10,
                "sort": [],
                "query": {
                    "filtered": {
                        "query": {
                        },
                        "filter": {
                        }
                    }
                },
                "skip": skip,
                "collectionName": table_name
            }
            print r
            print r.text

        def search_exists(self, table_name, column_name):
            url = "http://api.cloudboost.io/data/" + \
                self.app_id + "/" + table_name + "/search"
            payload = {
                "key": self.client_key,
                "limit": 10,
                "sort": [],
                "query": {
                    "filtered": {
                        "query": {
                        },
                        "filter": {
                            "bool": {
                                "must_not": [],
                                "should": [],
                                "must": [{
                                    "exists": {
                                        "field": column_name
                                    }
                                }]
                            }
                        }
                    }
                },
                "skip": 0,
                "collectionName": table_name
            }
            r = requests.post(url, data=json.dumps(
                payload), headers=self.headers)
            print r
            print r.text
            return json.dumps(r.json(), sort_keys=True, indent=4)

    def search(self, table_name, column_name, query):
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/" + table_name + "/search"
        payload = {
            "key": self.client_key,
            "limit": 10,
            "sort": [],
            "query": {
                "filtered": {
                    "query": {
                        "bool": {
                            "must_not": [],
                            "should": [{
                                "match": {
                                    column_name: {
                                        "query": query
                                    }
                                }
                            }],
                            "must": []
                        }
                    },
                    "filter": {
                    }
                }
            },
            "skip": 0,
            "collectionName": table_name
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def user_add_to_role(self, role_name, username, id_of_row):
        url = "http://api.cloudboost.io/user/" + \
            self.app_id + "/addToRole"
        payload = {
            "key": self.client_key,
            "role": {"_type": "role",
                     "expires": None,
                     "name": role_name,
                     "_modifiedColumns": ["createdAt",
                                          "updatedAt",
                                          "ACL",
                                          "expires",
                                          "name"],
                     "_tableName": "Role",
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
                     "_isModified": True},
            "user": {
                "_type": "user",
                "_version": 0,
                "username": username,
                "expires": None,
                "_id": id_of_row,
                "_tableName": "User",
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
            }
        }

        r = requests.put(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)

    def role_getrole(self, role_name):
        '''get Role object'''
        url = "http://api.cloudboost.io/data/" + \
            self.app_id + "/Role/find"
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
                "name": role_name
            },
            "skip": 0
        }
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        print r.text
        return json.dumps(r.json(), sort_keys=True, indent=4)


obj = CloudApp("anuchdiujlug", "ff59f960-5982-479c-81dc-e3b1f7856a96")

response = obj.role_getrole("CEO")
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
