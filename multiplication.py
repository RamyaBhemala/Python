a=12345
product=1
while(a>0):
    digit=a%10
    product=product*digit
    a=a//10
print(product)
