from datetime import datetime

import pytest

from crawler.crawler.utils.datetime import parse_datetime


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("25/12/2023 14:30", datetime(2023, 12, 25, 14, 30)),
        ("25/12/2023", datetime(2023, 12, 25)),
        ("None", None),
        ("abc", None),
        ("", None),
        (None, None),
        ("32/12/2023", None),
        ("25/13/2023", None),
    ],
)
def test_parse_datetime(input_data, expected):
    assert parse_datetime(input_data) == expected