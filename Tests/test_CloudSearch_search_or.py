import sys
import os
import ipdb
#INCLUDE IN INSTALLATION SETUP.PY
a = os.getcwd() 
pat = '/'.join(a.split('/')[:-1])
sys.path.append(pat)

from CloudBoost.cloudsearch import CloudSearch

obj = CloudSearch("anuchdiujlug", "ff59f960-5982-479c-81dc-e3b1f7856a96")
print obj
print
response = obj.search_or("User", "a2", 100, 2100)
print response
print
# ipdb.set_trace()
print response.document