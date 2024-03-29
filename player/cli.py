import pkg_resources
import rich_click as click
from rich.table import Table
from rich.console import Console

from player import core


click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True

@click.group()
@click.version_option(pkg_resources.get_distribution("player").version)
def main():
    """\
        CLI game player rewards
    """

@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Help do comando

    """

    table = Table(title="Players Rewards")
    headers = ["name", "category", "role", "email"]
    results = core.load(filepath)

    for header in headers:
        table.add_column(header, style="magenta")


    for person in results:
        table.add_row(*[
            field.strip() for field in person.split(",")
        ])

    console = Console()
    console.print(table)
