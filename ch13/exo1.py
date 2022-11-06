import urllib.request
import xml.etree.ElementTree as ET


# When an application makes a set of services in its API available over the web, we call these web services.
count = 0
sum = 0
url = input('Enter a url:')
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
for item in results:
    countvalue = int(item.find('count').text)
    count += 1
    sum = sum + countvalue

print("Count : ", count)
print("Sum : ", sum)

# Sample data: http: // py4e-data.dr-chuck.net/comments_42.xml
