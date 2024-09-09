import main

def test_extract_title():

    data = main.fetch_data(page=1)
    
    assert 'title' in data['items'][0], "Expected 'title' field in the first item"
    assert data['items'][0]['title'] != '', "Expected non-empty title in the first item"
