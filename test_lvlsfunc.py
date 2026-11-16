from lvlsfunc import count_levels
def test_count_levels_basic():
    loglist=["2026-11-09 10:15:02 INFO server started", "2026-11-09 10:15:09 WARNING disk usage at 85%", "2026-11-09 10:16:44 ERROR database timeout"]
    result=count_levels(loglist)
    expected={"INFO" : 1, "WARNING": 1, "ERROR":1}
    assert result == expected
def test_count_levels_empty():
    loglist=[]
    result=count_levels(loglist)
    expected={}
    assert result == expected
def test_count():
        loglist=["2026-11-09 10:15:02 INFO server started", "2026-11-09 10:15:02 INFO db started", "2026-11-09 10:15:09 WARNING disk usage at 85%", "2026-11-09 10:16:44 ERROR database timeout"]
        result=count_levels(loglist)
        expected={"INFO" : 2, "WARNING": 1, "ERROR":1}
        assert result == expected