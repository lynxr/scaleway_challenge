"""
We want to write in log for all errors
We want to send a sentry only when remote access failed
"""

from challenge.first.debug_service import sentry, log
from .errors import RemoteAccess


def do_something():
    """
    Noop function
    :return:
    """
    print('doing something cool')


def automate():
    """
    This automate is calling a function do_something that throw several types of errors:
    - RemoteAccessError
    - AuthorizationError
    """
    try:
        do_something()
    except Exception as e:
        log(e)
        if isinstance(e, RemoteAccess):
            sentry(e)


if __name__ == "__main__":
    automate()
