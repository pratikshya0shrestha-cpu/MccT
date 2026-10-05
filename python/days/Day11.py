#NOTES -> List,indexing.

# #Type casting -> converting one data type to another data type
# from collections import abc
# from operator import index
# from typing import List


# age= 20
# age=str(age) #converting integer to string
# print(type(age))
# print("My age is" +age)

# #Type casting provides built in functions.
# abc()
# int()
# float()
# str()

# List()#List
# tuple()#Tuple
# set()#Set
# dict()#Dictionary

#These are the built in functions that are used to convert one data type to another data type.

#LIST:
#It is a collection of data that have following features:

#1. List can have one, multiple or no data.
#Ex: abc:[1]
#    abc:[1,2,3,4]
#    abc:[]

#2.List uses square,big brackets.
#Ex: abc:[]

#3.List will be ordered.
# Ex: abc:[10,20,30,40] #The order of the data will be maintained.
#     abc:[1,2,3,4,5,6,7,8,9,10]
#     abc:[90,80,70,60,50]

# 4.Elements/ data / values of list are changable.(mutable)

# 5.Duplicate datas are allowed in the list.
# Ex: abc:[1,2,3,4,5,5,1,1]

# 6.List allows same data type or different data types.
# Ex: abc:[1, "apple" , True, 50.12]

#Creating a list:
# a. always declare a variable name for list.
# b. always put elements in square braces.
# Ex: abc=[1,2,3,4,5]
#     abc=["apple", "banana", "mango"]
#     abc=[1, "apple", True, 50.12]

#Indexing in list:
#abc=["Hello", False, 48, 101.35]
#index always starts from 0 in python.
# index[1] =False
# index[2] =48
# index[3] =101.35
# index[0] ="Hello"

# abc =["Hello", False, 48, 101.35]
#we can also acces the elements form right side.
# index[-1] =101.35
# index[-2] =48
# index[-3] =False
# index[-4] ="Hello"
# Ex: print(abc[-3]) #False

# abc[6]#accessing the index [6]of the list.
# abc= [6]# creating a list with one data[6].

#Changing the values of list:
# superheroes=['Ironman', 'Spiderman', 'Hulk']
# superheroes[2]="Thor" #changing the value of index[2] from "Hulk" to "Thor"
# print(superheroes)

#List slicing:
# print(superheroes[0:2])#it will print the values form index[0]to index[1]and not include the value of index[2].
# print(superheroes[0::])#This means it will print the values from index[0]to the last index of the list.
# print(superheroes[::2])#This means it will print the values from index[0]to the last index of the list with a step of 2.
                       
 #Methods of list:
 #1.List append() method:
# num1 = [10,20,30,40]
# num1.append(50) #[10, 20, 30, 40, 50]# here 50 will be added as a single element in the list.
# num1.append([80,90])#[10, 20, 30, 40, 50, [80, 90]] here 89 & 90 will be added as a single element in the list.(Nested list)
# print(num1)
# append() = adds one items at the end of the list.

# 2.Extend() method:
#Adds multiple elements to the list.
# num2=[10,20,30,40]
# num2.extend([80,90])
# print(num2)#[10, 20, 30, 40, 80, 90] 
# print(num2.extend([100,110]))# cannot use extend() method inside print() function because it will return None.


#Insert() method:
#Inserts or add the items at the specific position inside a list.
abc=[1,2,3,4,5,6,7,8,9,]
abc.insert(3,0)#abc,insert[3,0] means it will insert the value 0 at index[3] and shift the other values to the right.
print(abc)
abc.insert(6,85)
print(abc)

#remove() method:
abc.remove(0) #abc.remove(0) means it will remove the value 0 from the list.
print(abc)#[1, 2, 3, 4, 5, 6, 7, 8, 9]
abc.insert(0,0)
abc.insert(1,0)
print(abc)#[0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
abc.remove(0) #abc.remove(0) means it will remove the first occurrence of the value 0 from the list.
print(abc)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Pop() method:
#remove an element/item by using its index position.
abc.pop(6) #abc.pop(index)
print(abc)#[0, 1, 2, 3, 4, 5, 7, 8, 9]#it will remove the value at index[6] which is 6.

#clear() method:
#It will remove all the elements from the list.
abc.clear()
print(abc) #[] it will print an empty list because all the elements have been removed from the list.

#index,count,len(),sum,min,max,sort,reverse,copy,del ---> study these methods in the list.
