#write recursive program to print the digits in rev order
def fun(n):
    if n==0:
        return 
    else:
        print(n%10)
        return fun(n//10)
print(fun(12345))
