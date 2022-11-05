dictionary_words = dict()   
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        dictionary_words[word] = dictionary_words.get(word,0) + 1

# for key in dictionary_words:
    # print(key, dictionary_words[key])
print('Count',dictionary_words)