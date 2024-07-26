#write the fun to calculate sum of  first and last digit of a number
def fun(a):
    digit=a%10
    b=digit
    a=a//10
    while a>0:
        n=a%10
        a=a//10
    c=n
    print(c+b)
fun(1052)
        

        
