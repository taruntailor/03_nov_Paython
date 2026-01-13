number= 156
dic=0

remin =number
i=0

while remin>0:

    dic +=int(remin%10)* (8**i)
    remin = int (remin/10)
    i+=1
print(f"Octal ki decimal value = {dic}")
