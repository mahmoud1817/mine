from urllib.request import *
from urllib.error   import *

try:
    take = urlopen("https://mahmoudsite.000webhostapp.com/error")
    print(take.readline()) #read(characters),url,status
except HTTPError as e:
    print(f" code: {e.code} , reason: {e.reason}, link: {e.url}")
