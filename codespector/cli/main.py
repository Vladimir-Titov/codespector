from .review import review


def start(*args, **kwargs):
    print('in start')
    return review(*args, **kwargs)
