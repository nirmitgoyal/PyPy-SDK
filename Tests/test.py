import sys
import os

a = os.getcwd()
pat = '/'.join(a.split('/')[:-1])
sys.path.append(pat)
from CloudBoost import cloudboost

obj = cloudboost.CloudApp(
    "anuchdiujlug", "ff59f960-5982-479c-81dc-e3b1f7856a96")

response = obj.fetch("User", "6RU07TZv" )
print response
response = obj.save("User", "a1", "hello")
print response
response = obj.save("User", "a2", 100)
print response
response = obj.delete("User", "")
print response
response = obj.index_for_search("User", "a1", "hello")
print response
response = obj.query_equal_to("User", "a1", "wow")
print response
response = obj.query_not_equal_to("User", "wow")
print response
response = obj.query_exists("User", "username")
print response
response = obj.query_doesnot_exists("User", "username")
print response
