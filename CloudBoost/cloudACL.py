from cloudboost import *


class CloudACL(CloudApp):

    def ACL_setPublicWriteAccess(self, table_name, column_name, column_value):
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
                                              "name"],
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
        r = requests.put(url, data=json.dumps(payload), headers=self.headers)
        print r

    def ACL_setPublicReadAccess(self, table_name, column_name, column_value):
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
                                              "name"],
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
        r = requests.put(url, data=json.dumps(payload), headers=self.headers)
        print r
