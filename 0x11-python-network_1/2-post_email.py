#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This scrpt Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    email = {'email': argv[2]}
    email = urlencode(email)
    email = email.encode('ascii')
    request = Request(url, email)
    with urlopen(request) as response:
        string = response.read().decode('utf-8')
        print(string)
