import sys
import os

a = os.getcwd()
pat = '/'.join(a.split('/')[:-1])
sys.path.append(pat)
from CloudBoost import cloudboost

obj = cloudboost.CloudApp(
    "anuchdiujlug", "ff59f960-5982-479c-81dc-e3b1f7856a96")

response = obj.fetch("User", "6RU07TZv")
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
response = obj.query_get("User", "I7KWqKA1")
print response
response = obj.query_count("User", "a1", "hello")
print response
response = obj.query_distinct("User", "a1")
print response
response = obj.query_paginate("User", 1, 4)
print response
response = obj.search_search_on("User", "a1", "True")
print response
response = obj.search_equal_to("User", "a2", 200)
print response
response = obj.search_notequal_to("User", "a2", 200)
print response
response = obj.search_greater_than("User", "a2", 150)
print response
response = obj.search_less_than("User", "a2", 150)
print response
response = obj.search_or("User", "a2", 100, 2100)
print response
response = obj.search_order_by_asc("User", "a2")
print response
response = obj.search("User", "a2", 100)
print response
response = obj.role_getrole("CEO")
print response
