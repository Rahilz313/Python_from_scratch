print('sjkglhsughs')

def test():
    pass

def test1():
    print('this is my first funciton')
test1()

a = test1()
a+'sudh'
# Above It is giving error as Nonetype as we are trying to concacenate two string

def test2():
    return 'This is my first funciton'

test2()+'rahil' ####### Now it is working

def test3():
    return 233353
type(test3())

def test():
    pass
def test1():
    print('this is my first function')
    
test1()

a = test1()
a
type(a)
type(test1())
a = test1()
str(a)

def test2():
    return 'this is my first function'
test2()
test2() + 'rahil'

def test3():
    return 23242

type(test3())

def test4():
    return 4,5,'rahil', [1,2,3,4,5]

b= test4()
type(test4())
b[0]
test4()
a = 1
b = 5
c = 'rah'
d = [12,3]
a, b,c, d =  34, 45, 'rahil','sdfsfs'
test4()
x,y,c,z = test4()
x
y
c
d
def test5():
    a = 6*7 / 6   
    return int(a)
a

len('sdhfkshuf')
l = [3,4,5,3,3,2,4, 'rahil', [12,5,3,4,2]]


def test6(a):
    k = []
    if type(a)==list:
        for i in a:
            if type(i) == int:
                k.append(i)
            elif type(i) == list:
                for j in i:
                    if type(j)==int:
                        k.append(j)
    return k           
test6(l)    
test6('dsfs')
test6()
test6([['djfsjfoisf'],343434,3,23,[1,2,3]])

def test8(c):
    if type(c) == dict:
        return c.keys()
    else: 
        return 'you have not passed a dictionary'
test8({'key1':23244, 'key2': 'dfsfdsf'})

a={'key1':23244, 'key2': 'dfsfdsf'}
for i in a:
    print(i)
test8('dsfjksjf')

def test9(a,b):
    if type(a)==list and type(b)==list:
        a.extend(b)
        return a
    else:
        return 'either of your data is not a list'
a,b = ['rahil', 'shaikh'], [3,23,2,'skfdlskf']
test9(a,b)
a       
def star():
    for i in range(len(0,5)):
        print(i)
def star(c):
    '''this is a function which will help you to create a triangle'''
    for i in range(0,c):
        for j in range(0+i+1):
            print('*', end=' ')
        print('\r')

star(10)
help(star)
#########
'''
Q1. Write a function which will take string and return a len of it without using built in function len
Q2. write a function which will be able to print an index of all premitive elements which will pass
Q3. write a function which will take input as a dict and give me output as a list of all the values
Q4. write a function which will be take input as dict and give output as list of all the values even in case of 2 level nesting it should work.
Q5. write a function which will take a list as input as a input and give me concatnation of all the elements as and output
Q6. write a function whcich will be able to take a list as input return an index of each element like inbuilt index function but even if we have repetetive element it should return index
Q7. write a function which would return a list of all the file name from a directory
Q8. write a function which will be able to show your system configuration
Q9. write a function which will be able tot show date and time 
Q10. write a function which will be able to read a image file and show it to you
Q11. write a function which will be able to read video file and play for you.
Q12. write a function which will be ale to shutdown your system
Q13. write a function which will be able to access your mail
Q14. write a function which can move one file from directory to another directory.
Q15. write a function by which i can send a mail to anytone 
Q16. write a function to read a complte pdf file
Q17. write a function to read a word file
Q18. write a functin which can help to filter only word file from a directory
Q19. write a function by which you can print an ip adderess on your system
20l. write a function which will be able to append two pdf files
'''

