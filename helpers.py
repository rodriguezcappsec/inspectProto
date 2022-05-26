from bs4 import BeautifulSoup
import re
import requests
import base64
import click

def get_javascript(target, headers):
    click.echo(
        f"Scanning target {click.style(target, fg='green')} for client side prototype pollution..."
    )
    try:
        links = {"scripts": [], "links": [], "code": []}
        page = requests.get(target, headers=headers if headers != None else "")
        if page.status_code == 200:
            soup = BeautifulSoup(page.text, "lxml")
            for scripts, _links in zip(soup.findAll("script"), soup.findAll("link")):
                if scripts.get("src") != None:
                    links["scripts"].append(scripts.get("src"))
                else:
                    links["code"].append(
                        base64.b64encode(str(scripts.string).encode("ascii"))
                    )
                if re.match(".*\.js", _links.get("href")):
                    links["links"].append(_links.get("href"))
        else:
            print(f"there was an problem accessing the website {page.status_code}")
        page.raise_for_status()
        return links
    except requests.exceptions.HTTPError as e:
        print("Http Error:", e)
    except requests.exceptions.ConnectionError as ce:
        print("Error Connecting:", ce)