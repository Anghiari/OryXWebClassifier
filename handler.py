'''
Created on Oct 31, 2013

@author: Dell
'''
import httplib
from urlparse import urlparse
import time
import utils

def checkUrl(url):
    try:
        p = urlparse(url)
        conn = httplib.HTTPConnection(p.netloc)
        conn.request('HEAD', p.path)
        resp = conn.getresponse()
        return resp.status < 400
    except:
        return False
    
def getType(type):
    if type =="forum":
        return "Forum"
    if type == "orgsite":
        return "Org page"
    if type == "Blogs":
        return "Blog"
    else:
        return type
    