# Program to open a webpage using urllib library.

import urllib.request

data = urllib.request.urlopen("https://obnerd.in")
for line in data:
    print(data.read())
