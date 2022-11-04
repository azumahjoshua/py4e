# n = 0
# while n > 0 :
#     print('Lather')
#     print('Rinse')
# print('Dry off!')

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

x = '40'
y = int(x) + 2
print(y)


x = 'From marquard@uct.ac.za'
# print(x[15:18])

# print(x[15:3])

# print(x[14+17])

# print(x[14:17])

# print(x[14:3])

# print(x[14/17])
# print(x[q])

# print(x[-1])
# 
# print(x[7])
# 
# print(x[8])
# 
# print(x[9])

print(len('banana')*7)


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])