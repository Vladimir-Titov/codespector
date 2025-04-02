from codespector.prepare.local import CodeSpectorDataPreparer
from codespector.reviewer import CodeSpectorReviewer
from .errors import NotValidCfgError


class CodeSpector:
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

        self.data_preparer = CodeSpectorDataPreparer(
            output_dir=self.output_dir,
            compare_branch=self.compare_branch,
            request_link=self.request_link,
            git_token=self.git_token,
        )
        self.reviewer = CodeSpectorReviewer(
            diff_file=self.data_preparer.combined_file,
            chat_token=self.chat_token,
            chat_agent=self.chat_agent,
            system_content=self.system_content,
            output_dir=self.output_dir,
            chat_model=self.chat_model,
        )
        self.pipeline = [self.data_preparer, self.reviewer]

    def initialize(self):
        if self.request_link is not None and self.git_token is None:
            raise NotValidCfgError('git_token required if request link passed')

        elif self.request_link is None and self.compare_branch is None:
            raise NotValidCfgError('compare_branch required for local diff')

        if self.prompt_content is None:
            pass  # todo set default prompt content

        if self.system_content is None:
            pass  # todo set default system content

    def review(self):
        for pipe in self.pipeline:
            pipe.start()
