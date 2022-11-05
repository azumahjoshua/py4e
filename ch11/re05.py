import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
let = re.findall('\S+@\S+', s)
print(let)
