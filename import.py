import csv
f=open("ramya.csv",'a',newline="")
a=csv.writer(f)
a.writerow(["name","rollno","place","college"])
name=input("enter name:")
rollno=int(input("enter roll number:"))
place=input("enter place:")
college=input("enter college name")
a.writerow(["name","rollno","place","college"])
print("data has been saved")
