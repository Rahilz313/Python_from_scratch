#Q1. Write a function which will take string and return a len of it without using built in function len



def string(a):
    count = 0
    for i in a:
        count = count+1
    return count
        
string('rahil')

#Q2. write a function which will be able to print an index of all premitive elements which will pass
def indexes(a):
    for i in range(len(a)):
        print("Index:", i, "Character:", a[i])

# Now call the function after defining it
indexes('shaikh')


#Q3. write a function which will take input as a dict and give me output as a list of all the values

def dic(c):
    k=[]
    if type(c) == dict:
        for i in c:
            k.append(i)
        return k
dic({'key1':'value1', 'key2':'value2'})

# Q4. write a function which will be take input as dict and give output as list of all the values even in case of 2 level nesting it should work.

def dic2(a):
    l = []
    if type(a)==dict:
        for i in a:
            l.append(a[i])
            if a[i]==dict:
                for j in a[i]:
                    l.append(a[i][j])

def dic2(a):
    l = []
    if type(a) == dict:
        for i in a:
            l.append(a[i])
            if type(a[i]) == dict:
                for j in a[i]:
                    l.append(a[i][j])
    return l
dic2({'key1':'value1', 'key2':'value2','dict':{'inside':22323}})

#Q5. write a function which will take a list as input  and give me concatnation of all the elements as and output

def lis(a):
    result = ''
    if type(a) == list:
        for item in a:
            result = result + str(item)
        return result
    else:
        return 'plz provide a list'

lis('hkuhku')

#Q6. write a function whcich will be able to take a list as input return an index of each element like inbuilt index function but even if we have repetetive element it should return index
def ind(a):
    if type(a)==list:
        for i in range(len(a)):
            print(i, 'is the index value of ', a[i])
            
ind(['rahil', 'shaikh', 1,2,3, {'key':'value'}])
      
#Q7. write a function which would return a list of all the file name from a directory
k=[]
for i in pwd:
    k.append(i)            
return k


    

           