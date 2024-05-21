# Python provides an in built function open() to open a file.

# Synatax

#f = open(filename, mode='r', buffering, encoding=None, errors=None, newline=None, Closefd=True)

#f = open(filename,mode=='r')

# Below are the arguments used in the filehandling
 
 # 1. filename - which file we want to access it simply means that
 # 2. mode - access mode (purpose of opening file)
 f = open('test.txt') # if we do not specify any mode then it will take by default read mode
 if f:
     print('file successfully opened')
     
f = open('test.txt', mode = 'w') # now if we want to write something in a file then we pass argument after a comma, as write     
print(type(f))

# Opening a file from different location

k = open('new.txt','r')
if k:
    print(k)
    
f = open('dummy.txt','w')
f = open('dummy1.txt','r')
f.write('this is my first file operation')
f.close()

f.read()
f.write('this is sample writing operation') # here it is giving this error io.UnsupportedOperation: not writable bcz we have opened the file in read mode

f = open('dummy1.txt','r')
f.read()  # if we open the file in read mode and open it and again we open it, it will give blank string ''
# so what happens here when we open a file and read it first time it will be readable but 2nd time it will give blank string.
# bcz first time the cursor will read the data from start to end and now the cursor is at the end point.
# and if we try to read the file it is trying to read but as the cursor is at last and after the cursor there is no data it is giving blank string

# to reset the cursor we have a function, using which cursor can be reset at any position, eg if want to read out the file at 5th charter
f.seek(5)
f.read() # now here as we can see it is giving us the data from the 5th position

# we want to reset at begining then we can give index = 0 
f.seek(0)
f.read() # here we are able to read the whole data from starting 

# if we want to know where is our cursor, then we can get to know that using a function call tell
f.tell() # it is giving us where our cursor is present
f.seek(0)
f.tell()

f.close()

f = open('dummy1.txt', 'r+')
f.read()
f.readline()
f.seek(0)
f.readline()
f.write('''this is just for 
        demo purpose''')
f.seek(0)
f.readline()
f.close()
f.read()

f = open('google.txt', 'w')
f.write("""Google began in January 1996 as a research project by Larry Page and Sergey Brin while they were both PhD students at Stanford University in California.[21][22][23] The project initially involved an unofficial "third founder", Scott Hassan, the original lead programmer who wrote much of the code for the original Google Search engine, but he left before Google was officially founded as a company;[24][25] Hassan went on to pursue a career in robotics and founded the company Willow Garage in 2006.[26][27]

While conventional search engines ranked results by counting how many times the search terms appeared on the page, they theorized about a better system that analyzed the relationships among websites.[28] They called this algorithm PageRank; it determined a website's relevance by the number of pages, and the importance of those pages that linked back to the original site.[29][30] Page told his ideas to Hassan, who began writing the code to implement Page's ideas.[24]

Page and Brin originally nicknamed the new search engine "BackRub", because the system checked backlinks to estimate the importance of a site.[21][31][32] Hassan as well as Alan Steremberg were cited by Page and Brin as being critical to the development of Google. Rajeev Motwani and Terry Winograd later co-authored with Page and Brin the first paper about the project, describing PageRank and the initial prototype of the Google search engine, published in 1998. Héctor García-Molina and Jeffrey Ullman were also cited as contributors to the project.[33] PageRank was influenced by a similar page-ranking and site-scoring algorithm earlier used for RankDex, developed by Robin Li in 1996, with Larry Page's PageRank patent including a citation to Li's earlier RankDex patent; Li later went on to create the Chinese search engine Baidu.[34][35]

Eventually, they changed the name to Google; the name of the search engine was a misspelling of the word googol,[21][36][37] a very large number written 10100 (1 followed by 100 zeros), picked to signify that the search engine was intended to provide large quantities of information.[38]""")
f.close()
f = open('google.txt')
f.read()
f.seek(0)
f.readline()
f.tell()
f.close()

f = open('google.txt', 'r+')
for line in f:
    print(line, end = '')
    
f = open('google.txt', 'r+') # r+ mode is nothing but read as well as write mode
f.write('this is fake info')
f.close()
f = open('google.txt')
for i in f:
    print(i, end = " ")
f.tell()
f.write('this is fake info')
f = open('google.txt', 'r+')
f.read()
f.tell()
f.seek(2341)
f.write('this is demo writing operation at particular index')
f.close()
f = open('google.txt')
for i in f:
    print(i, end = " ")
    
# Q. Where there is google word in a file we need to replace that with our name
f = open('google.txt', 'r+')
for i in f:
    if i == 'google' or i == 'Google':
        print(i)
        