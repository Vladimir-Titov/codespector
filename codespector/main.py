from pathlib import Path

import click
from environs import Env

from .controller import CodeSpectorController

BASE_PATH = Path(__file__).parent.parent

env = Env()
env.read_env(path=str(BASE_PATH / '.env'))


@click.option(
    '--chat-model',
    type=click.Choice(['codestral', 'chatgpt'], case_sensitive=False),
    envvar='CHAT_MODEL',
    show_envvar=True,
    default='codestral',
    help='Choose the chat model to use',
)
@click.option(
    '--debug',
    is_flag=True,
    default=False,
    envvar='CODESPECTOR_DEBUG',
    show_envvar=True,
    help='If set debug, all tmp files will be save and show works log',
)
@click.option(
    '--chat-token',
    type=str,
    envvar='CHAT_TOKEN',
    show_envvar=True,
)
@click.option(
    '--mode',
    type=click.Choice(['cli', 'bot'], case_sensitive=False),
    default='cli',
    help='Choose the mode of the application',
)
@click.version_option(message='%(version)s')
@click.command()
def main(*args, **kwargs):
    click.echo('Hello World!')
    return start(*args, **kwargs)


def start(*args, **kwargs):
    codespector = CodeSpectorController.create(*args, **kwargs)
    return codespector.start()


if __name__ == '__main__':
    main()
