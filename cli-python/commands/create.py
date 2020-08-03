import click


@click.command()
@click.argument("Name", requeared = true)

def cli(Name):
    print("New Walet create " + Name)
