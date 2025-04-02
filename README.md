![DoD Spend (3000 x 3000 px) (454 x 265 px) (4)](https://github.com/user-attachments/assets/0cfa4c23-455b-4d2d-9fb7-db894f922fb3)

# FBI Most Wanted API 

<img width="560" alt="Screenshot 2025-04-02 at 3 36 19 PM" src="https://github.com/user-attachments/assets/b5e652df-1b90-457a-8955-b7f716edf00f" />

A Python client for interacting with the FBI Most Wanted API.

## Features

- Fetch basic wanted list
- Search by field office
- Paginated results
- Custom search by crime type, nationality, and age range
- Rate limiting handling with exponential backoff
- Error handling for network and JSON parsing issues

## Requirements

- Python 3.x
- requests library (`pip install requests`)

## Installation

1. Clone this repository:
```bash
git clone [repository-url]
cd [repository-name]
```
## Install Dependencies 

```python3
pip install requests
```
## Usage 

```
python3 fbi.py
```
The script includes four example functions:

`basic_example()`: Shows total count and first wanted person

`search_by_field_office()`: Searches Miami field office

`paginated_example()`: Gets page 2 of results

`custom_search_example()`: Searches with specific criteria

You can also import and use the `FBIMostWantedAPI` class in your own code:

```python3
from fbi import FBIMostWantedAPI

api = FBIMostWantedAPI()

# Basic list
data = api.get_wanted_list()

# Search with parameters
data = api.search_by_criteria(
    crime_type="Violent Crime",
    nationality="American",
    age_min=25,
    age_max=40
)
```
## API Parameters

Available search parameters include:

`field_offices`: FBI field office (e.g., "miami")

`page`: Page number for pagination

`crime_type`: Type of crime

`nationality`: Nationality of wanted person

`age_min`: Minimum age

`age_max`: Maximum age

## FBI Full List 

This is a version where it will list all most wanted without you having to manually entering API fields. 

## Author 

Michael Mendy (c) 2025. 


