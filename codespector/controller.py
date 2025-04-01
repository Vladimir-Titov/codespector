from codespectors.local import LocalCodeSpector
from codespectors.git_link import GitLinkCodeSpector
from .errors import NotValidCfgError


class CodeSpectorController:
    def __init__(
        self,
        chat_token: str,
        chat_agent: str,
        chat_model: str,
        compare_branch: str | None = None,
        system_content: str | None = None,
        output_dir: str = 'codespector',
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
            raise NotValidCfgError('git_token required if request link passed')

        if self.request_link is not None:
            self.mode = 'diff_link'
        else:
            self.mode = 'local'

        if self.mode == 'local':
            if self.compare_branch is None:
                raise NotValidCfgError('compare_branch required for local mode')

        if self.prompt_content is None:
            pass # todo set default prompt content

        if self.system_content is None:
            pass # todo set default system content


    def start(self):
        self.initialize()
        if self.mode == 'local':
            codespector = LocalCodeSpector(
                chat_token=self.chat_token,
                chat_agent=self.chat_agent,
                compare_branch=self.compare_branch,
                output_dir=self.output_dir,
                system_content=self.system_content,
                chat_model=self.chat_model,
            )
        elif self.mode == 'git_link':
            codespector = GitLinkCodeSpector()
        else:
            raise NotValidCfgError('Not valid mode')

        codespector.review()
