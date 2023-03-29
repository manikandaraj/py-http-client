"""
 * Project Name: Batman's Belt 
 * Author: Manikandaraj Srinivasan [manikandaraj.com]
 * Copyright (c) 2023 Manikandaraj Srinivasan @manikandaraj.com
 * License: MIT License 
 * Version: 1.0
 * 
 * Description: Used for making HTTP requests 
 *
 * Usage: Import the class and use it for making HTTP requests 
 * 
 * Dependencies: requests library 
"""

import requests

class HTTPRequest:
    def __init__(self, http_url):
        self.http_url = http_url

    def get_request(self):
        try:
            response = requests.get(self.http_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print("HTTP error occurred:", err)
        except Exception as err:
            print("An error occurred:", err)

    def post_request(self, data):
        try:
            response = requests.post(self.http_url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print("HTTP error occurred:", err)
        except Exception as err:
            print("An error occurred:", err)

    def put_request(self, data):
        try:
            response = requests.put(self.http_url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print("HTTP error occurred:", err)
        except Exception as err:
            print("An error occurred:", err)

    def delete_request(self):
        try:
            response = requests.delete(self.http_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print("HTTP error occurred:", err)
        except Exception as err:
            print("An error occurred:", err)

# Example usage
api = HTTPRequest("https://www.example.com/api/")
data = {"key": "value"}
print("GET Response:", api.get_request())
print("POST Response:", api.post_request(data))
print("PUT Response:", api.put_request(data))
print("DELETE Response:", api.delete_request())

