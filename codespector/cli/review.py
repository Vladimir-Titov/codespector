from .prepare import prepare
from .ai import aireview
from .report import save_report


async def review(*args, **kwargs):
    prepared_data = await prepare()
    review = await aireview()
    report = await save_report()
    return 1
