a=int(input("side  1 value:"))
b=int(input("side 2 value:"))
c=int(input("side 3 value:"))
if a==b==c:
      print("equilateral triangle")
elif a==b or b==c or a==c:
    print("isosceles triangle")
else:
      print("scalene triangle")


