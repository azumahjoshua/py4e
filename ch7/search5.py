count = 0
total = 0
fname = input('Enter a file name: ')
try:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        exit()
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
for line in fhand:
    if line.startswith('X-DSPAM-Confidence'):
        pos = line.rstrip().find(':')
        count = count +  1
        number = (line[pos+1:]).rstrip()
        fnumber = float(number)
        total = total + fnumber
average = total / count
print('Average spam confidence: ', average)    
