import click
from helpers import CrawlPage

banner = click.style(
    """
_________ _        _______  _______  _______  _______ _________   _______  _______  _______ _________ _______ 
\__   __/( (    /|(  ____ \(  ____ )(  ____ \(  ____ \\__   __/  (  ____ )(  ____ )(  ___  )\__   __/(  ___  )
   ) (   |  \  ( || (    \/| (    )|| (    \/| (    \/   ) (     | (    )|| (    )|| (   ) |   ) (   | (   ) |
   | |   |   \ | || (_____ | (____)|| (__    | |         | |     | (____)|| (____)|| |   | |   | |   | |   | |
   | |   | (\ \) |(_____  )|  _____)|  __)   | |         | |     |  _____)|     __)| |   | |   | |   | |   | |
   | |   | | \   |      ) || (      | (      | |         | |     | (      | (\ (   | |   | |   | |   | |   | |
___) (___| )  \  |/\____) || )      | (____/\| (____/\   | |     | )      | ) \ \__| (___) |   | |   | (___) |
\_______/|/    )_)\_______)|/       (_______/(_______/   )_(     |/       |/   \__/(_______)   )_(   (_______)
                                                                                                              
""",
    fg="red",
    bold=True,
)


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
    click.echo(banner)
    crawler = CrawlPage(target, headers)
    page = crawler.crawl_page_for_javascript()
    print(page)


if __name__ == "__main__":
    inspect_proto()
