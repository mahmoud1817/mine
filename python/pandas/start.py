from pandas import *
lst = ["mahmoud","anas","yusef"]
val = ["fst","scnd" ,"thrd"]
s=Series(data=lst,index=val)

stdy = ["math","physics","mechanics"]
ex   = ["science","arabic" , "english"]
mark = [10,20,30]
extra = [1,2,3]
a = Series(data=mark,index=stdy)
b = Series(data=extra,index=stdy)
c=a+b

print(c)