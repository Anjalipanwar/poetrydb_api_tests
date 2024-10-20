import requests
import pytest

BASE_URL = "https://poetrydb.org"

@pytest.mark.parametrize("author", ["Robert Frost", "Emily Dickinson", "William Wordsworth"])
def test_get_poems_by_author(author):
    """Test fetching poems by author."""
    response = requests.get(f"{BASE_URL}/author/{author}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data, list), "Response should be a list"
    assert len(data) > 0, "Response list should not be empty"
    assert all('title' in poem for poem in data), "Each poem should have a title"
