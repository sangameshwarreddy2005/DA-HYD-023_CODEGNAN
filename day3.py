#Numeric datatype -->int,float,complex along with booean

#Input formatting -->Accepting input from the user -->input()

#Accepting integer input from user

#By default input() accepts any input -->str
#int(input()) --> will accept only integers
'''
#Float
age=float(input("Enter the age:"))
print(age)
print(type(age))

#Int
age=int(input("Enter the age:"))
print(age)
print(type(age))
'''
'''
#Str
Name=input("Enter the name:")
print(Name)
print(type(Name))
'''
'''
#Accept the group of values

a=input.split()#by default split() has space
print(a)
#space separated values
a=input.split()#now you enter spaces in output
print(a)

#comma separated values
a=input("Enter the Values: ").split(",")
print(a)
#List of Integer(map,list)
#Map
marks=map(int,input("Enter the marks:").split(','))
print(marks)

#List
marks=list(map(int,input("Enter the marks:").split(',')))
print(marks)

#Now we want to accept 2 values from user
age,salary= map(int,input("Enter the values:").split(','))
print(age)
print(salary)

#single input-->int(input())
#two inputs-->a,b=map(int,input().split(',')
#any number result as list -->a=list(map(int,input().split(',')))

marks=list(map(float,input("Enter the marks:").split(',')))
print(marks)

age,salary= map(float,input("Enter the values:").split(','))
print(age)
print(salary)
# Accepting input from user -->int,float ->input formating
#operators -->OPertors perform operation betweeen values (opeanda)
#7 types -->arithamatic,assingment,comparision(Relationship)
#membership,identity,logical,bitwise
#arithamatic operations
#+,-,*,/,//,%,**
print(5+3)
print(5-3)
print(5*3)
print(5/3)
print(5//3)#floor division -->return quotient
print(5%3)#modulus -->divisiable rules ->return remainder
print(4**2)#power (exponential)

l=int(input("Enetr the Length:"))
b=int(input("Enter the Breadth:"))
area=l*b
print("The area of Recatngle is:",area)

#Assignment operators -->assign the Values
#=,+=,-=
a=45
print(a)
#update the values of a
a+=5 #a+=5
print(a)

b=35
b+=a
print(b)

b-=5
print(b)
#Task:*=,/=,//=,**=


#Comparision Operators -->we compare the values -->boolean
#==(equal to),!=(not equal to),<(less Than),(greater Than)
#<=(less than equal to)>=(greater than equal to)
age=25
print(age==25)#return the boolean output

age=23
print(age != 12)

age=34
print(age>35)

age=26
print(age<25)

age=39
print(age >= 34)
age =34
print(age <=45)

#membership operators -->in,not in
#it check for the existance of an object in a collection
marks=[23,34,45,56]
print(19 in marks)
print(19 in 204)
print(25 not in marks)

#logical operators --> logical decision making -->and,or,not
#and -->all condition to be satisfied
#or --> any one condition to be satisified

a=(25 in [23,34,56])and 45<56
print(a)
b=45>56 or 25<=45
print(b)
c=not(True)
print(c)
'''
#Identity operators --> check for the identity of an object -->id()
#is,is not
a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c=a
print(id(c))
print(c is a)

























