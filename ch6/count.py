def count(word,se):
    ct = 0
    for letter in word:
        if letter == se:
            ct = ct +1
    return ct

print(count('banana','b'))