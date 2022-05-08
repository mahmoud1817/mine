from requests_html import *
from tkinter import *

ex=Tk()
ex.title("أرشيف")
ex.geometry("600x700+250+250")
s = HTMLSession()
r=s.get("https://ask.fm/KareemAHelmy2")
n=int(r.html.find('.profileTabAnswerCount ',first=True).text)
filename = input("filename: ")
with open(filename+".txt", "w", encoding="utf-8") as f:
    for m in range(n):
        x=r.html.find(".streamItem_header")[m]
        y=r.html.find(".streamItem_content")[m]
        f.write(f"السؤال: {x.text} \n \n الجواب: {y.text} \n {'*'*50}  \n")

