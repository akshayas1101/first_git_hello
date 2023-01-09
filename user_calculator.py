a=input("enter a number :")
b=input("enter a number :")
if a.isnumeric() and b.isnumeric():
    c=int(a)+int(b)
else:
    c="cannot be added"    
print(c)