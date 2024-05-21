s = 'rahil' # string object is iterable, only iterable objects can be converted into iterator
next(s) # first checking whether it is iterator or not, if not a iterator then will convert it into iterator 
s = iter(s) # converting iterable object to iterator
next(s) # here it is working now with next element, as above it was not working and giving error saying object is not iterator
next(s)
next(s)
next(s)
next(s)
next(s)
next(s)
a = 56 
next(a) # here it is giving error stating that int object is not iterator
a = iter(a) # ere it is giving error as int object is not iterable. so we know that the object which are not iterable cannot be converted into iterator

t = (5,6,7,8,9)
next(t)
t = iter(t)
next(t)

r = range(6)
next(r)
r = iter(r)
next(r)

tuple(range(0,45,3))


###### Creating a function to generate cube numbers till the number is given in the argument
def cube(n):
    j=[]
    for i in range(n):
        j.append(i**3)
    return j
        
        
cube(60) # here when i take big numbers it is taking too much memory and giving the output only when its completed.

# here creating a function which will give cube only of a given number
def cube1(n):
    return n**3
    
cube1(4) 

    

def cube(n):
    j=[]
    for i in range(n):
        j.append(i**3)
    return j
        
        
cube(60) # here when i take big numbers it is taking too much memory and giving the output only when its completed.

for i in range(50):
    print(i)
    
def fib(n):
    a =1
    b=1
    for i in range(n):
        yield a,i
        a,b = b , a+b

for i in fib(10):
    print(i)
    
def fib(n):
    a = 1
    b = 1   
    for i in range(n):
        yield a,i
        a,b = b , a+b
        
for i in fib(10):
    print(i)

def fib1(n):
    a = 1
    b = 1
    k=[]
    for i in range(n):
        k.append(a)
        a,b = b  , a+b
    return k

fib1(12)