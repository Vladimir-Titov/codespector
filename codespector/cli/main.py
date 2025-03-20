from .review import review


async def start(*args, **kwargs):
    print('in start')
    return await review(*args, **kwargs)
