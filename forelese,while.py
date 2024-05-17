l = ['name', 'emailid', 'phoneno', 'address']
for i in l:
    print(i+'rahil')
######################3333
# For Else
for i in l:
    print(i)
else:
    print('if for loop is going to complete itself then it will come to else ')

for i in l:
    if i =='emailid':
        break
    print(i)    
else:
    print('check this statement')

s = 'rahil'    
for i in s:
    if i == 'a':
        break
else:
    print('dont execute unless its printing my name')    
############################################################
a = 1
while a < 6:
    print(a)    
    a = a+1
##############################################3
#####3Break Statement####################################33
# It is used to break the loop based on certain conditions
a = 1
while a < 5:
    print(a)
    if a == 4:
        break
    a = a+1    
##############Continure Statement#############################
# It is used to continue the loop when certain condition is met
a = 1
while a < 5:
    print(a)    
    if a == 3:
        continue
    a = a+1
    
a = 1
while a < 5:
    print(a)
    a = a+1
    if a == 3:
        continue
#############Pass Statement############################
## Pass keyword is used just to pass when we dont want to do anything
for i in l:
    pass

while a < 10:
    pass

list(range(7))
list(range(0,21))
list(range(1,21))
list(range(0,21,3))
list(range(3,10,-3))
list(range(10,6,-1))
list(range(10,-5,-2))


##########################3
# Printing Piramid
n =5
for i in range(0,n):
    for j in range(0,i+1):
        print('*', end='')
    print('\r')    
    
t =  (3,4,5,3,2,4,5)
for i in t:
    print(i)    
for i in  t:
    print(t[::-1])
list(range(len(t), 0, -1))

for i in range(len(t), -1, -1):
    print(t[i-1])    

s = 'This is a basic python class'
len(s)

count = 0
for i in s:
    count = count +1
print(count)

for i in s:
    print(i)
    
for i in range(len(s)-1, -1, -1):
    print(s[i])
for i in range(len(s)-1, -1, -1):
    print(s[-i])
########## now printing the same using while loop##################33
s = 'ineuron'
v = 'AaEeIiOoUu'
for i in s:
    if v in s:
        print(i)

s = 'rahil'
v = 'AaEeIiOoUu'
for i in s:
    if i in v:
      print(i,'vowel')
    else:
      print(i, 'not a vowel')        
#######################Finding whether the string is palandrome or not.
s = 'eye'
for i in range(len(s)):
  
  if s[i] != s[len(s)-1-i]:
    print(s, 'is not a palandrome' )
    break
else:
  print(s, 'is a palandrome')
  
s = input()
v = s[::-1]
if s == v :
    print('palandrome', s)
else:
    print(s, 'not a palandrome')
#####################################
d = {
    'india' : "IN",
    'canada' : "CA",
    'China'  : "CH",
    'United states': "US"
}

  # Storing all the keys in a list who have more than 5 chars
k=[]
for i in d:
    if len(i) > 5:
        k.append(i, )
print(k)

# Storing all the keys in a list who have less than equal to 5 chars
f=[]
for i in d:
    if len(i)<=5:
        f.append(i)
print(f)

#both in same code 
 
f=[]
l = []
for i in d:
  if len(i)<=5:
    f.append(i)
  else:
    l.append(i)
print(f)
print(l)


d_1 = {
    "ineuron":{
        'a':14, 
        'b':10, 
        'c'=4}, 
    "Course":  {'d':45, 
     'e': 34, 
     'f':1}
}
######Finding maximum values from the dictionary###########3
k=[]
for i in d_1:
  
  for j in d_1[i]:
    k.append(d_1[i][j])
  print(max(k))
  
  
####Printing maximum int value from the dict, note - nested dict values should be considered ############

d_1 = {
    "ineuron":{
        'a':14,
        'b':10,
        'c':4},
    "Course":  {'d':45,
     'e': 34,
     'f':1},
    'g': 34, 
    'h':[45,5,4,6,7],
    'i':(45,34,2),
    'k':'rahil'
}

d_1
l = []
for i in d_1.values():
  if type(i) == int:
    l.append(i)
  elif type(i) == dict:
    for j in i:
      if type(i[j]) == int:
        l.append(i[j])
  elif type(i) == list:
    for k in i:
      if type(k) == int:
        l.append(k)
  elif type(i) == tuple:
    for g in i:
      l.append(g)

  
print(l)
print(max(l))
