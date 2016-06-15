from cloudboost import *


class CloudRole(CloudApp):

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
        self.serialize(r.json())
        return self  # return object of CloudRole
        
