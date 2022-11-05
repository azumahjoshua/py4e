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
        if words[2] not in dictionary_words:
            dictionary_words[words[2]]  = 1
        else:
            dictionary_words[words[2]] +=1
print(dictionary_words)