from app.utils import doThing

def test_do_thing_ok():
    result = doThing("alice", 1,2,3,4,5,6,7,8,9)
    assert result is True
