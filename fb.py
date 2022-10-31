import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from colorama import Fore, Back, Style
import random

randomnumber = round(random.uniform(0, 1000))
randomsleeptime= round(random.uniform(10, 25))

df=pd.read_csv('ያገርቤትስም.csv')
print(Back.GREEN,Fore.YELLOW )


randomname=df.iloc[randomnumber]
print(randomname)
print(Style.RESET_ALL)

df = pd.read_excel("accounts.xlsx")
usernames=df['ስም'].tolist()
passwords=df['ቁልፍ'].tolist()

for i in range(0,len(usernames)):
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get("https://www.facebook.com")
  driver.maximize_window()
 
  driver.implicitly_wait(30)
  x=driver.find_element(By.XPATH,"//input[@id='email']").send_keys(usernames[i])
  time.sleep(1)
  x=driver.find_element(By.XPATH,"//input[@id='pass']").send_keys(passwords[i])
  time.sleep(10)
  d=driver.find_element(By.NAME, "login")
  d.click()
  time.sleep(randomsleeptime)

  
  elem=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]")
  elem.click()
  elem.send_keys(randomname)
  time.sleep(randomsleeptime)
  elem.send_keys(Keys.RETURN)

  seemore=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]/div[1]/div[1]/span[1]/span[1]")
  seemore.click()

  time.sleep(randomsleeptime)
  addfriends =driver.find_elements(By.CLASS_NAME,"x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619.x3nfvp2.xdt5ytf.xl56j7k.x1n2onr6.xh8yej3")
  
  time.sleep(randomsleeptime)
  print(Back.GREEN )
  print(addfriends)
  print(len(addfriends),"-friends to add")
  
  count=0
  for friend in addfriends:
    if friend.get_attribute('aria-label') == "Add friend":
            friend.click()
            count+=1
            if count>=5:
              break
            time.sleep(randomsleeptime)
    else:
     break
     print("nnnnnnnnnnnnnooooooooooooooooooooo") 
  print(Style.RESET_ALL)
  

  time.sleep(randomsleeptime)
  account=driver.find_element(By.CLASS_NAME,"x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xzsf02u.x1rg5ohu")
  account.click()
  time.sleep(randomsleeptime)
  
  logout=driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]")
  print(account)
  logout.click()
  time.sleep(randomsleeptime)

  driver.close()



# def login():

