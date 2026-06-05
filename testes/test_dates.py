import pytest
from datetime import datetime

from paper_fetch.dates import parse_since


def test_parse_since_returns_datetime():
    result = parse_since("7d")

    assert isinstance(result, datetime)


def test_parse_since_invalid_suffix():
    with pytest.raises(ValueError):
        parse_since("7")


def test_parse_since_invalid_number():
    with pytest.raises(ValueError):
        parse_since("abcd")


def test_parse_since_30_days():
    result = parse_since("30d")

    assert isinstance(result, datetime)