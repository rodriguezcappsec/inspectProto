from bs4 import BeautifulSoup
import re
import requests
import base64
import click
from urllib.parse import urljoin


class CrawlPage:
    def __init__(self, target, headers, filter_file):
        self.target = target
        self.headers = headers
        self.filter = filter_file

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
                soup = BeautifulSoup(page.text, "html.parser")
                for scripts in soup.findAll("script"):
                    if scripts.get("src") != None:
                        file_name = re.search("[^\/]*$", scripts.get("src"))
                        if file_name != None and file_name.group(0) not in self.filter:
                            links["scripts"].append(
                                urljoin(self.target, scripts.get("src"))
                            )
                    else:
                        for i in scripts:
                            if i.string:
                                links["code"].append(
                                    base64.b64encode(i.string.encode("utf-8"))
                                )
            else:
                page.raise_for_status()
            return links
        except requests.exceptions.HTTPError as e:
            print("Http Error:", e)
        except requests.exceptions.ConnectionError as ce:
            print("Error Connecting:", ce)

    def get_javascript():
        print()  # time to decode javascript and fetch javascript
