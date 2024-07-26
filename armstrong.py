a=153
a1=a
org=a1
sum=0
sum1=0
count=0
while(a>0):
    count=count+1
    a=a//10
while a1>0:
    digit=a1%10
    sum=digit**count
    sum1=sum1+sum
    a1=a1//10
if(sum1==org):
    print("armstrong")
else:
    print("not")
