dictionary_words = dict()    
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        if word in dictionary_words:
            continue
        dictionary_words[word] = word
    # print(words)
# print(dictionary_words)

# x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
# y = x.items()
# print(y)
# 
# days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
# print(days[2])
# 
# 
x = (5, 1, 3)
if (6, 0, 0)> x:
    print(True)
