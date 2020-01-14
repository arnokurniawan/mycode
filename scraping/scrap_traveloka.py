from selenium import webdriver
import chromedriver_autoinstaller
import requests, bs4, re, time


chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
            
                                      # then add chromedriver to path
source = "https://www.traveloka.com/id-id/flight/fullsearch?ap=JKTA.PLM&dt=11-01-2020.NA&ps=1.0.0&sc=ECONOMY"
driver = webdriver.Chrome()
driver.get(source)
#assert "Python" in driver.title

jspagedata = bs4.BeautifulSoup(driver.page_source, 'lxml') 

pagedata = jspagedata.find('body')

# for data in pagedata:

# 	harga = data.span.text

# 	print(harga)

rute = pagedata.find('h2', class_="css-4rbku5 css-901oao").text
#print(rute)
print("\n RUTE : "+ rute +'\n')
# tanggal = pagedata.find('div', class_='css-901oao r-lsix3s r-fdjqy7').text
# print(tanggal)

# kelas = pagedata.find('div', class_='css-901oao r-low6zhx').text
# print(kelas)

jam = pagedata.find_all('div', class_='_32ZNg')
#print(jam)
jb = jam[0].span.text
jt = jam[1].span.text

print("Jam Berangkat : "+jb )

print("Jam Tiba : "+jt +'\n')

harga = pagedata.find('div', class_='JGqAE').span.text
#print(harga)
print("HARGA : "+harga +'\n')



