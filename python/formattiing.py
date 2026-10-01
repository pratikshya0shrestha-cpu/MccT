
#amount=1250000
#output= I have Rs.1,250,000 
Amount=1250000
print(f"I have Rs.{Amount:,}") #,=comma formatting

#Percentage fromatting
Marks=128
Total= 250
per= Marks/ Total 
#output= percentage:<>%
print(f"Percentage: {per:.2%}") #:.2%=percentage formatting

#output:
#student.      math      python
#RAM            85       90
#sita           90       80
#Anyone.        78       88

print(f"{'student.':<15}{'math':<10}{'python':<10}") #< left alignment
print(f"{'RAM':<15}{'85.':<10}{'90':<10}")
print(f"{'sita':<15}{'90.':<10}{'80':<10}")
print(f"{'Anyone.':<15}{'78.':<10}{'88  ':<10}")
                                     
#====== BUS TICKET ======
# passenger   :"Pratikshya"
# Fare        :2500
#Destination  :"Kathmandu"
#========================
passenger="Pratikshya"
Fare=2500
Destination="Kathmandu"
print(f"{'='*20} BUS TICKET {'='*20}")      
print(f"{'passenger:':<15}{passenger:<10}")
print(f"{'Fare:':<15}{Fare:<10}")
print(f"{'Destination:':<15}{Destination:<10}") 
print(f"{'='*50}")

#mathematical operations
#+ #addition
#-#subtraction
#*#multiplicatioN
#/#division(returns float value)
#//#floor division (removes decimal values)
#%#modulus(returns remainder)
#**#exponentiation(returns power of a number)






