import click


@click.command()
@click.argument('deck-path', type=click.Path(exists=True))
def main(deck_path):
    pass
