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
 * Dependencies: requests, urllib3
"""

import requests
from urllib3.exceptions import InsecureRequestWarning

class HTTPRequest:
    def __init__(self, http_url):
        self.http_url = http_url

    def get_request(self, get_args=None, headers={}, connection_time_out=10, skip_https_certificate_check=False):
        try:
            if(skip_https_certificate_check):
                #Disable warnings for insecure HTTPS requests
                requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

            response = requests.get(
                self.http_url,
                headers=headers,
                params=get_args,
                timeout=connection_time_out,
                verify=not skip_https_certificate_check
            )
            response.raise_for_status()  #Raise an exception if the response contains an HTTP error status code
            return response.json()
        except requests.exceptions.RequestException as exc:
            print(f"An error occurred while making the request: {exc}")
        except ValueError:
            print("The response could not be parsed as JSON.")
        except Exception as exc:
            print(f"An unexpected error occurred: {exc}")
        return None

    def post_request(self, post_args=None, post_json=None, headers={}, connection_time_out=10, skip_https_certificate_check=False): 
        try:
            if(skip_https_certificate_check):
                #Disable warnings for insecure HTTPS requests
                requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

            response = requests.post(
                self.http_url,
                headers=headers,
                data=post_args,
                json=post_json,
                timeout=connection_time_out,
                verify=not skip_https_certificate_check
            )
            response = requests.post(self.http_url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as exc:
            print(f"An error occurred while making the request: {exc}")
        except ValueError:
            print("The response could not be parsed as JSON.")
        except Exception as exc:
            print(f"An unexpected error occurred: {exc}")
        return None

    def put_request(self, put_args=None, put_json=None, headers={}, connection_time_out=10, skip_https_certificate_check=False): 
        try:
            if(skip_https_certificate_check):
                #Disable warnings for insecure HTTPS requests
                requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

            response = requests.put(
                self.http_url,
                headers=headers,
                data=put_args,
                json=put_json,
                timeout=connection_time_out,
                verify=not skip_https_certificate_check
            )
            response = requests.put(self.http_url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as exc:
            print(f"An error occurred while making the request: {exc}")
        except ValueError:
            print("The response could not be parsed as JSON.")
        except Exception as exc:
            print(f"An unexpected error occurred: {exc}")
        return None

    def delete_request(self, headers={}, connection_time_out=10, skip_https_certificate_check=False): 
        try:
            if(skip_https_certificate_check):
                #Disable warnings for insecure HTTPS requests
                requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

            response = requests.delete(
                self.http_url,
                headers=headers,
                timeout=connection_time_out,
                verify=not skip_https_certificate_check
            )
            response = requests.delete(self.http_url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as exc:
            print(f"An error occurred while making the request: {exc}")
        except ValueError:
            print("The response could not be parsed as JSON.")
        except Exception as exc:
            print(f"An unexpected error occurred: {exc}")
        return None

# Example usage
api = HTTPRequest("https://www.example.com/api")
data = {"key": "value"}
print("GET Response:", api.get_request())
print("POST Response:", api.post_request(data))
print("PUT Response:", api.put_request(data))
print("DELETE Response:", api.delete_request())

