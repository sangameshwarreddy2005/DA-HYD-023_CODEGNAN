strings-->caseconversion,searching & and finding,string testing methods,replace,space removal

#searching,finding ,replacing,joining...
a='Sangameshwarreddy'
print(len(a))
print(min(a))
print(max(a))

a='Sangameshwarreddy'
b=a.index('S')#its return the index position
print(b)
c=a.index('a')# its return the only the first occurence
print(c)
d=a.index('a',5)#its return the next occurence
print(d)
e=a.index('a',25)#valueerror
print(e)
f=a.index('x')#value error
print(f)

#rindex()--> return the occurence
a='Sangameshwarreddy'
b=a.rindex('a')# here 'a' is accuring at 10 index
print(b)
c=a.rindex('a',10)# here 'a' is accuring at 10 index
print(c)

#Count()-->retuns the numbers of items object is repeating
print('code'.count('c'))
print('code'.count('w'))#it return a as we dont have 'w' in 'code'
print('sangameshwar'.count('a'))

#Find()-->first occurence but it avoid error returns -1 if substring is not found
print('sangameshwar'.find('z'))# it return -1
print('sangameshwar'.find('a'))# find give the 1st occurence in the position
print('sangameshwat'.rfind('a'))

a='SangameshwarReddy'
print(len(a))
for i in a:
    #print(a.count(i))
    print(a.count(i),a.index(i))

#Replacing,splitting,Joining
a='Sangameshwar'
print(a.replace('a','A'))
print(a)
a=a.replace('a','A')
print(a)
print('ryrdysjbwigrgqoi#asd#s'.replace('#',''))
print(a.replace('g','reddy'))

#Split
a='sanga mesh war'
print(len(a))
b=a.split()# (by default if we have space it splits (return list)
print(b)
print(len(b))
c='sang,ames,shwar'
d=c.split()
print(d)
e=c.split(',')
#print(len(e))
print(e)
print(len(e))

#Join(iterable)-->concatenate any number of strings
a='sanga'
b='mesh'
print(a.join(b))
print('#'.join(a))

#String testing methods (booleans)
#isalpha(),isalnum(),isdigit(),isupper(),islower()...
a='sangam123'
print(a.isalnum())#return true for alphanumeric string else false
b='sangam'
c='123'
print(b.isalnum())
print(a.isalpha())#return true only for alphabets
print(a.isdigit())
print(c.isdigit())
print('123'.isdigit())
print('123'.isnumeric())#tis has upper edge(num,fraction,romans)

#start with()-->how its starting
print('sanga'.startswith('s'))
print('sanga'.startswith('a',1))
print('sanga'.endswith('a'))#endswith --> how its ending

print('sangam'.islower())#return the true for all lower case
print('Samgam'.isupper())#return the true for all upper case
print('Sangamesh Reddy'.istitle())#return the true for title start with capital litter 


#Space removal -->strip()(removes leading and trailing space)
a=' sanagam '
print(a.strip())
c=input('enter the name:').strip().lower()
print(c)

#zfill() filling with zeros as per the given numeric string
print('563'.zfill(4))
print('123'.zfill(9))
#center(),ljust(),rjust()-->alignment of strings (check length and then modify the width accordingly)
print('sangam'.center(9,'$'))
print('san'.rjust(4,'$'))
