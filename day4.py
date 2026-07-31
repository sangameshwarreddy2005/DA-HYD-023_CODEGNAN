#identyity operaton

#Bitwise Operation --> we perform bitwise operations over operands
#& and, (^) xor,(|) or,shifting (<<>>)
#& -->0 0-0,1 1-1,1 0-0,0 1-0
#|-->1 1-1,0 0-0,1 0-1,0 1-0
#^-->both should not be same like 1 1-0,1 0-1
#Number will be converted into binary format
'''
print(6&19)#both 5 and 3 to be converted binary and bitwise and is performed

print(5|20)# bitwise or

print(5^20)#bitwise xor
print(5 and 3)# here and is logical operator check for both existances
#return 5 in the above case
print(5 or 3)#return 3 in this case

# leftshift operator <<,rigth shift operator >>
print(5<1)
print(5<<3)# shifting the left side at one position
print(5>>2)# shifting the right side at one position

'''
'''
print(15<<2)
print(15>>2)
#Input formating -->input(),int(input()),float(input())
#you know -->single input
#2 or 3 inputs-->map()
#group of integers -->list(map(int,input().split(',')))
names=input("Enter a names:").split(",")
print(names)

name1,name2=map(str,input('enter the names:').split(','))
print(name1,name2)

#Tokens-->Numeric Datatypes-->operations -->floe of the rogram
#control block statements
#conditional statements -->if,else,elif
#Repetition statement (loop)-->for,while

#Conditional statements--> if usage

syantax:
if<condition>:
   statement(s)...
   .....

age=int(input("Enter the age: "))
if age>=18:
    print("Your age is:",age)

age=int(input("Enter the age: "))
if age>=18 and age in[19,20,21]:
    print("Your age is:",age)
print(age)

#else keyword-->if else
#else:
    #statement(s)..
if else usage below:
if<condition>:
    statement(s)...
    ...
else:
    statement(s)....
    ...

#voter eligability
age=int(input("Enter the age:"))
if age>=18:
    print("You are eligiable:",age)
    print("access granted")
else:
    age=18-age 
    print("you need to wait more:",age,"years")
'''
#same
if age>0:
    age1=int(input("Enter the age:"))
    if age>=18:
        print("You are eligiable:",age1)
        print("access granted")
    else:
            age=18-age
            print("you need to wait more:",age1,"years")
else:
    print("you have enter the -ve values enter only +ve")

 
#task:student maeks and grade analyzer
'''
 90-100-->A
    80-89-->B
    70-70-->c
    60-69-->D
    >60-->fail
    '''
#also -ve cases should not be alloewd and marks shouldnt be greater 100




