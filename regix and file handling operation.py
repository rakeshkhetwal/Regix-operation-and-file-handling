
#program for count no col by two methods


data=open(r'C:\Users\RAKESH KHETWAL\Desktop\bro.txt','r')
c=0
for row in data.readlines():
    col=row.split(',')
    c=len(col)   
    
print(c)
data.close()

data=open(r'C:\Users\RAKESH KHETWAL\Desktop\bro.txt','r')
x=0
for row in data.readlines():
    x=x+1

print(x)
data.close()

data=open(r'C:\Users\RAKESH KHETWAL\Desktop\bro.txt','r')
cc=0
for row in data.readlines():
    for col in row.split(','):
        cc=cc+1

print(cc/x)
data.close()


#list of rows with only digits 

data=open(r'C:\Users\RAKESH KHETWAL\Desktop\bro.txt','r')
import re

for row in data.readlines():
    row=row.replace(",",'')
    
    matchs=re.match(r'^(\d)*$',row,re.M)
    if matchs:
        print("with digit",row)
    else:
        print("sorry bro")

data.close()

#list of columns with only digits
#DOubt

data=open(r'C:\Users\RAKESH KHETWAL\Desktop\bro.txt','r')
import re
print("columns with digits")
for row in data.readlines():
    col=row.split(',')
    l=len(col)
    maaachoman=re.match(r'^(\d)$',col[1],re.M)
    if maaachoman:
        print("with diits ",col[1])
    else:
        print("sooorrry")
data.close()


#: WAP to input roll number, name and marks of a student in 5 subjects and calculate the total and average marks. Display all the values.

marks=[]


for x in range(0,5):
    y=int(input("enter marks"))
    marks.append(y)
    
sum=0

for x in range(0,len(marks)):
    sum=sum+marks[x]


print("sum of marks :",sum)
print("average :",sum/5)

    
    
        
































