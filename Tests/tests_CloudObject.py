import sys
import os
#INCLUDE IN INSTALLATION SETUP.PY
a = os.getcwd() 
pat = '/'.join(a.split('/')[:-1])
sys.path.append(pat)

from CloudBoost.cloudobject import CloudObject

obj = CloudObject("anuchdiujlug", "ff59f960-5982-479c-81dc-e3b1f7856a96")
print obj
print
response = obj.save("User", "a1", "nice")
print response
# ipdb.set_trace()
print response.document['ACL']
print response.document['_id']
print response.document['expires']

		
