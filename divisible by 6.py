#calculate the diff of sum of numbers that are divisible by 6 and not divisible by 6 in the range of 1st 30 numbers
sum=0
sum1=0
for i in range(1,31):
    if(i%6==0):
        sum=sum+i
    else:
        sum1=sum1+i
print(sum1-sum)
