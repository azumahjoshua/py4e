
myList = []
while True:
    inputValue = input("Enter a number: ")
    if inputValue == 'done':
        break
    try:
        number = float(inputValue)
    except ValueError:
        print('Invalid input')
        exit()
    myList.append(number)
print('Maximum: ',max(myList))
print('Minimum: ',min(myList))