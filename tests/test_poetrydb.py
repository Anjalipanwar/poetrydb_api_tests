import requests
import pytest

BASE_URL = "https://poetrydb.org"

# Authors expected to be found
found_authors = ["Emily Dickinson", "William Wordsworth"]
# Authors expected to have no poems
no_poems_authors = ["Robert Frost", "Unknown Author"]

# Combine both author lists for testing
author_test_cases = found_authors + no_poems_authors

@pytest.mark.parametrize("author", author_test_cases)
def test_get_poems_by_author(author):
    """Test fetching poems by authors, verifying response based on expectation."""
    response = requests.get(f"{BASE_URL}/author/{author}")
    
    if author in found_authors:
        assert response.status_code == 200, f"Expected status code 200 for author {author}"
        data = response.json()
        
        assert isinstance(data, list), "Response should be a list"
        assert len(data) > 0, "Response list should not be empty"
        assert all('title' in poem for poem in data), "Each poem should have a title"
    
    elif author in no_poems_authors:
        assert response.status_code == 200, f"Expected status code 200 for author {author} as poems are expected to exist"
        data = response.json()
        
        assert isinstance(data, dict), "Response should be a dictionary"
        assert 'reason' in data and data['reason'] == 'Not found', "Response should indicate the reason for the 404 status"
        assert data['status'] == 404, "Status should be 404"
