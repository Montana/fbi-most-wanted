import requests
import json
from typing import Dict, Optional
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class FBIMostWantedAPI:
    def __init__(self):
        self.base_url = "https://api.fbi.gov/wanted/v1/list"
        self.headers = {
            "User-Agent": "FBI Wanted API Client/1.0"
        }
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)

    def get_wanted_list(self, params: Optional[Dict] = None) -> Dict:
        try:
            response = self.session.get(
                self.base_url,
                headers=self.headers,
                params=params if params else {},
                timeout=10
            )
            response.raise_for_status()
            return json.loads(response.content)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            if hasattr(e.response, 'status_code') and e.response.status_code == 429:
                wait_time = int(e.response.headers.get('Retry-After', 60))
                print(f"Rate limited. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
            return {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {}

    def search_by_criteria(self, 
                          crime_type: Optional[str] = None,
                          nationality: Optional[str] = None,
                          age_min: Optional[int] = None,
                          age_max: Optional[int] = None) -> Dict:
        params = {}
        if crime_type:
            params['crime_type'] = crime_type
        if nationality:
            params['nationality'] = nationality
        if age_min:
            params['age_min'] = age_min
        if age_max:
            params['age_max'] = age_max
        return self.get_wanted_list(params)

def basic_example():
    api = FBIMostWantedAPI()
    data = api.get_wanted_list()
    if data:
        print(f"Total wanted individuals: {data.get('total', 0)}")
        if data.get('items') and len(data['items']) > 0:
            print(f"First wanted person: {data['items'][0].get('title', 'N/A')}")

def search_by_field_office():
    api = FBIMostWantedAPI()
    params = {
        'field_offices': 'miami'
    }
    data = api.get_wanted_list(params)
    if data:
        print(f"Total in Miami field office: {data.get('total', 0)}")
        if data.get('items') and len(data['items']) > 0:
            print(f"First Miami wanted person: {data['items'][0].get('title', 'N/A')}")
            print(f"Description: {data['items'][0].get('description', 'N/A')}")

def paginated_example(page_number: int = 2):
    api = FBIMostWantedAPI()
    params = {
        'page': page_number
    }
    data = api.get_wanted_list(params)
    if data:
        print(f"Current page: {data.get('page', 'N/A')}")
        print(f"Total pages: {data.get('total_pages', 'N/A')}")
        if data.get('items') and len(data['items']) > 0:
            print(f"First person on page {page_number}: {data['items'][0].get('title', 'N/A')}")

def custom_search_example():
    api = FBIMostWantedAPI()
    data = api.search_by_criteria(
        crime_type="Violent Crime",
        nationality="American",
        age_min=25,
        age_max=40
    )
    if data and data.get('items'):
        print(f"Found {data.get('total')} matching individuals")
        print(f"First match: {data['items'][0].get('title', 'N/A')}")

def main():
    print("=== Basic Example ===")
    basic_example()
    time.sleep(2)  
    print("\n=== Search by Field Office (Miami) ===")
    search_by_field_office()
    time.sleep(2)
    print("\n=== Paginated Example (Page 2) ===")
    paginated_example(2)
    time.sleep(2)
    print("\n=== Custom Search Example ===")
    custom_search_example()

if __name__ == "__main__":
    main()
