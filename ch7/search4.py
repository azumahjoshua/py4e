fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip() #use the rstrip method which strips whitespaces from the right side of a string
    # if not line.startswith('From:'):
        # continue
    # Since find looks for an occurrence of a string within another string and either returns the position of the string or -1 if the string was not found
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)
