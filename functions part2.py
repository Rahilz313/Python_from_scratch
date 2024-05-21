# now for eg in function there are multiple arguments we have to take in function.
# we may write function like below. eg if there are 5 argumnets it needs to take
def test(a,b,c,d,e):
    return a,b,c,d,e
# so i can call and get function here
test(22,43,23,'sdf','fdsf')

#But the Above arguments are fixed that only 5 arguments will come, but what if we dont know how many arguments will come?
# in that situation we use *args, it means we are trying to pass n no of argumnets
 def test1(*args):
     return(args)
# here we are able to pass n no of arguments without hardcoding
test1(45,32,22)

test1('rahil', 'shiakh', 12324, ['dfjskjf',3874983])

test1('rhail', 'shaikh', [2,3,4,5])

#here args just a standard name not a reserved keyword, we can give my name your name etc *rahil, *shaikh, *abc anything

def test2(*rahil):
    return rahil
test2('fdjksfks', 'jfksjf',2323)

def test3(*rahil, a):
    return rahil, a
test3(34,21,45,23)
test3(3,232,123,a=21)

def test4(*rahil, a,b,c,d,e):
    return rahil, a,b,c,d,e
test4(34,2,3,12,4,212,32,a='rhail',b='shaikh',c= 'jflsjfs', d=232, e= '343')

# now keeping the *argumt in last and see what happens
def test5(a, *rahil):
    return a, rahil
test5(a = 12324, 'rahil', 'shaikh', 123232) # it is giving this error SyntaxError: positional argument follows keyword argument 
                                            # even though we have difened value of a and giving n no of argumnet for *rahil
                                            # the probelm is that when we keep *args in last and give any particular variable in begining
                                            #it takes first value as the varables value, i will give eg below
                                            #def test5(a, *rahil):
                                            # here calling test5('rahil', 'shaikh', 324,342,) here bydefault first value will be assinged to 'a'
 test5('rahil', 'shaikh', 1,2,3,4,5,5)
 
 # take anything from user and return it in a list
 def test6(*args):
     return list(args)
 test6(1,2,3,4,'rhail')
 
 # now take anything from the user and if there is a list in the data only return that.
 
 def test6(*args):
     k=[]
     for i in args:
         if type(i) == list:
             k.append(i)
     return(k)
test6(1,2,3,4,{'shaikh':123}, [1,2,23,4,],[1,2,3,3,5])        

# now if we want to pass the data in key:value pair which is a n no of data like below
{'a':'b', 'rahil': 'shaikh', 23:[1234]}
# so it is possible to pass n of data like above in a function using double **keyargs again keyargs here is just a notion
def test7(**keyargs):
    return keyargs

test7(rahil='shaki', b = 12344)

def test8(**rahil):
    return rahil
test8(a=2343,b=4342,c='dsfdsf', f= [2,3,4,21,3])

def test9(**rahil):
    return rahil

test9(name=31, phone_no=9283430, mail_id='rahiljs@gmailcmfdhi',)

def test9(a, *rahil, **args):
    return a, rahil, args
test9(1,2,3,4,34,3,2,{'rahil':'shiakh'},g=79879)

def test13(a,b):
    return a*b
test13(7,5)

a = lambda a,b :a*b
a(45,25)

a = 10
def test16(c,d):
    c=5
    return c*d
test16(a,50)
test16(10,50)
c

# add 2 in each of the element in the list and then give the final list
l = [1,2,3,4,5,62,3,5,3,9]
def add2(l):
    k=[]
    for i in l:
        k.append(i+2)
    return k
    
add2(l)
# doing the same thing now using a lambda function
a= lambda a :[i+2 for i in a]

a(l)

# comprehension operation
l
[i for i in l]
[i+2 for i in l]

[(i**2, i+i)for i in l if i < 4]

d = {1:1, 2:4, 3:9}

d1 = {}
for i in range(10):
  d1[i] =i**2
  
d1

f={}
for i in range(10):
    f[i] =i**2
f

(i for i in range(10)) # it is giving this <generator object <genexpr> at 0x00000248AC9A7340> 
tuple(i for i in range(10))

#######
a = 56
for i in a:
    print(i) # it is giving this error - ""TypeError: 'int' object is not iterable""
    
s = 'rahil'
for i in s:
    print(i)    ## here we can say that string object is iterable
next(s) # now it is giving this error - ""TypeError: 'str' object is not an iterator""

# so as we saw string object is iterable but not iterator, so we need to convert it into itertor in order to access the values 1 by 1
b = iter(s) # here we have used iter function which makes the iterable obejct an iterator and then we can access the value
            # and this is how for loop works
next(b) # using next funciton we can 
type(b)

s = 'djflsjfosh' # so first of all it converts the iterable into iterator by using iter() function and then works
for i in s:
    print(i)
    
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*(n-1)
    
factorial(3)

def EvenNums(num):
    print(num)
    if num % 2 != 0:
        print('plz enter an even number')
    elif num ==2:
        return num
    else:
        return EvenNums(num-2)
EvenNums(9)    

def usd(a):
    inr = a*83
    return a, 'usd = ', inr 
usd(1)
#######wrting a function which will take a number as an input if it is even it will print even else odd
def type_num(a):
    if a % 2 != 0:
        print('this is an odd number')
    else:
        print('this is a even number')
        
type_num(44)

    #####Recursice Function
    def show(n):
        if n == 1:
            return 
        print(n)
        return show(n-1)
show(5)

def fact(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fact(n-1)
    
fact(5)

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
fact(6)

def rec(n):
    if n == 0:
        return
    else: 
        return n - rec(n) 
         

rec(5)

for i in range(1,5):
    print(i)
    if i ==3:
        break
    
    
    def rec(n):
        if n == 1 or n ==0:
            return 
        print(n)
        return rec(n-1)
    
    rec(4)
    
def rep(n):
    if n==0  :
        return
    print(n)
    return rep(n-1)
rep(9)

def fib(n):
    if n==0:
        return n
    
    return n + fib(n-1) 
fib()
       
# Nested functions
def fun(n):
    if(n>100):
        return n-10
    else:
        return fun(fun(n+11))

fun(95)