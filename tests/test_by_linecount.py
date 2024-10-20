import requests
import pytest
import json

BASE_URL = "https://poetrydb.org"



@pytest.mark.parametrize("endpoint, expected_linecount", [
    ("/linecount/3", 3),
    ("/linecount/51", 51),
    ("/linecount/999", 999),
])
def test_linecount_api(endpoint, expected_linecount, load_json):
    """Test linecount API for verifying titles along with expected linecounts."""
    # Load the json_data from the specified file
    json_data = load_json('data/linecount_responses.json')

    response = requests.get(f"{BASE_URL}{endpoint}")
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"

    # Parse the actual response data
    actual_data = response.json()
    # Found expected_linecount of tpye list in the response
    if isinstance(actual_data, list):
        
        # Generate the key for accessing the expected data in the json_data
        expected_key = f"linecount_{expected_linecount}"

        # Fetch expected titles from the json_data
        expected_titles = [
            poem["title"] for poem in json_data[expected_key]
        ]

        # Initialize a list to hold titles from the actual data that match the expected linecount
        actual_titles = [
            item['title'] for item in actual_data
            if int(item['linecount']) == expected_linecount  # Ensure the linecount matches
        ]
        
        # Assert that all expected titles are present in the actual titles
        for expected_title in expected_titles:
            assert expected_title in actual_titles, (
                f"Expected title: {expected_title} not found in actual titles: {actual_titles}"
            )

    elif isinstance(actual_data, dict):
        expected_response = {"status": 404, "reason": "Not found"}
        assert actual_data == expected_response, (
            f"Expected 404 response: {expected_response}, but got: {actual_data}"
        )


def test_get_poem_titles_by_linecount(load_json):
    """Test fetching titles of poems with an exact linecount of 3."""
    # Load the expected titles from the specified file
    expected_titles_output = load_json("data/expected_titles.json")
    response = requests.get(f"{BASE_URL}/linecount/3/title")
    
    assert response.status_code == 200, "Expected status code 200"
    
    actual_data = response.json()

    # Extract only the titles of poems from the actual data
    actual_titles = [{"title": poem["title"]} for poem in actual_data if poem["title"] in [item["title"] for item in expected_titles_output]]

    # Check that all items in the filtered actual data contain only the 'title' field
    for item in actual_titles:
        assert "title" in item, "Each item should have a 'title' field"
        assert len(item) == 1, "Each item should only contain the 'title' field"

    # Compare the filtered actual data with the expected data
    assert actual_titles == expected_titles_output, f"Expected: {expected_titles_output}, Actual: {actual_titles}"