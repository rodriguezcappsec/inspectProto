from bs4 import BeautifulSoup
import re
import requests
import base64
import click


class CrawlPage:
    def __init__(self, target, headers):
        self.target = target
        self.headers = headers

    def crawl_page_for_javascript(self):
        click.echo(
            f"Scanning target {click.style(self.target, fg='green')} for client side prototype pollution..."
        )
        try:
            links = {"scripts": [], "links": [], "code": []}
            page = requests.get(self.target, headers=self.headers if self.headers != None else "")
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, "lxml")
                for scripts, _links in zip(
                    soup.findAll("script"), soup.findAll("link")
                ):
                    if scripts.get("src") != None:
                        links["scripts"].append(scripts.get("src"))
                    else:
                        links["code"].append(
                            base64.b64encode(str(scripts.string).encode("ascii"))
                        )
                    if re.match(".*\.js", _links.get("href")):
                        links["links"].append(_links.get("href"))
            else:
                click.echo(
                    click.style(f"there was an problem accessing the website", fg="red")
                    + page.status_code
                )
            page.raise_for_status()
            return links
        except requests.exceptions.HTTPError as e:
            print("Http Error:", e)
        except requests.exceptions.ConnectionError as ce:
            print("Error Connecting:", ce)

    def get_javascript():
        print()
