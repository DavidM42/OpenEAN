# -*- coding: utf-8 -*-
import requests
from RequestStatus import RequestStatus
from Item import Item

base_url = "http://opengtindb.org/?cmd=query"

class OpenEAN:
    def __init__(self, userID):
        self.userID = userID
    
    def request(self, ean):
        """only does request and returns raw text response doesn't check anything like error code in content"""

        url = base_url + "&queryid=" + self.userID + "&ean=" + ean
        r = requests.get(url)

        content = r.content
        #don't know if needed or correct but solves misprinted chars in output
        content = content.decode("latin-1")

        return content

    def query(self, ean):
        """does request and checks errorcode then returns content as string"""
        status = RequestStatus()

        content = self.request(ean)

        errorafter = content.split("error=")
        if len(errorafter) == 2:
            try:
                errorCodeString = errorafter[1].split("\n")[0]
                errorCode = int(errorCodeString)

                #checks for errors and raises exceptions
                status.checkStatus(errorCode)                
                return content
            except ValueError as verr:
                #TODO error raisen
                print(verr)

        else:
            #TODO raise error if there is no errorCode in response?
            pass

    def parse(self, ean):
        """checks errorCode,parses response and returns array of possible items sorted after relevance"""
        content = self.query(ean)

        blocks = content.split("---\n")

        if len(blocks) > 1:
            #removes error code block
            blocks.pop(0)
            
            items = []
            for block in blocks:
                if len(block.strip()) > 0:
                    item = Item(block)
                    items.append(item)
            return items
        else:
            #TODO no item found feedback maybe other than None?
            return None

    def getMostRelevant(self,ean):
        """returns most relevant item found by api or None"""
        items = self.parse(ean)
        return items[0]