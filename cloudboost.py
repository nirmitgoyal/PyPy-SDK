import os
import time


class CloudApp :
    count = 0
    id=None
    # key=""
    time=""
    def __init__(self, id, key):
        '''initialize with app id & key'''
        self.id = id
        self.key = key
        self.time = time.strftime("%c")
        CloudApp.count += 1
        print "CloudApp object", CloudApp.count, "with id", self.id, "created on", self.time
        # print self.message
    def __str__(self):
        pass

        

    def initTable(self, name):
        print "Table name %s" % self.name

    def set(self):
        ''''''
        pass

    def find(self):
        ''''''
        pass

    def objectCount(self):
        print "Total CloudApp objects: %s" % CloudApp.count


obj1 = CloudApp(3452, "w4jhtkj4uEkrIt0")
obj2 = CloudApp(34332, "slkgufeLK599Eo4ka")
obj1.objectCount()
