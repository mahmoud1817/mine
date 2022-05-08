see "enter a name: "
give name
if name = "mahmoud"
    see "hey bro"+nl
but name = "anas"
    see "hey anas"+nl
else
    see "who r u?" +nl
ok

see "enter a number: "
give num

switch number(num)
    on 10
        see "ten" +nl
    on 20
        see "twenty" +nl
    other
        see "what is this?" +nl
off

for x=1 to num step 5
    see "hey bro" +nl
next

y=2
while y < num
    see "hey u" +nl
    y++
end

see date() +nl
see time() +nl
see timelist()[18]+nl

n = adddays(date(),3)
see n

m1 = clock()
for z=1 to 1000
    see z # + nl
next
see nl + nl + nl
see "second: "+(clock() - m1)/clockspersecond() +nl

load "stdlib.ring"

see dayofweek("1997-12-13")+nl

see upper(name) #lower

mynames()

func mynames
    see nl+"my name is mahmoud"+nl
    see "my name is ans too"+nl
    see " also yusuf too " +nl

#def other
#    see "my other names are: hasan , ali ....."
#end
#other()