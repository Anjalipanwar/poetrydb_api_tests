import requests
import pytest

from config import BASE_URL


@pytest.mark.parametrize("title", ["A Baby's Death", "A Ballad Of The Trees And The Master"])
def test_get_poems_by_title(title):
    """Test fetching poems by title."""
    response = requests.get(f"{BASE_URL}/title/{title}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list), "Response should be a list"
    assert len(data) > 0, "Response list should not be empty"
    assert all('author' in poem for poem in data), "Each poem should have an author"


def test_get_random_poems():
    """Test fetching random poems."""
    response = requests.get(f"{BASE_URL}/random")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list), "Response should be a list"
    assert len(data) > 0, "Response list should not be empty"
