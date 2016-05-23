import sys
import ipdb
import os
#INCLUDE IN INSTALLATION SETUP.PY
a = os.getcwd() 
pat = '/'.join(a.split('/')[:-1])
sys.path.append(pat)

from CloudBoost.cloudquery import CloudQuery

obj = CloudQuery("anuchdiujlug", "ff59f960-5982-479c-81dc-e3b1f7856a96")
print obj
print
response = obj.query_equal_to("User", "a1", "hello")
print response
# ipdb.set_trace()
print response.document[0]['ACL']
print response.document[0]['_id']
print response.document[0]['updatedAt']

		
