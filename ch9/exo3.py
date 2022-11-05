maximum = 0
maximum_address = ''
dictionary_words = dict()
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_words:
            dictionary_words[words[1]]  = 1
        else:
            dictionary_words[words[1]] +=1
# print(dictionary_words) 

for key in dictionary_words:
    if dictionary_words[key] > maximum:
        maximum = dictionary_words[key]
        maximum_address = key
print(maximum_address,maximum)