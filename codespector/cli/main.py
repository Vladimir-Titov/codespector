from .review import review


class CLICodespector:
    def __init__(self, chat_token: str, debug: bool, chat_model: str):
        self.chat_token = chat_token
        self.debug = debug
        self.chat_model = chat_model

    def review(self):
        review()
        return
