import main

def test_extract_field_offices():

    data = main.fetch_data(page=1)

    assert 'field_offices' in data['items'][0], "Expected 'field_offices' field in the first item"
    assert isinstance(data['items'][0]['field_offices'], list), "Expected 'field_offices' to be a list"
