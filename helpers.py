from bs4 import BeautifulSoup
import re
import requests
import base64
import click
from urllib.parse import urlparse


class CrawlPage:
    def __init__(self, target, headers):
        self.target = target
        self.headers = headers
        print(urlparse(self.target))

    def crawl_page_for_javascript(self):
        click.echo(
            f"Scanning target {click.style(self.target, fg='green')} for client side prototype pollution... \n\n"
        )
        try:
            links = {"scripts": [], "code": []}
            page = requests.get(
                self.target, headers=self.headers if self.headers != None else ""
            )
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

    def format_paths(path):
        print()
