# -*- coding: utf-8 -*-
def between(s, leader, trailer):
    #pure python way to find strings between two strings
    #used to find values of key value pairs in response without regex for small footprint and possible micropython adaption
    end_of_leader = s.index(leader) + len(leader)
    start_of_trailer = s.index(trailer, end_of_leader)
    return s[end_of_leader:start_of_trailer]

class Item:
    """Represents item in responses from api with all it's properties"""
    def __init__(self, itemString):
        self.content = itemString
        self.name= self.findValue("name")
        self.detailname= self.findValue("detailname")
        self.vendor= self.findValue("vendor")
        self.maincat= self.findValueArr("maincat")
        self.subcat= self.findValueArr("subcat")
        self.descr= self.findValue("descr")
        self.origin= self.findValue("origin")
        self.validated= self.findValue("validated")

        #TODO understand contents,pack flags thing
        # contents=
        # pack=

        del self.content

    def findValue(self, varName):
        substring1 = varName + "="
        substring2 = "\n"

        try:
            value = between(self.content,substring1,substring2)
            if len(value.strip()) == 0:
                value = None
            return value
        except ValueError:
            return None

    def findValueArr(self, varName):
        valueStr = self.findValue(varName)
        if valueStr != None:
            return valueStr.split(",")
        return None