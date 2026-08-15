'''
List,TUPLES...
#List-->Mutable,ordered,hetrogenous
#index(),count(),copy(),sort(),reverse()
details=['codegnan',7,8,'hyf']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,23,45,23])
print(details.index(23))
print(details.index(23,6))
print(details.count(23))

#copy()-->shallow copymof the givrn  collection
d=['codegnan',7,8,'hyd']
new=d.copy()
print(new)
print(type(new))
print(len(d))

new[2]='sangamesh'
print(new)
print(d)

d.append('sanga')
print(d)
print(new)

d.extend('code')

data=[1,24,[3,45,56],46]
print(data)
new=data.copy()
print(new)

new[2][2]='agents'
print(new)
print(data)

new[1]='python'
print(new)
print(data)

marks=[14,24,-45,27,35]
print(marks)
print(marks.sort())#-->return none
print(marks)#return in ascending order
marks.sort(reverse=True)# return in descending order...
print(marks)
marks.insert(2,'code')
#marks.sort()
#reverse()-->return in reverse order 
marks.reverse()
print(marks)
print(marks[::-1])

print(sorted('sangam')) #return list in ascending order
print(sorted(['code','23',34,56])) # raose error


#Tuples --> tuples are also indexed,ordered,heterogenous,immutable collection
#dimensions,coordinates,database records,we prefer() for tuple notation
a=()
print(type(a))
print(len(a))

b=1.3,34,4
print(b)
print(type(b))

#Operations-->Indexing,slicing,striding,membership,merging,repetition

courses=('pfs','jfs',('da','ds'),'agenticai',34,[234,23,54])
print(courses[3][-2:-1])
print(courses)
print(len(courses))
#courses[2]=23 tuples are immutable
courses[-1].append('codegnan')# we can make any modification inside list
print(courses)
courses[-1].insert(1,'codegnan')
print(courses)

# create a nested tuple as above and work on slicing ,striding and list function
print('pfs' in courses)
d=courses*2
print(d)
e=courses + (2,3,4,5)
print(e)


e=courses + {2,3,4,5}
print(e)

'''
#tuples immutable --> count(),index()

courses=('pfs','jfs',('da','ds'),'agenticai',34,[234,23,54])
print(courses.index('agenticai'))
print(courses.count('agentt'))
#print(courses.sort()) # attribute error-->sort() is in lists not in tuples
print(sorted(courses[-1]))

#typecasting
d=tuple(sorted((23,343,45,56,)))
print(d)
d=list(sorted((-1,23,343,45,56,)))
print(d)
print('9+4')
print(eval('9+4'))
a=eval(input('Enter a list'))
print(a)
print(type(a))

#task: Take a user input as string, do this in two ways...
1)give the count of each repating chart
test case1:programming hint:count
r is repeating 2 times
' ' ' ' '  '
2)index=[1,4]
g is repeating 2 times
''''''''''














