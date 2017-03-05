import urllib.request
import codecs

def findJS(url):
    url = str(url)
    try:
        temp = urllib.request.urlopen(url).read().decode("utf-8")
        if("<script>" in temp):
            print("It has js!")
        print("entered")
    except:
        print("error!")
