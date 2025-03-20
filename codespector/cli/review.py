from .prepare import prepare
from .ai import aireview
from .report import save_report


def review(*args, **kwargs):
    prepared_data = prepare()
    review = aireview()
    report = save_report()
    return 1
