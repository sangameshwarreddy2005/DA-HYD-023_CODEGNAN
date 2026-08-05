#sequences-->strings,lists,tuples,mapping(dict)
#string -->group of char,we use singlr or double or triple quotes
#for represention of strings...
#string are immutable,ordered,indexed collection

name="codegnan"
print(name)
print(type(name))
print(len(name))#len-->returns the number of items in container

#index-->is used to fetch the object(position) start at 0 and ends at len(obj)-1
# we use [] representation
#print(name[4])
#print(name[25])#index error-->out of range
name='codegnan'
#-ve indexing-->-1 to len(obj)
#-ve start with -1/+ve start with the 0
print(name[-4])
print(name[-33])

#Slicing-->we can access group of char's(obj)
#we use [srt:end] strt default-->0,start is included,end is exclude

name='sangamesh'

print(name[:])#return the entire the string
print(name[0:])#''   ''    ''
print(name[:6])#starting with the 0th position and end with the 6th index
print(name[1:7])#starting index 1with the 0th position and end with the 7th index
print(name[:9])

print(name[7:3])#returns empty as strings are immutable
#slicing is applicable from lower index to higher index
print(name[:15])#return till end of the string
print(name[45:])

name='python'
print(name[4:6])
print(name[4:])
print(name[-2:])
print(name[2:-6])
print(name[1:-2])

#observe +ve,+ve,-ve,-ve,+ve,-ve all possibilies
#striding-->[strt:end:step]
course="DataAnalysis"
print(len(course))
print(course[:4])
print(course[4:])
print(course[-3:])
print(course[::1])
print(course[::2])
print(course[1:6:3])
print(course[2::3])
print(course[::-1])#it returns of the reverse of them string
print(course[::])
#task:workout with all possibilites of slicing and striding on a example
name='codegnan'

#name[3]='w' #strings are immutable
#operation on strings-->indexing,concatenation,repetition
print(name*3)
print('*'*25)
#concatenation-->combining strings
data='sai'+'pyt'+' '+'daa'
print(data)
print('123'*2)
print('code' in 'codegnan')

for i in 'codegnan':
    print(i)

for i in 'codegnan':
    print(i,end='')
name='sangamesh'

#built in functions-->len(),min(),max(),sorted()
name='Sangameshz1 $'
print(len(name))
print(min(name))
print(max(name))
print(ord('B'))#alphabetical order ascii ordering
print(ord('g'))
print(sorted(name))#return the list by sorting the all elements
print(chr(65))

#Methods on strings -->case-conversitions,finding/serching...
name='Sangamesh reddy'
print(name.upper())
print(name.lower())
#capitalize()-->convert the 1 letter to uppercase
print(name.capitalize())
print(name.title())

#task:A to Z
#use loops and strings to return A-Z




















