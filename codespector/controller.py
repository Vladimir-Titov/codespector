from codespector import local
from .errors import NotValidCfgError


class CodeSpectorController:
    def __init__(
        self,
        chat_token: str,
        chat_agent: str,
        compare_branch: str,
        output_dir: str,
        system_content: str,
        chat_model: str,
        request_link: str | None = None,
        prompt_content: str | None = None,
        git_token: str | None = None,
    ):
        self.chat_token = chat_token
        self.chat_agent = chat_agent
        self.compare_branch = compare_branch
        self.output_dir = output_dir
        self.system_content = system_content
        self.chat_model = chat_model
        self.request_link = request_link
        self.prompt_content = prompt_content
        self.git_token = git_token
        self.mode = None

    def initialize(self):
        if self.request_link is not None and self.git_token is None:
            raise NotValidCfgError('git token required if u pass request link')

        if self.request_link is not None:
            self.mode = 'diff_link'
        else:
            self.mode = 'local'

    def start(self):
        self.initialize()
        codespector = local.LocalCodespector(
            chat_token=self.chat_token,
            chat_agent=self.chat_agent,
            compare_branch=self.compare_branch,
            output_dir=self.output_dir,
            system_content=self.system_content,
            chat_model=self.chat_model,
        )
        codespector.review()
