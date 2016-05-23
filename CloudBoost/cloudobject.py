from cloudboost import *


class CloudObject(CloudApp):
    """docstring for  CloudObject"""

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
        r = requests.put(
            url, data=json.dumps(payload), headers=self.headers)
        print r
        self.serialize(r.json())
        return self  # return CloudObject

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
        self.serialize(r.json())
        return self  # return CloudObject

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
        self.serialize(r.json())
        return self  # return CloudObject

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
        self.serialize(r.json())
        return self  # return CloudObject
