import asyncio
from . import cli
import click


@click.command()
def main(*args, **kwargs):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start(*args, **kwargs))
    click.echo('Hello World!')


async def start(*args, **kwargs):
    await cli.start(*args, **kwargs)


if __name__ == '__main__':
    main()
