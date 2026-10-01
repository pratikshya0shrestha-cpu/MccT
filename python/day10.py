# def area_of_rec(length, breadth):
#     return length * breadth
# area=area_of_rec(10,20)
# print(area)
# area2= area_of_rec(10,5)
# print(area2)

# #Find the preimeter of rectangle
# def perimeter_of_rec(length,width):
#     return 2*(length + width)
# perimeter= perimeter_of_rec(10,5)
# print(perimeter)



# #How to take user input inside a function.
# def square(num):
#     return num*num
# # return num**2
# # return math.pow(num,2)
# num=int(input("Enter a number:"))
# output = square(num)
# print(f"square of {num} = {output}")

# #Find odd even from the given input
# #make sure you define a function

# def even_num(number):
#     return number % 2 == 0

# number = int(input("Enter a number:"))
# if even_num(number):
#     print("It is an even number")
# else:
#     print("It is odd number")


#    #If you are above 18 you are an adult else you are underage
# def age(number):
#     return number >= 18

# number = int(input("Enter a number:"))
# if age(number):
#     print("you are an adult")
# else:
#     print("You are underage")


# #Fruitful and non-fruitful function
# # Fruitful function -> returns a Value
# # Non-fruitful function -> performs a certain activity or action

# # def hello(name="RAM"):
# #     print (f"hello{name}")
# #hello()
# #GLOBAL VARIABLE
# # name="RAM"
# # def greetings(name):
# #         print(name)
 
#  #Calling a function from a function

# def square(number):
#     return number*number

# def show_value(number):
#     result =square(number)
#     print(f"square of a {number}={result}")
#     show_value(5)

# for i in range(100):
#     print("Hello")

#Loop: repeatedly executing a block of code , in a specific condition, or 
#if the algorithm requirement.
#print from 1 to 10
for i in range(1, 11):
    print(i)

for i in range(0,6):
    print(i)

for i in range(5):
    print("Pratikshya")

#range(start,stop)
#range(stop)
#range(1,10,2)->(start,stop,step)
for i in range(1,10,2):
    print(i)
#Multiplication of 5
for i in range(5,51,5):
    print(i)

# #counting backwards
for i in range(10,0,-1):
    print(i)





