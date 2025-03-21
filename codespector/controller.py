from enum import Enum
from typing import Self
from codespector import cli


class CodeSpectorController:
    __slots__ = ('mode', 'chat_token', 'debug', 'chat_model')

    def __init__(self, mode: str, chat_token: str, debug: bool, chat_model: str):
        self.mode = mode
        self.chat_token = chat_token
        self.debug = debug
        self.chat_model = chat_model

    @classmethod
    def create(
        cls,
        mode: str,
        chat_token: str,
        debug: bool,
        chat_model: str,
    ) -> 'Self':
        return cls(mode=mode, chat_token=chat_token, debug=debug, chat_model=chat_model)

    def start(self):
        if self.mode == 'cli':
            codespector = cli.CLICodespector(chat_token=self.chat_token, debug=self.debug, chat_model=self.chat_model)
            codespector.review()
        return
