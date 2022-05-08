from requests_html import *
with open('c:/users/mahmoud/desktop/learn/zero/general/accordion.html') as h:
    s  = h.read()
    ah = HTML(html=s)

print(ah.text) #ah.html