import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from datetime import datetime, timedelta
from utils import (
    sortiereListe, parse_dt, validate_email, passwords_match, strong_password,
    is_nonempty_string, hours_between, format_date, is_valid_id
)

def test_sortiereListe():
    assert sortiereListe([3, 6, 1]) == [1, 3, 6]
    assert sortiereListe([]) == []
    assert sortiereListe([-2, 0, 1]) == [-2, 0, 1]

def test_parse_dt():
    assert parse_dt("2024-01-01 12:00:00") == datetime(2024, 1, 1, 12, 0, 0)
    assert parse_dt("2024-01-01 09:30") == datetime(2024, 1, 1, 9, 30)
    with pytest.raises(ValueError):
        parse_dt("bad-date")
    assert parse_dt(None) is None

def test_validate_email():
    assert validate_email("test@example.com")
    assert validate_email("a@b.co")
    assert not validate_email("test@")
    assert not validate_email("test.com")
    assert not validate_email("")
    assert not validate_email(None)

def test_passwords_match():
    assert passwords_match("123", "123")
    assert not passwords_match("123", "456")
    assert not passwords_match("", "")
    assert not passwords_match("abc", "")

def test_strong_password():
    assert strong_password("abcdef")
    assert strong_password("1234567")
    assert not strong_password("abc")
    assert not strong_password("")
    assert not strong_password(None)

def test_is_nonempty_string():
    assert is_nonempty_string("abc")
    assert not is_nonempty_string("   ")
    assert not is_nonempty_string("")
    assert not is_nonempty_string(None)
    assert not is_nonempty_string(123)

def test_hours_between():
    dt1 = datetime(2024, 1, 1, 10, 0, 0)
    dt2 = datetime(2024, 1, 1, 12, 30, 0)
    assert hours_between(dt1, dt2) == 2.5
    assert hours_between(dt2, dt1) == 0
    assert hours_between(dt1, None) == 0
    assert hours_between(None, dt2) == 0
    assert hours_between(None, None) == 0

def test_format_date():
    dt = datetime(2024, 1, 2)
    assert format_date(dt) == "02.01.2024"
    assert format_date(None) == ""

def test_is_valid_id():
    assert is_valid_id(1)
    assert is_valid_id("5")
    assert not is_valid_id(0)
    assert not is_valid_id(-3)
    assert not is_valid_id("abc")
    assert not is_valid_id(None)