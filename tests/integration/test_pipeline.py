from app.transform import clean_data
from app.metrics import average

def test_pipeline():
    data = [1, None, 3]
    clean = clean_data(data)
    assert average(clean) == 2
