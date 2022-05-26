import click
import helpers

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
    js = helpers.get_javascript(target, headers)
    print(js)


if __name__ == "__main__":
    inspect_proto()
