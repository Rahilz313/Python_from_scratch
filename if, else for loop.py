a  = 10 
a < 15
id a < 15:
    print('my name is Rahil')
if a < 15:
    pass
if a < 15:
    print('my name is rahil')
    
if 24 < 15:
    print('my name is rhail')  
if 10 < 3:
    print('10 is lesser then 3')
else: 
    print('if statement is wrong')
    
if 5 < 10:
    print('5 is lesser than 10')
else: 
    print('5 is not lesser than 10')
##############################################3
income = 100
if income < 50:
    print('i will be able to but phone ')
elif income < 70:
    print(' i will be able to buy a car')
elif income < 90:
    print(' i will be able to rent a house')  
else: 
    print(' i wont be able be buy anything')      
#########################################################
# Taking input from the user for the same code
income = int(input())

if income < 50:
    print('I will be able to buy a phone')
elif income < 70:
    print('I will be able to buy a car')    
elif income < 90:
    print('I will be able to rent a house') 
else:
    print('I won\'t be able to buy anything')      

####################################################################
# Discount Calculation
Total_price = int(input())
if Total_price >  2000:
    discount = Total_price * .20
    print("Discount will be ", discount)
elif Total_price <= 7000:
    discount = Total_price *.05
else:
    print('wont be able to give any discount')    
############################################################
# Giving discont based on coupon code
coupon = "Rahil17"

if coupon == "Rahil17":
    print('You will be able to get a discount of 5%')
    paid_amount = 7080 - (7080 * 0.05)
    print('You will be able to get a discount of this amount:', paid_amount)
else:
    print('Kindly use a valid coupon code')
#########################################################
# Taking input from the user in the same code
coupon = input()
amount = int(input())
if coupon == 'Rahil17':
    print('you will get a discount of 5%')
    paid_amount = amount-(amount*0.05)
    print('you will be able to get a discount of this amount:', paid_amount)
else:
    print('Kindly use a valid coupon')    
    
# Giving result of based on hours studied
study_hours = float(input())
if study_hours < 1:
  print('it may take 8-9 months to transition')
elif study_hours > 1 and study_hours <= 3:
  print('it may take 7-8 months to transition')
elif study_hours > 3 and study_hours <=6:
  print('it may take around 4-5 months to transition')
##############################################################3 
s = input('Enter to Start')


if s == 'oneneuron':
    course = input('Enter the course')
    if course == "DSA":
        print('yes it is available under one neuron and in multiple mode for job preparation and core concepts')
    elif course == 'BlockChain':
        print('This is not available as of now, kindly raise your demand and we will fullfill in 60 days' )
    elif course == "FSDS":
        print('yes its available, you can start learning ')
    else:
        print('this course is not available kindly raise your demand')
       
elif s == 'oneneuronservice':
    service = input('Enter the service') 
    if service == 'courserequest':
        print('Dear Learner: you can raise demand related to any new course, and we will fulfil in 60 days')
    elif service == 'doubt':
        print('Dear Learner: you can raise demand related to any doubt and we will fullfill it in 24 hours')
    elif service == "workwithus":
        print('Dear Learner:, you can raise the demand to work with us, our HR will evaluate and get back to you')
    else:
        print('kindly provide us you feedback and we will fulfill')
else:
    print('kindly connect with our team') 

###################################################################################################################
l = [1,2,3,4,5,6,7,8,9,0]
for i in l:
    print(i)

for i in 'rahil':
    print(i)
t = (1,2,3,45,6,3)
for i in t:
    print(i)    
    
l = [1,2,3,54,4.7j, 'rahil', True]  
for i in l:
    print(type(i),i)
    
l = [1,2,3,45,5]
l1=[]
for i in l:
    print(i+2)
    l1.append(i)
l1

#####################
#filter out just an integer out of this below list
l = [2,45,78,12,'rahil',6+7j,[65,83,2,'sdjls']]
for i in l:
    if type(i) == int:
        print(i)
        
    elif type(i) == list:
        for j in i:
            if type(j) == int:
                print(j)
                
########
l = [2,45,78,12,'rahil',6+7j,[65,83,2,'sdjls']]                
# Q1. try to print index of all the element
# Q2. try to extract all the list of char if element is string
# Q3. try to return a list after doing a square of all the int element
#Q1
for i in  range (len(l)):
    print('index', i , 'for an element',l[i])
    
for i,j in enumerate(l):
    print(i,j)
    
#Q2
for i in l:
    if type(i) == str:
        l2=[]
        for j in (i):
            l2.append(j)
        print(l2)
    elif type(i) == list:
        l2=[]
        for j in i:
            if type(j) == str:
                for k in j:
                    l2.append(k)
        print(l2)
l2
#Q3.   
for i in l:
    if type(i) == int:
        k=[]
        k.append(i**2)
        print(k)
    elif type(i) == list:
        for j in i:
            if type(j) == int:
                k=[]
                k.append(j**2)
                print(k)