import urllib.request
import codecs

def findJS(url):
    url = str(url)
    try:
        valid = urllib.request.urlopen(url)
    except:
        return "error, invalid url"
    try:
        temp = urllib.request.urlopen(url).read().decode("utf-8")
        if("<script>" in temp):
            return "it has js"
        return "no js"
    except:
        return "weird charSet"
