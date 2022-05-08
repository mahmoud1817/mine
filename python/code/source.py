help("heywords")
a,b,c=1,2,3
d = "1234\rabcde"
e = "mahmoud" 
f = e[0:8:1]
g = len(e)
h = "# hey bro "
i = h.strip('#')
j = e.title() #captalize , upper , lower
k = e.zfill(10)
l = e.split('-',5)
m = e.center(10,"-")
n = e.count("m",0,8)
o = e.swapcase()
p = e.startswith('m',0,8)
q = e.endswith('d',0,8)
r = e.index('m',0,8)
s = e.find('m',0,8)
t = e.rjust(14,"_")
u = h.splitlines()
v = h.expandtabs(5)
w = e.istitle() #isspace , islower , isupper , isidentifier , isalpha ,isalnum
x = type(e)
#replace("anas","yusef",1)  (",").join("mylist")
ee=l.sort(reverse=False)
eee=l.reverse()
l.clear() ; l.copy ; l.append("anas"); l.insert(0,"ali");l.pop(-1)
tu = "mahmoud","anas" #immutable 
mm,nn = tu
s1 = {"mahmoud"} ; s2 = {"anas"}
s3 = s1.update(s2) # union
#issubset isuperset symmetric difference intersection isdisjoint
s1.discard(2) #remove
print(s1|s2 )
print(tu * 5)
print(e.replace("mahmoud","ans",1))
print(",".join(e))
print("my name is %s"%(e)) #%d %.2f %.5s
print("my name is {}".format(e)) #{:f}{:,d}{0:.3s}
print(f"my name is {e}")
print(119//20) # 3**3
from random import *;print(randint(10,11))
# from shutil import *; copy2('from','to');move('from','2);copytree('f','1')
# from os import *; mkdir('thing.txt'); remove('thing.txt');rmdir('folder')
# if path.exists('folan.txt') and path.isfile(m):listdir('here')
# m=open('mahmoud.txt','w+');m.write('hey');m.close()
# system('app.exe')
# things = [n for n in range(10) if name == "mahmoud"]
# from datetime import *;print(datetime.now().time());print(date(1997,12,13))
# from math import *; print(floor(1.2),round(1.4),ceil(2.01))
# names=['mahmoud','anas'];print("mahmoud" in names);myset.clear()
# from csv import *; r =reader('names.csv'); n= next(r)
# exec(open('file.py').read())
# from sys import *;path();help(path);print(dir)
# print(hasattr(m,'name'));setattr(m,'folan');getattr(m,'name');delattr(m,'name')
# print(n.__doc__);print(m.__dict__);print(m.__name__);print(m.__module__)
# print(m.__bases__);print(m.__class__.__base__)