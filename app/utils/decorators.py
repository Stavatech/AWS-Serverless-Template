import functools
import config


def lambda_handler(func):
    @functools.wraps(func)
    def wrapper(event, context):
        setattr(context, 'config', config)
        return func(event, context)
    return wrapper