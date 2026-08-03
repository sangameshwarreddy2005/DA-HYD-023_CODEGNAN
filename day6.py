'''
controal statements --> flow of execution of the program
                    -->Condition statements -->if,elif,else...
                    -->Repetition statements(Loops)-->for,while(for with else)(while with else)
                    -->Jumping statements-->break,continue,pass
                    '''
#Loops -->loops are helpful for repetation(Automation tasks)
#for keyword will be helpful to iterate over a sequence/range
#syntax for(for keyword):
'''
for <temp_var> in sequence/range:
    statement(s)...
    ....

#range (stop)-->default 0 ends at stop -1
#range(start,stop,step)
#by default range picks 0 as start value
for i in range(10):
    print(i)
    
#In above case we got 10 iterations
# start,stop
for i in range (1,8):
    #if i>5:
        #print(f'value of i is -->',(i))
    if i>5 and i%2==0:
        print(f'fainal value is:',(i))# print(f'fainal value is:{i}')

#range(start,stop,step)-->here step --interval
for i in range(2,10,2):
    print(i)
    print("done")
for i in range(1,10,2):
    print(i)
    print("done")
for i in range(1,10,3):
    print(i)

for i in range(-10,0,1):
    print(i)


#[]-->we generally Lists
names=['sangamesh','pranay','sai']
for i in names:
    print(f'student name is:',(i))# print(f'student name is:{i}')

names=['sangamesh','pranay','sai']
print(len(names))#len(obj)-->returns the number of items in a container
for name in names:
    #print(f'student name is:',(name))# print(f'student name is:{i}')
    if name=='sai':
        print(f'student name is {name}')
        
#Task:calculate the sum of first 10 numbers
result=0
for i in range(1,11):
    #print(i)
    #print(f'result is {i+i}')
    result=result+i
    print(result)
print(f'sum of 10 numbers is {result}')
  
result=0
for i in range(21):
    if i%2==0:
        result=result+i#result +=i
        #print(result)
print(f'the sum of first 10 even numbers is:',(result))
'''
#Understand the loops usage with fitness streak example
#work_out=1,work out missed=0
work_log=[0,1,1,1,0,1,0]
longest_streak=0#Target variable
current_streak=0
for day in work_log:
    if day==1:
        current_streak=current_streak+1
        if current_streak>longest_streak:
            longest_streak=current_streak
            #print(longest_streak)
    else:
        current_streak=0#streak breaks
            
print(longest_streak)
