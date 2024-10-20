# Project Structure

    .
    ├── README.md                   # This file
    ├── config.py                   # Configuration file containing base URL and other constants
    ├── data                        # Directory for storing JSON data files
    │   ├── expected_titles.json    # Expected titles for poems with specified line counts
    │   └── linecount_responses.json # Expected responses for line count API tests
    ├── pytest.ini                  # Configuration file for pytest
    ├── requirements.txt            # List of dependencies required for the project
    └── tests                       # Directory for test files
        ├── __init__.py             # Initializes the tests package
        ├── conftest.py             # Configuration for pytest fixtures
        ├── test_by_author.py       # Test cases for fetching poems by author
        ├── test_by_linecount.py    # Test cases for line count API
        └── test_by_poem.py         # Test cases for fetching poems by title


# Test Cases

## Test Case 1: Fetch Poems by Author

| Step | Action | Expected Result | Validation Method |
|------|--------|-----------------|-------------------|
| 1    | Send a GET request to `/author/Emily Dickinson` | Status code 200 received | Check if response status code is 200 |
| 2    | Send a GET request to `/author/William Wordsworth` | Status code 200 received | Check if response status code is 200 |
| 3    | Send a GET request to `/author/Robert Frost` | Status code 200 received | Check if response status code is 200 |
| 4    | Send a GET request to `/author/Unknown Author` | Status code 200 received | Check if response status code is 200 |
| 5    | Verify response data for Emily Dickinson is a list | Response should be a list | Use `isinstance(data, list)` to validate |
| 6    | Check that the response list for Emily Dickinson is not empty | List contains poems | Use `assert len(data) > 0` to ensure the list is not empty |
| 7    | Ensure each poem for Emily Dickinson has a title | Each poem should include 'title' field | Use `assert all('title' in poem for poem in data)` to validate |
| 8    | Verify response data for Robert Frost is a dictionary | Response should be a dictionary | Use `isinstance(data, dict)` to validate |
| 9    | Check that the response indicates no poems found for Robert Frost | Response contains reason for 404 status | Assert `data['reason']` is 'Not found' |
| 10   | Validate status for Robert Frost | Status should be 404 | Assert `data['status']` is 404 |
| 11   | Verify response data for Unknown Author is a dictionary | Response should be a dictionary | Use `isinstance(data, dict)` to validate |
| 12   | Check that the response indicates no poems found for Unknown Author | Response contains reason for 404 status | Assert `data['reason']` is 'Not found' |
| 13   | Validate status for Unknown Author | Status should be 404 | Assert `data['status']` is 404 |

### Validation Description
- **Status Code Validation**: This checks if the API responded correctly. A status code of 200 indicates success for authors with poems, while a status code of 404 confirms that the author has no poems.
- **Type Validation**: Ensures that the data format returned by the API is as expected (list for authors with poems and dictionary for authors without poems).
- **Content Validation**: Confirms that the returned list contains poems and that each poem has the necessary information (title) for authors with poems, while verifying the correct reason for the 404 status for authors without poems.

---

## Test Case 2: Fetch Titles by Line Count

| Step | Action | Expected Result | Validation Method |
|------|--------|-----------------|-------------------|
| 1    | Send a GET request to `/linecount/3/title` | Status code 200 received | Check if response status code is 200 |
| 2    | Verify response data is a list | Response should be a list | Use `isinstance(data, list)` to validate |
| 3    | Extract titles from response | Titles are correctly extracted | Use list comprehension to get titles from data |
| 4    | Compare extracted titles with expected titles | Extracted titles match expected titles | Use `assert actual_titles == expected_titles_output` for comparison |

### Validation Description
- **Status Code Validation**: Confirms that the API successfully processed the request.
- **Type Validation**: Checks if the data returned is in the correct format.
- **Content Comparison**: Ensures the data returned matches expected results, verifying the accuracy of the API's output.

---

## Test Case 3: Fetch Poems by Title

| Step | Action | Expected Result | Validation Method |
|------|--------|-----------------|-------------------|
| 1    | Send a GET request to `/title/A Baby's Death` | Status code 200 received | Check if response status code is 200 |
| 2    | Verify response data is a list | Response should be a list | Use `isinstance(data, list)` to validate |
| 3    | Check that the response list is not empty | List contains poems | Use `assert len(data) > 0` to ensure the list is not empty |
| 4    | Ensure each poem has an author | Each poem should include 'author' field | Use `assert all('author' in poem for poem in data)` to validate |
| 5    | Send a GET request to `/title/A Ballad Of The Trees And The Master` | Status code 200 received | Check if response status code is 200 |
| 6    | Verify response data is a list | Response should be a list | Use `isinstance(data, list)` to validate |
| 7    | Check that the response list is not empty | List contains poems | Use `assert len(data) > 0` to ensure the list is not empty |
| 8    | Ensure each poem has an author | Each poem should include 'author' field | Use `assert all('author' in poem for poem in data)` to validate |

### Validation Description
- **Status Code Validation**: Confirms that the API responded successfully with a status code of 200.
- **Type Validation**: Ensures that the returned data format is a list.
- **Content Validation**: Verifies that the list of poems is not empty and that each poem contains the 'author' field.

---

## Test Case 4: Fetch Random Poems

| Step | Action | Expected Result | Validation Method |
|------|--------|-----------------|-------------------|
| 1    | Send a GET request to `/random` | Status code 200 received | Check if response status code is 200 |
| 2    | Verify response data is a list | Response should be a list | Use `isinstance(data, list)` to validate |
| 3    | Check that the response list is not empty | List contains random poems | Use `assert len(data) > 0` to ensure the list is not empty |

### Validation Description
- **Status Code Validation**: Confirms that the API responded successfully with a status code of 200.
- **Type Validation**: Ensures that the returned data format is a list.
- **Content Validation**: Verifies that the list is not empty, indicating that random poems were successfully retrieved.



# How to Use This Test Repository

### Installation

1. **Clone the Repository:**
   Open your terminal and run the following command to clone the repository to your local machine:
   
   ```bash
   git clone https://github.com/Anjalipanwar/poetrydb_api_tests.git
   cd poetrydb_api_tests

   ```

2. **Install Dependencies:** Ensure you have Python installed (preferably version 3.6 or higher).
   Then, install the required packages using pip:
   
   ```bash
    pytest tests/test_by_author.py
    
    ```


### Running Tests
    **Execute:** 

    ```bash
    pytest tests/test_by_author.py
    
    ```

# Code Style Checks with Flake8

1. **Run Flake8:** Flake8 is a tool for checking the style guide enforcement of your Python code. 
To check your code for style issues, run:

    ```bash
    flake8 .
    
    ```

