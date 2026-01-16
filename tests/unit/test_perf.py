from app.transform import clean_data

def test_clean_data():
    assert clean_data([1, None, 2]) == [1, 2]
