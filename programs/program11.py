# Program to open a webpage using urllib library.

import urllib.request

data = urllib.request.urlopen("https://obnerd.in")
print(data.read())
