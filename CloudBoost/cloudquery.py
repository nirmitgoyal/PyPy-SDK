from cloudboost import *


class CloudQuery(CloudApp):

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
        self.serialize(r.json())
        return self  # return CloudQuery

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
        self.serialize(r.json())
        return self  # return CloudQuery

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
        self.serialize(r.json())
        return self  # return CloudQuery

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
        self.serialize(r.json())
        return self  # return CloudQuery

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
        self.serialize(r.json())
        return self  # return CloudQuery

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
        self.serialize(r.json())
        return self  # return CloudQuery

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
        self.serialize(r.json())
        return self  # return CloudQuery

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
        self.serialize(r.json())
        return self  # return CloudQuery
