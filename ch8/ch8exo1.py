def chop(t):
    del t[0]
    del t[-1]

letters = ['a', 'b', 'c']
print(letters)
chop(letters)
print(letters)

def middle(lst):
    new = lst[1:]
    del new[-1]
    return new

letters = ['a', 'b', 'c']
print(middle(letters))