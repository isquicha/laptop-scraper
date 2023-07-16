import pytest


def pytest_sessionfinish(session: pytest.Session) -> None:
    if session.exitstatus == 5:
        session.exitstatus = 0
