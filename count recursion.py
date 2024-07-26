#write a recursive function to count number of digits of a number
def count(n):
    if n==0:
        return 0
    else:
        return 1+count(n//10)
    
    
    
