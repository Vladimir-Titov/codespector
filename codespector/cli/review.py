from .prepare import prepare
from .ai import send_to_review
from .report import save_report


def review(*args, **kwargs):
    diff_filename = prepare(*args, **kwargs)
    review = send_to_review(diff_filename)
    report = save_report()
    return 1
