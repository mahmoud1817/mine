from bs4 import *;from requests import *

# with open("c:/users/mahmoud/desktop/learn/zero/goal.html","r") as f:
#     doc = BeautifulSoup(f,"html.parser")

# tag = doc.title
# tag.string = "modified"

# print(doc.prettify())
# print(doc.find_all("span"))
# print(doc.find_all("span")[0].prettify())

url = "......"
result = get(url)
doc = BeautifulSoup(result.text , "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
specific = parent.find("strong")



