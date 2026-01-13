number = 1011
num=number
c=0
s=0
while number>0:
    r=number%10
    k= r*(2**c)
    s=s+k
    number=number/10
    c=c+1

print(s,"is the demical number ", num)