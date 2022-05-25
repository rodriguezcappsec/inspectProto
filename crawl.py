from bs4 import BeautifulSoup
import re
import requests
import sys
import esprima
import base64

page = requests.get(sys.argv[-1])
soup = BeautifulSoup(page.text, "lxml")


def getJavaScriptFiles():
    links = {"scripts": [], "links": [], "code": []}
    for scripts, _links in zip(soup.findAll("script"), soup.findAll("link")):
        if scripts.get("src") != None:
            links["scripts"].append(scripts.get("src"))
        else:
            links["code"].append(base64.b64encode(str(scripts.string).encode("ascii")))

        if re.match(".*\.js", _links.get("href")):
            links["links"].append(_links.get("href"))
    print(links)
    return links


getJavaScriptFiles()