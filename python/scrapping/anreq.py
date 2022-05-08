from requests import *

reg = get("https://mahmoudsite.000webhostapp.com")
print(reg.text) #.text , .content