# 人生苦短，我学Python
# 2021年10月14日
# 人生苦短，我学Python
# 2021年10月14日
from math import sqrt
b=[]
for i in range(1,29):
    end=int(sqrt(i))
    a=0
    #for j in (1,end+2):
    j=1
    while j<end+2:
        if i%j == 0:
            a=a+j
        j+=1
    #print(a,i)
    if a==i:
        b.append(a)
print(b)
s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')