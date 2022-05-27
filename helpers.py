from bs4 import BeautifulSoup
import re
import requests
import base64
import click
from urllib.parse import urljoin


class AssesPage:
    def __init__(self, target, headers, filter_file):
        self.target = target
        self.headers = headers
        self.filter = filter_file
        self.code = {"script_urls": [], "js_code": []}
        self.crawl_page_for_javascript()

    def crawl_page_for_javascript(self):
        click.echo(
            f"Scanning target {click.style(self.target, fg='green')} for client side prototype pollution... \n\n"
        )
        try:
            page = requests.get(
                self.target, headers=self.headers if self.headers != None else ""
            )
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, "html.parser")
                for scripts in soup.findAll("script"):
                    if scripts.get("src") != None:
                        file_name = re.search("[^\/]*$", scripts.get("src"))
                        if file_name != None and file_name.group(0) not in self.filter:
                            self.code["script_urls"].append(
                                urljoin(self.target, scripts.get("src"))
                            )
                    else:
                        for i in scripts:
                            if i.string:
                                self.code["js_code"].append(
                                    base64.b64encode(i.string.encode("utf-8"))
                                )
            else:
                page.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Http Error:", e)
        except requests.exceptions.ConnectionError as ce:
            print("Error Connecting:", ce)

    def check_if_vulnerable(self):
        for file in self.code["script_urls"]:
            try:
                js = requests.get(
                    file, headers=self.headers if self.headers != None else ""
                )
                if js.status_code == 200:
                    click.echo(f"{click.style('Scanning file: ', fg='green')} {click.style(file, fg='yellow')} for prototype pollution...")
                    # code here to check if vulnerable
                else:
                    js.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print(f"Http Error: {click.style(file, fg='red')}", e)
            except requests.exceptions.ConnectionError as ce:
                print(f"Error Connecting to: {click.style(file, fg='red')}", ce)
    def check_for_pollution(self):
        print()
