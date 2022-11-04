mylist = []
fhand = open('romeo.txt')
for line in fhand:
    newords = line.split()
    for word in newords:
        if word in mylist:
            continue
        mylist.append(word)

# print(newords)
print(sorted(mylist))
