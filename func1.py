#write a function which takes two parameters a and b typecast the value of second argument into integer.Then multiply both the arguments and print the last digit of the result

def fun(a,b):
    b=int(b)
    c=a*b
    digit=int(c%10)
    print(digit)
fun(27.9,5.5)
