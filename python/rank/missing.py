def findmissed(thing):
    al   = "abcdefghijklmnopqrstuvwxyz"
    some = al.index(thing[0])

    for i in al[some:]:
        if i not in thing:
            return "this is it => " + i
    
print(findmissed("acd"))