import pytest
from logentry import parse_line
@pytest.fixture
def error_line():
    return "2026-11-09 10:16:44 ERROR database timeout"
def test_parse_line(error_line):
    result=parse_line(error_line)
    assert result.level=="ERROR"
    assert result.message=="database timeout"
def test_empty_line():
    line=[""]
    result=parse_line(line[0])
    assert result is None
def test_invalid_level():
    line=["2026-11-09 10:16:44 CRITICAL database timeout"]
    result=parse_line(line[0])
    assert result is None
def test_parse_line_lowercase_level():
    line="2026-11-09 10:16:44 error database timeout"
    result=parse_line(line)
    assert result.level == "ERROR" 
    assert result.message == "database timeout"
def test_parse_line_two_words():
    line="2026-11-09 10:16:14"
    result=parse_line(line)
    assert result is None
def test_parse_line_no_message():
    line="2026-11-09 10:16:44 ERROR"
    result=parse_line(line)
    assert result.level == "ERROR"
    assert result.message == ""