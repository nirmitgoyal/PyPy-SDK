from cloudboost import *


class CloudUser(CloudApp):

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
        self.serialize(r.json())
        return self  # return object of CloudUser

    def user_remove_from_role(self, role_name, username, id_of_row):
        url = "http://api.cloudboost.io/user/" + \
            self.app_id + "/removeFromRole"
        payload = {
            {
                "role": {
                    "_type": "role",
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
                    "_isModified": True
                },
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
                    },
                    # "password": ${encrypted_password}
                },
                "key": self.client_key
            }
        }
        r = requests.put(url, data=json.dumps(payload), headers=self.headers)
        print r
        self.serialize(r.json())
        return self  # return object of CloudUser