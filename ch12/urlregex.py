# The ssl library allows this program to access web sites that strictly enforce HTTPS. The read method returns HTML source code as a bytes object instead of returning an HTTPResponse object. The findall regular expression method will give us a list of all of the strings that match our regular expression, returning only the link text between the double quotes
import urllib.request
import urllib.parse
import urllib.error

import re

import ssl

ctx = ssl.create_default_context()

ctx.check_hostname = False

ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -: ')

html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())
