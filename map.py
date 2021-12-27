#Write a Python program to triple all numbers of a given list of integers. Use Python map.
"""a = (1,2,3,4,5,6,7,8)
b = map(lambda x:x+x+x,a)
print(list(b))

#multiplication
z = (12,24,36,48,60,72,84,96)
y = map(lambda x:x*x*x,z)
print(list(y))

#dividation
z = (12,24,36,48,60,72,84,96)
y = map(lambda x:x/x/x,z)
print(set(y))

#Write a Python program to add three given lists using Python map and lambda.
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
print(a)
print(b)
print(c)
d = map(lambda x,y,z:x+y+z,a,b,c)
print(list(d))

x = [25,50,75]
y = [100,125,150]
z = [175,200,225]
print(x)
print(y)
print(z)
a = map(lambda x,y,z:x+y+z,x,y,z)
print(list(a))

#Write a Python program to listify the list of given strings individually using Python map.
a = ['red','blue','green','black']
print(a)
b = list(map(list,a))
print(list(b))

x = ['nilesh','ajay','nawaj','vijay']
print(x)
y = list(map(list,x))
print(y)

#Write a Python program to Multiply three given lists using Python map and lambda.
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = [11,12,13,14,15]
d = map(lambda x,y,z:x*y*z , a,b,c)
print(list(d))

#Write a Python program to divide three given lists using Python map and lambda.
a = [4,6,8,10]
b = [12,14,16,18]
c = [22,24,26,28]
d = map(lambda x,y,z:x/y/z,a,b,c)
print(list(d))

#Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
a = [10,20,30,40,50,60,70,80,90,100]
b = [1,2,3,4,5,6,7,8,9,10]
c = list(map(pow,a,b))
print(c)

#Write a Python program to square the elements of a list using map() function.
a = [2,4,6,8]
print(a)
b = map(lambda x:x**2,a)
print(list(b))

#Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function.
def case_changes(s):
    return str(s).upper(),str(s).lower()
a = {'a','b','c','d','a','e','f','a'}
print(a)
b = map(case_changes,a)
print(set(b))
def case_changes(s):
    return str(s).upper(),str(s).lower()
a = {'a','b','c','d','e','f','a','b'}
print(a)
b = map(case_changes,a)
print(set(b))
"""
a ='1,2,3,4'
print(a)
a = [10,20,30,40,50]
print(a)
a.append(100)
print (a.append(100))

