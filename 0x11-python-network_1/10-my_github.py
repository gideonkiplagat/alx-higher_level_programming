#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id


FUNCTIONALITY

1.First, we import the required packages, requests and sys.

2. We get the username and password (personal access token)
    from the command line arguments using the sys module.

3. We set up the API endpoint URL to retrieve the user information.

4. We set up the Basic Authentication header with the provided
    credentials using the base64 encoding.

5. We make the API call using the requests.get method and
    passing the URL and headers as parameters.

6. We check the response status code to ensure that the
    API call was successful.

7. If the API call was successful, we display the user id by
    accessing the 'id' key of the JSON response.
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    r = requests.get(url,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))