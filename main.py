# import module
# pip install selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# location chromedriver.exe
# firt you must a download chromedriver 
PATH = "C:\Program Files (x86)\chromedriver.exe"
# open chrome
driver = webdriver.Chrome(executable_path=PATH)

# link 
driver.get("https://web.whatsapp.com/")

# choese the name or grup Whatsapp
name = input("Enter the name : ")
msg = input("Enter your message : ") # message do you wan't 
pakage = int(input("Enter your count : ")) # how to much package do you wan't

input('Enter anything after scanning QR code')

# seacrh a xpath html from whatsapp
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div')

# for loop
for i in range(pakage):
	msg_box.send_keys(msg)
	msg_box.send_keys(Keys.RETURN)