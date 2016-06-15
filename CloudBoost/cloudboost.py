import requests
import ipdb
import json
import time


class CloudApp(object):

    def __init__(self, id, key):
        '''initialize with app id & key'''
        self.app_id = id
        self.client_key = key
        self.headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json'}
        self.document = {}
        print "Your CloudApp object", "with app id:", self.app_id

    # def __str__(self):
        # print "Your CloudApp object", "with app id", self.app_id
        # pass
    def serialize(self, response):
        self.document = response

# Use self to refer to instance variables and methods from other instance
# methods. Also put self as the first parameter in the definition of
# instance methods.

# A example:

# class MyClass(object):

#     my_var = None

#     def my_method(self, my_var):
#          self.my_var = my_var
#          self.my_other_method()

#     def my_other_method(self):
#          # do something...
