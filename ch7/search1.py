fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip() #use the rstrip method which strips whitespaces from the right side of a string
    if line.startswith('From:'):
        print(line)
