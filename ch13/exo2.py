import urllib.request
import urllib.parse
import urllib.error
import json

count = 0
sum = 0
while True:
    url = input('Enter url: ')
    print("Retrieving url: ", url)
    # url_data = urllib.request.urlopen(url).read()
    if len(url) < 1:
        exit()
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    info = json.loads(data)
    # print(info)
    for item in info['comments']:
        # print(item['count'])
        count += 1
        sum = sum + item['count']
    print('Count: ', count)
    print('Sum: ', sum)
    count = 0
    sum = 0
