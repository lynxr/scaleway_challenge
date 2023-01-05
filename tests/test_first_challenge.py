import contextlib
import unittest
from collections import namedtuple
from unittest import mock

from challenge.first.catching_error import automate
from challenge.first.errors import RemoteAccess, AuthorizationError

TestData = namedtuple('TestData', ['exc', 'is_sentry'])


@contextlib.contextmanager
def patch_script_functions(exc):
    """
    Patching function for test proposes
    :param exc: expected exception which will be raised
    :return: context manager with functions:
        - do_something
        - log
        - sentry
    """

    with contextlib.ExitStack() as stack:
        mock_log = stack.enter_context(mock.patch(f'challenge.first.catching_error.log'))
        mock_sentry = stack.enter_context(mock.patch(f'challenge.first.catching_error.sentry'))
        mock_do_something = stack.enter_context(
            mock.patch(f'challenge.first.catching_error.do_something', side_effect=exc)
        )

        yield mock_do_something, mock_log, mock_sentry


class TestFirstChallenge(unittest.TestCase):
    TEST_DATA = [
        TestData(ValueError, False),
        TestData(KeyError, False),
        TestData(RemoteAccess, True),
        TestData(AuthorizationError, False),
    ]

    def test_catch_errors_in_log(self):
        for test_data in self.TEST_DATA:
            with patch_script_functions(test_data.exc) as mocks:
                mock_fn, mock_log, mock_sentry = mocks

                automate()

                mock_log.assert_called_once()
                if test_data.is_sentry:
                    mock_sentry.assert_called_once()
                else:
                    mock_sentry.assert_not_called()
