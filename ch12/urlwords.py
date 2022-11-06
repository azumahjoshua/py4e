import urllib.request
import urllib.parse
import urllib.error

count = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word, 0)+1  # create a word frequency
print(count)
