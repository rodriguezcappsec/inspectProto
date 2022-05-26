from bs4 import BeautifulSoup
import re
import requests
import base64
import click


@click.command()
@click.option("--url", help="URL to be scanned for client side prototype pollution")
@click.option("--headers", help="Any header neaded for the request to be successful")
def getJavaScript(url, headers):
    page = requests.get(url, headers=headers if headers != None else "")
    if page:
        soup = BeautifulSoup(page.text, "lxml")
        links = {"scripts": [], "links": [], "code": []}
        for scripts, _links in zip(soup.findAll("script"), soup.findAll("link")):
            if scripts.get("src") != None:
                links["scripts"].append(scripts.get("src"))
            else:
                links["code"].append(
                    base64.b64encode(str(scripts.string).encode("ascii"))
                )
            if re.match(".*\.js", _links.get("href")):
                links["links"].append(_links.get("href"))
        print(links)
        return links


getJavaScript()
