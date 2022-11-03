num = 0
tot  = 0.0 
while True:
      sval = input("Inter a number: ")
      if sval == 'done':
        break
      try:
         fval = float(sval)
      except:
        print("Number must be an integer")
        continue

      num = num +1
      tot = tot + fval
print(tot,num,tot/num)