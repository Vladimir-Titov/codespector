from . import cli
import click


@click.command()
def main(*args, **kwargs):
    start(*args, **kwargs)
    click.echo('Hello World!')


def start(*args, **kwargs):
    cli.start(*args, **kwargs)


if __name__ == '__main__':
    main()
