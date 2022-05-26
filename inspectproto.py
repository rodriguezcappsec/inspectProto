import click
from helpers import CrawlPage

@click.command()
@click.option(
    "--target",
    required=True,
    type=str,
    help="URL to be scanned for client side prototype pollution",
)
@click.option(
    "--headers",
    required=False,
    type=str,
    help="Any header neaded for the request to be successful",
)
def inspect_proto(target, headers):
    crawler = CrawlPage(target, headers)
    page = crawler.crawl_page_for_javascript()
    print(page)


if __name__ == "__main__":
    inspect_proto()
