import sys
import os
#INCLUDE IN INSTALLATION SETUP.PY
a = os.getcwd() 
pat = '/'.join(a.split('/')[:-1])
sys.path.append(pat)

from CloudBoost.cloudACL import CloudACL

obj = CloudACL("anuchdiujlug", "ff59f960-5982-479c-81dc-e3b1f7856a96")
print obj
print
response = obj.ACL_setPublicWriteAccess("User", "a1", False)
print response
response = obj.ACL_setPublicWriteAccess("User", "a2", True)
print response


