from selenium import webdriver
path = "C:\Program Files (x86)\chromedriver.exe"

dr = webdriver.Chrome(path)
dr.get("https://mahmoudsite.000webhostapp.com")
#print(dr.title)
dr.quit() #dr.close => tab