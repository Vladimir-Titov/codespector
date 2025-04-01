from pathlib import Path

import click
from environs import Env

from codespector.codespector import CodeSpector
from .controller import CodeSpectorController
from loguru import logger

BASE_PATH = Path(__file__).parent.parent

env = Env()
env.read_env(path=str(BASE_PATH / '.env'))


@click.option(
    '--git-token',
    type=str,
    help='Token for access git management system via api. Required if u use pass request_link',
    envvar='CODESPECTOR_GIT_ACCESS_TOKEN',
    show_envar=True,
)
@click.option(
    '--prompt-content',
    type=str,
    help='Prompt content which included to review prompt',
    envvar='CODESPECTOR_PROMPT_CONTENT',
    show_envvar=True,
)
@click.option(
    '--request-link',
    type=str,
    help='Link to the open pull or merge request',
)
@click.option(
    '--system-content',
    type=str,
    envvar='CODESPECTOR_SYSTEM_CONTENT',
    show_envvar=True,
    help='Content which used in system field for agent',
)
@click.option(
    '--output-dir',
    type=str,
    envvar='CODESPECTOR_OUTPUT_DIR',
    show_envvar=True,
    help='Select the output directory',
)
@click.option(
    '-b',
    '--compare-branch',
    type=str,
    help='Select the branch to compare the current one with',
)
@click.option(
    '--chat-agent',
    type=click.Choice(['codestral', 'chatgpt'], case_sensitive=False),
    envvar='CODESPECTOR_CHAT_AGENT',
    show_envvar=True,
    help='Choose the chat agent to use',
)
@click.option(
    '--chat-model',
    type=str,
    envvar='CODESPECTOR_CHAT_MODEL',
    show_envvar=True,
    help='Choose the chat model to use',
)
@click.option(
    '--chat-token',
    type=str,
    envvar='CODESPECTOR_CHAT_TOKEN',
    show_envvar=True,
)
@click.version_option(message='%(version)s')
@click.command()
def main(*args, **kwargs):
    return start(*args, **kwargs)


def start(*args, **kwargs):
    codespector = CodeSpector(*args, **kwargs)
    try:
        codespector.review()
    except Exception as e:
        logger.error('Error while review: {}', e)


if __name__ == '__main__':
    main()
