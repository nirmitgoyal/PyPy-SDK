from cloudboost import *


class CloudSearch(CloudApp):

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
        self.serialize(r.json())
        return self
        

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
        self.serialize(r.json())
        return self
        

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
        self.serialize(r.json())
        return self
        

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
        self.serialize(r.json())
        return self

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
        self.serialize(r.json())
        return self


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
        self.serialize(r.json())
        return self
        

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
        self.serialize(r.json())
        return self
        

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
        self.serialize(r.json())
        return self
        

    def set_limit(self, table_name, limit):
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

    def set_skip(self, table_name, skip):
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
        r = requests.post(url, data=json.dumps(payload), headers=self.headers)
        print r
        

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
        self.serialize(r.json())
        return self
        
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
        self.serialize(r.json())
        return self
        
