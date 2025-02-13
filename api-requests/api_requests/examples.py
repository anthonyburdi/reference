"""Examples of using the python requests library"""

import os
import requests
from requests.auth import HTTPBasicAuth


def main() -> None:
    base_url = "http://httpbin.org"
    get_url = f"{base_url}/get"

    # Simple GET
    response = requests.get(get_url)
    print_response_info(response)

    # URL Params
    params = {"key1": "value1", "key2": "value2"}
    response = requests.get(get_url, params=params)

    # Custom headers
    headers = {"Accept": "application/json"}
    response = requests.get(get_url, headers=headers)

    # API Key auth
    auth = HTTPBasicAuth("apikey", os.environ.get("MY_API_KEY"))
    response = requests.get(url=get_url, headers=headers, auth=auth)

    # Simple POST
    post_url = f"{base_url}/post"
    payload = {"key1": "value1", "key2": "value2"}
    response = requests.post(url=post_url, data=payload)
    print_response_info(response)

    # PUT = update resource (all fields), PATCH = partial update, DELETE, HEAD, OPTIONS

    # Session to persist parameters or headers across requests
    session = requests.Session()

    session.params = {"url_param_key": "value"}
    session.headers = {"Accept": "application/json", "Custom-Header": "my_value"}
    session.auth = auth

    response = session.get(get_url)
    print_response_info(response)
    # Same params, headers & auth used
    response = session.get(get_url)
    print_response_info(response)

    # Error handling
    # try:
    #     response = requests.get(get_url, timeout=3)
    # except requests.exceptions.ConnectionError:
    #     print("handle connection error")

    # Raise for status
    response = requests.get(get_url, timeout=3)
    response.raise_for_status()

    # Upload file(s)
    # files = {"file1": open("report.xls", "rb"), "file2": open("data.json", "rb")}
    # response = requests.post(post_url, files=files)


def print_response_info(response) -> None:
    print("response.ok:", response.ok)
    print("response.status_code:", response.status_code)
    print("response.text:\n", response.text)
    print("response.json():\n", response.json())
    # Binary content -> response.content


if __name__ == "__main__":
    main()
