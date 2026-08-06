#q1)to calculate the ecommerce retails add  cart price total sum 
'''
price=list(map(int,input("Enter the cost:").split(',')))
sum=0
for i in price:
    sum=sum+i
    #print(sum)
print(sum)
'''
#q2)write the python progrram to analyze the how many upper case, lower case,special chart
'''
password = input()

upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

for i in password:
    if i.isupper():
        upper_count += 1
    elif i.islower():
        lower_count += 1
    elif i.isdigit():
        digit_count += 1
    else:
        special_count += 1

print("Upper:", upper_count)
print("Lower:", lower_count)
print("Digit:", digit_count)
print("Special:", special_count)

passward=input()
upper=lower=digit=special=0
for i in passward:
    if 'A'<=i<='Z':
        upper+=1
    elif 'a'<=i<='z':
        lower+=1
    elif '0'<=i<='9':
        digit+=1
    else:
        special+=1
print("Upper:", upper)
print("Lower:", lower)
print("Digit:", digit)
print("Special:", special)
'''
#write a python program to extract the email from @
email = input("Enter the email: ").split()
for mail  in email:
        print(mail.split('@')[1])

























        

