#Lists--> collection of heterogenous elements(item)
#list-->Indexed,ordered,mutable,Hetrogenous,we use [] to store the data

marks=[35,23,45,67,90]
print(marks)
print(len(marks))
print(type(marks))
print(23 in marks)
#Operations:Indexing,slicing,striding,Membership,Merging,Repetition

#Nested lists--> A list inside another list

names=['codegnan',25,35.8,[1,2,3,4],'da23',90,67]
print(names)

print(len(names))
print(names[0])
print(names[0][:4])
print(names[0][4:])
print(names[0][::2])
names[0]=names[0][::-1]
print(names)

print(names[3])
print(len(names[3]))
print(names[3][2])

#indexing,slicing-->mutable

names[2]='python'
print(names)

#by 
names[6]=['san','gam',2,434,34.6]
print(names)
print(len(names))

names=['codegnan',25,35.8,[1,2,3,4],'da23',90,['cpdegnan',23,56,78]]
print(names[6][0][4:])
names[2:4]='sanga','reddy','qefvq'
print(names)

#in slicing whatever elements u pass as per the logic length keeps on increase
#names=['codegnan', 25, 'sanga', 'reddy', 'qefvq', 'da23', 90, ['cpdegnan', 23, 56, 78]]

names[3:6:2]='python','java'
print(names)

#create a neasted list with strings,lists and work on the indixing slicing striding added advantage if u could
#add string functions also it
#lists functions -->append(),insert(),extend(),pop(),remove(),clear()
#index(),count(),copy(),sort(),reverse()
name=['sangamesh','reddy']
name.append('bandari')
print(name)
#names.append(analysis,data)-->type error
name.append(['analysis','agent'])
print(name)
#append() will alawys increment the length of list by 1
print(name[3])
name[3].append('chatgpt')
print(name[3].append('chatgpt'))#its return none as append is applicable on the list not print
print(name)

#Extend()-->inserts multiple elements to the end of the list
#name.extend('analysis')
#print(name)
name.extend(['analysis'])
print(name)
name.extend([1,2,3])
print(name)
name.extend(1,2,3)#Type error
print(name)
'''
#Insert
name=['sangamesh','reddy',2,4]
'''
name.insert(1,'bandari')
print(name)
name.insert(0,'reddy')
print(name)
#names.insert([1:4],'a','b','c'])#syntax error
name.insert(-3,'data')
print(name)
'''
#pop(),remove(),clear()
#pop()by default last,else given index
'''
print(name.pop())
print(name)
'''
name.pop(2)
print(name)
# remove () we can specific value
name.extend([23,234,45])
print(name)
name.remove(234)
print(name)
#delete
del name[1:3]
print(name)

name.clear()#clear() will remove all elemnets and return empty list
print(name)
#task data=['codegnan','saketh','python','java']
#output:
'''
0:codegnan
1:saketh
' ' '
' ' '
'''










