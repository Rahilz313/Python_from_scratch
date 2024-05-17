t = (1,2,3,4,5)
type(t)
t1 = ('rahil', 345, 45+3j, True)

l = ['rahil', 345, 45+3j, True]
type(l)

t2 = ()
type(t2)
l[0:2]
t1[0:2]
t1
type(t1)
t1[::-1]
t1[-1]
t1[0::2]
# Figuring out the difference between list and tuples
l
l[0]
l[0] = "Roshan"
l
# now doing same thing in tuples
t1[0]
t1[0] = 'xyz' # it will give error as tuples object does not support item assigemnt 
# Hence we got to know that tuples are immutable whereas lists are mutable
t1
t2 = (3,543,32,34)
t2
t1+t2
t1
t1*2
t1.count('rahil')
t1.index('rahil')
t = ('rahil', 'John', 343, 4+8j, True, ('the', 343))
t1 = ([23,'ragil'], (343, 'off'), 3434)
t1[0][0]

t1[2]
t1[0][1] = "Rahil"
t1
# Converting list to tuples and tuples to list
t1
l
tuple(l)
list(t1)
l = [1,2,3,4,5,53,43,56,4,43,5435645,32,32,34,4552346576864,232,43,23346,45745,2]
set(l)
l
s = {}
type(s)
s2 = {1,1,1,1,1,2,2,3,44,3,443,445,3} # here we got to know that set does not contain duplicate elements 
s2
s2[0] # and here we got to know that set cannot be accessed using slicing operations as set is an unordered collection of elements
list(s2)
s2
s2[0]
s2
s2.add('Rahil')
s2
s2.add(['23','sdfs'])
s={(3,34,45,6),43,5,3,2}
s.remove(43)
s.discard(5)
s[0]
s
s = {1,1,2,3,23,324,3,2,243242,43223,21,21,34, 'rahil', 'rahil'}
s
#####################################################################
d  = {}
type(d)
d = {1,2}
type(d)
d = {4:'rahil'}
type(d)
d1 = {'key1': 5445, 'key2': 'Rahil', 53:[3,3,4,5]}
d1
d1["key1"]
d1[53][0]
d = {3: ['sdfsdf', 'errte', 3,4,5,3,2,9]}
d[3]
d1 = {'key1': [ 1,3,45], 'key2' : "rahil", 'key1':45}
d1['key2']
d= {'name': 'Rahil', 'mo_no': 23432412, 'mail_id': 'rahilz.shaikh@gmail.com', 'key1': (3,4,5,6),'key3': {1,2,3,4,45,5,}, 'key4':{1:4,6:9}}
d['key4'][6]
d.items()
d['key3']
d['name'] = 'Roshan'
d
# we cannot renama a key, we can delete and creata a new one
del d['name']
d['name'] = 'Roshan'
d
d['name']
d.get('name')