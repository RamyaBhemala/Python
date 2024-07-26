def sum(n):
    if n==0:
        return 0
    else:
        digit=n%10
        return digit+sum(n//10)
print(sum(52345))
    
