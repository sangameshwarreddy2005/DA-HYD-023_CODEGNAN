#SET AND FROZENSET
#set--> set is unique collection of oblects,unordered,mutable,hashing,unindexed,heterogenous
#set(),{}
#a={} is an empty dictionary
'''
a=set()
print(type(a))
s_id={123,2334,45,567,45}
print(s_id)
print(type(s_id))
print(len(s_id))
#print(s_id[2])-->Typeeror
print(2334 in s_id)
#print(s_id */+ 2)#type error two sets can not be merge ite carrry unique elements

#data={45,67,34,68,[1,4,6,7],'sangam'}
#print(data)-->TypeError: unhashable type: 'list' no list inside the set(hashig techniques)lists are mutable
data={45,67,34,68,(1,4,6,7),'sangam'}
print(data)
print(len(data))
for i in data:
    print(i)
'''
#Methods on sets -->add(),update(),remove(),discard(),pop()
name={'sangam','arvand','sai','adfqf'}
print(name)
#name.add('sofk')
#name.add('sofl','afek')-->: set.add() takes exactly one argument (2 given)
#print(name)
#name.add(['sofk','rfmk'])-->TypeError: unhashable type: 'list'
#name.add(('sai','rfmk'))# in this u should add the data unique
#print(name)
#Update() we can update multiple elements (set)
#names={'sai','afweefw','qifw'}
#print(names)
'''
print(len(names))
name.update(names)
print(name)
print(len(name))
names.update(name)
print(len(names))
namprint(names)

#remove(),discard(),pop(),clear()
#remove() removes an elemnt from the set (it must be a member)
name.remove('sai')
print(name)
#name.remove('sai')
#print(name)-->KeyError: 'sai' if you already remove it show the keyerroe
name.discard('sangam')
print(name)

name.pop()
print(name)
print(name.pop())#removes and return an arbritary element
print(name)
name.clear()
print(name)
name.add('sairam')
print(name)

name.update(['san','gam'])
print(name)

s=name.copy()
print(s)
s.update(('python','samvf '))
print(s)
'''
#Mathematical opeations --> union(),intersection(),difference(),symmetric()
#issubset(),issuperset(),isdisjoint()
da_1={12,34,56,67,76,12}
da_2={12,56,34,78}
'''
event=da_1.union(da_2)
print(event)
print(len(event))
com=da_1.intersection(da_2)
print(com)
print(len(com))#intersection(|)(#&) and union(&)


com=da_1.intersection_update(da_2)
print(com)
print(da_1)
'''
#difference() #removes common elements and print remaning elements from the first set
'''
diff=da_1.difference(da_2)
print(diff)
f=da_1 - da_2
print(f)

sym=da_1.symmetric_difference(da_2)
print(sym)
h=da_1^da_2
print(h)
'''
da_2.remove(78)


print(da_2.issubset(da_1))
print(da_1.issuperset(da_2))

#isdisjoint() return false for sets having common elements
print(da_1.isdisjoint(da_2))



















