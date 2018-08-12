import urllib2
import time
import json
import datetime
import subprocess
import sys
import logging

class processOpenFalcon():

    def sentToOpenFalcon(self,url,endpoint,metric,timestamp,step,value,counterType,tags=''):


        for x in range(5):
            ts = int(time.time())
            payload = [
                {
                    "endpoint":endpoint ,
                    "metric": metric,
                    "timestamp": timestamp,
                    "step": step,
                    "value": value,
                    "counterType": counterType,
                    "tags": "",
                }
            ]

            data=json.dumps(payload)


            req=urllib2.Request(url,data)
            response=urllib2.urlopen(req)
            time.sleep(2)