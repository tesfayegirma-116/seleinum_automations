import time as ጊዜ
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By as በ
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as ፓንዳ
from colorama import Fore, Back, Style
import random as እንዳገኘ


class amigos():

    ትንሽጠብቅ1 = round(እንዳገኘ.uniform(10, 25))
    ትንሽጠብቅ2 = round(እንዳገኘ.uniform(10, 25))
    ትንሽጠብቅ3 = round(እንዳገኘ.uniform(10, 25))

    def __init__(self):

        df = ፓንዳ.read_csv('ያገርቤትስም.csv')
        self.እንዳገኘስም = እንዳገኘ.choice(df['ስም'].to_list())
        df = ፓንዳ.read_excel(
            "../accounts and comment/accounts_for_add_friend.xlsx")
        self.ስም = df['ስም'].tolist()
        self.ቁልፍ = df['ቁልፍ'].tolist()

    def __str__(self):
        x = f" ዛሬ በ U+1F44D {self.እንዳገኘስም} ስም ያሉ ጓደኞች እንዲሆኑን እንጠይቃለን!"
        return f"\n{Fore.YELLOW }{x}\n\n ጓደኛ ጠያቂዎች {self.ስም}{Style.RESET_ALL}\n"

    def ጀምር(self):
        for i in range(0, len(self.ስም)):
            self.ወደፌስቡክግባ(i)
            self.ጓደኛፈልግ()
            # self.ጓደኛአክል()
            # self.ከፌስቡክውጣ()

    def ወደፌስቡክግባ(self, i):
        print(f'{Fore.GREEN }\nopening faceebook........')
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.facebook.com")
        self. driver.maximize_window()
        print('\nlogging.....')
        self.driver.implicitly_wait(30)
        self.driver.find_element(
            በ .XPATH, "//input[@id='email']").send_keys(self.ስም[i])
        ጊዜ.sleep(1)
        self.driver.find_element(
            በ .XPATH, "//input[@id='pass']").send_keys(self.ቁልፍ[i])
        ጊዜ.sleep(10)
        self.driver.find_element(በ .NAME, "login").click()
        print(f'\nloged in...{Style.RESET_ALL}')
        # ጊዜ.sleep(self.ትንሽጠብቅ1)
        self.driver.implicitly_wait(30)

    def ጓደኛፈልግ(self):
        print(Fore.YELLOW)
        ፈልግ = self.driver.find_element(በ .XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]\
                /div[1]/div[1]/label[1]/input[1]")
        # ፈልግ.click()
        ፈልግ.send_keys(self.እንዳገኘስም)

        ጊዜ.sleep(self.ትንሽጠብቅ2)

        ፈልግ.send_keys(Keys.RETURN)

        self.driver.find_element(በ .XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]\
                /div[1]/div[1]/div[1]/div[2]/a[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()

        self.driver.implicitly_wait(30)

        # ጊዜ.sleep(self.ትንሽጠብቅ3)
        self.እጩጓደኞቼ = self.driver.find_elements(
            በ .CLASS_NAME, "x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619.x3nfvp2.xdt5ytf.xl56j7k.x1n2onr6.xh8yej3")
        ጊዜ.sleep(self.ትንሽጠብቅ2)

        print(self.እጩጓደኞቼ)

        print(len(self.እጩጓደኞቼ), "-friends to add")
        print({Style.RESET_ALL})
        # self.ጓደኛአክል()
        # return self.እጩጓደኞቼ

        print(f'{Fore.RED }')
        ቆጣሪ = 0
        for ጓደኛ in self.እጩጓደኞቼ:
            if ጓደኛ.get_attribute('aria-label') == "Add friend":
                ጓደኛ.click()
                ቆጣሪ += 1
                if ቆጣሪ >= 5:
                    break
                ጊዜ.sleep(self.ትንሽጠብቅ2)

            else:

                print("መጨመሪያውን አላገኘውትም!")

                break
        print({Style.RESET_ALL})

        print(f'{Fore.BLUE }')
        ጊዜ.sleep(self.ትንሽጠብቅ1)

        self.driver.find_element(በ .CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.\
            x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.\
                xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.\
                    x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xzsf02u.x1rg5ohu").click()
        self.driver.implicitly_wait(30)
        # ጊዜ.sleep(self.ትንሽጠብቅ3)

        self.driver.find_element(በ .XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]\
            /div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]").click()
        self.driver.implicitly_wait(30)
        # ጊዜ.sleep(self.ትንሽጠብቅ1)

        self.driver.close()
        print({Style.RESET_ALL})


አስነሳ = amigos()
print(አስነሳ)
አስነሳ.ጀምር()
