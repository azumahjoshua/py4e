fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    # print(words[1])

# it is important to distinguish between operations that modify lists and operations that create new lists. For example, the append method modifies a list, but the + operator creates a new list
a = "banana"
b = "banana"
print(a is b)


words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
print(pieces)
parts = pieces[3].split('-')
print(parts)
n = parts[1]

print(n)

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])

t = [9, 41, 12, 3, 74, 15]
print(t[2:4])


fruit = 'Banana'
fruit[0] = 'b'
print(fruit)