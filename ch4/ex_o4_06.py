def computepay(hours,rate):
    print("In compute pay",hours,rate)
    if hours > 40:
        reg = rate *hours
        otp = (hours -40.0)*(rate*0.5)
        pay = reg* otp
    else:
        pay = rate * hours
    
    return pay


sh = input('Enter hours: ')
sr = input('Enter hours: ')
fh = float(sh)
fr = float(sr)
print(computepay(fh,fr))
    
    
    
    
    
    
    