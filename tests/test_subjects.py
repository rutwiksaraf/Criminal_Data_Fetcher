import main

def test_extract_subjects():

    data = main.fetch_data(page=1)

    assert 'subjects' in data['items'][0], "Expected 'subjects' field in the first item"
    assert isinstance(data['items'][0]['subjects'], list), "Expected 'subjects' to be a list"
