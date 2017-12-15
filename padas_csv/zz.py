import re
p='11-20'
print(p[-1])
if re.findall("\d",p[-1]):
    p=p[:]+"㎡"
print(p)
