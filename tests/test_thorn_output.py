import main
from io import StringIO
import sys

def test_thorn_separated_output(monkeypatch):

    dummy_data = {
        'items': [
            {
                'title': 'Test Title',
                'subjects': ['Subject1', 'Subject2'],
                'field_offices': ['Office1', 'Office2']
            }
        ]
    }

    def mock_fetch_data(page):
        return dummy_data
    

    monkeypatch.setattr(main, 'fetch_data', mock_fetch_data)

    captured_output = StringIO()
    sys.stdout = captured_output

    main.main(page=1)

    sys.stdout = sys.__stdout__

    expected_output = "Test TitleþSubject1,Subject2þOffice1,Office2\n"

    assert captured_output.getvalue() == expected_output, "Expected thorn-separated output"

