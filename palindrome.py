n=1441
n1=n
sum=0
while(n>0):
    digit=n%10
    sum=sum*10+digit
    n//10
if sum==n1:
    print("palindrome")
else:
    print("not")
