import pytest
import json


@pytest.fixture(scope="session")
def load_json():
    """Fixture to load JSON data from a specified file."""

    def _load_json(filename):
        with open(filename) as f:
            return json.load(f)

    return _load_json
