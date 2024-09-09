
import main

def test_fetch_non_empty_data():
    
    data = main.fetch_data(page=1)
    assert len(data['items']) > 0, "Expected non-empty data from the FBI API"
