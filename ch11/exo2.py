import re
rev = []
fname = input('Enter file:')
try:
    fhand = open(fname)
except FileExistsError:
    print('File cannot be opened: ')
    exit()
for line in fhand:
    line = line.strip()
    rev_tem = re.findall('New Revision: ([0-9.]+)', line)
    # print(rev_tem)
    for val in rev_tem:
        if val != " ":
            val = float(val)
            # print(val)
            rev.append(val)
    # print(rev)
rev_sum = sum(rev)
print(rev_sum)
count = float(len(rev))
print(count)
rev_ave = rev_sum / count
print(rev_ave)
#
