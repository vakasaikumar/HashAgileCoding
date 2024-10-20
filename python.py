arry = [5, 5, 5, 2, 5, 3, 5, 4]

increase = 0
check = None
for i in range(len(arry)):
    count = 0  
    for j in range(len(arry)):
        if arry[i] == arry[j]:
            count += 1
            
    if count > increase:
        increase = count
        check = arry[i]

if increase > 0:
    print(check)  
else:
    print("No majority element found.")




''' 
//palindrome
using boolean
name = 'abcb'
length = len(name)
n = length//2
valid = True
for i in range(n):
    l=name[i]
    r=name[length-1-i]
    if l !=r:
        valid = False
        
if valid:
    print('palindrome')
else:print('not a plandrome')
name ='mom'
if name == name[::-1]:
    print(name+' palindrome')
else:
    print(name+' not a palindrome')
    
name ='mom'
rev=''
for char in name:
    rev = char + rev 
if rev == name:print('palindrome')
else:print('not a palindrome')
//reverse 
name = 'abcd'
ans = name[::-1]  # This slices the string in reverse order
print(ans)

name ='abcd'
ans =""
for i in name:
    ans = i+ans
print(ans)

n=100
count=0
for i in range(1,n+1):
    if i %15 ==0:
        print(i)
        count += 1
print('even '+str(count))
//6
li = [10,20,30,40,50,60]
add =0
for i in li:
    if i%2==0 and i%6==:
        add += 1
print(add)
//2
li = [1,2,3,4,5,6,7,8,9]
count = 0
for i in li:
    if i%2 ==0:
        count +=1
print(count)
//4
li = [10,20,10,30,10,20,10]
count = 0 
for i in li:
    if i == 10:
        count += 1ṇ
print(count)
//4
'''