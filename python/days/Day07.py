#Number system conversion in python
x = "10001"
print(f"{int(x,2)}")
#convert this binary number into decimal
#1. 11100
""" Take this number as input, use f-string
conversion expression inside the f-string"""

num1="11100"
print(f"{int(num1,2)}")

#Decimal to octal
x = 486 
#print(oct(x))
print(f"The octal of {x} is {oct(x)} ")

 #Octal to decimal
x = "124" #method1
print (int(x,8))

octal_number = int(x,8)#method2
print(octal_number)

print(f"{int(x,8)}")#method3
