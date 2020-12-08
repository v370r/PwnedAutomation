from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from time import sleep 
import sys
sys.stdout=open("OthersOutput.txt","w")
driver = webdriver.Chrome() 
driver.get('https://haveibeenpwned.com/') 
print ("Opened pwned") 
options = webdriver.ChromeOptions()
options.add_argument("headless")
sleep(1) 
count = 0
with open('test.txt', 'r') as file:
    input_lines = [line.strip() for line in file]
    for usr in input_lines:
        username_box = driver.find_element_by_name('Account') 
        username_box.send_keys(usr) 
        print ("Email Id entered") 
        sleep(1)
        login_box = driver.find_element_by_id('searchPwnage') 
        login_box.click()
        sleep(2)
        z= driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/div[1]')
        if z.find_element_by_css_selector("h2").text =="Oh no — pwned!":
            print(usr + " "*10 + "Change Password")
            count +=1

        else:
            print(usr+" "*10+  "safe")
        driver.refresh()
print("Total No of Breachs found",count)
print ("Done")   
sys.stdout.close()

"""
print(input_lines)
usr = "vectorvijay5@gmail.com"
username_box = driver.find_element_by_name('Account') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 

login_box = driver.find_element_by_id('searchPwnage') 
login_box.click()
sleep(2)

z= driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/div[1]')
print(z.find_element_by_css_selector("h2").text)    
print ("Done")      
"""