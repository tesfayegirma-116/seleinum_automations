import time
import pandas as pd
import json
import random
import requests
import pyfiglet
from rich import print
from rich.console import Console
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

console = Console()

ascii_banner = pyfiglet.figlet_format(
    "F   A   C    E   B   O   O   K")
console.print(ascii_banner, justify="left")

console.rule(
    f"Enter the number of accounts for Comment and Share Below: Current Date & Time:  {datetime.now().ctime()}")
console.print("(1)  for   100%  accounts",
              justify="center", style="white on black")
console.print("(2)  for   75%   accounts",
              justify="center", style="white on black")
console.print("(3)  for   50%   accounts",
              justify="center", style="white on black")
console.print("(4)  for   25%   accounts",
              justify="center", style="white on black")
console.print("(5)  for   0%    accounts",
              justify="center", style="white on black")

my_comment = input("Please Enter for Comment: ")
my_share = input("Please Enter for Share: ")


console.print("0 for read account from local excel",
              justify="center", style="white on black")
console.print("1 for read account from google-sheet",
              justify="center", style="white on black")

read_excel_from = input("Please Enter account source: ")


console.print("0 for read link from local",
              justify="center", style="white on black")
console.print("1 for read link from Telegram-BOT",
              justify="center", style="white on black")


read_link_from = input("Please Enter link source: ")

home_url = 'https://www.facebook.com/'
disbled_link = 'checkpoint/disabled/?next'
password_fail = 'login/?privacy_mutation_token'


class social_media():

    def login(self):
        delay = random.randint(5, 20)

        if read_excel_from == "0":
            self.wb_acc = pd.read_excel("./accounts and comment/accounts.xlsx")

        elif read_excel_from == "1":

            self.scopes = [

                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive',
            ]
            self.creds = ServiceAccountCredentials.from_json_keyfile_name(
                "./key.json", scopes=self.scopes)
            self.files = gspread.authorize(self.creds)
            self.workbook = self.files.open("Account_Mgt")
            self.sheet = self.workbook.worksheet('Sheet2')
            self.wb_acc = pd.DataFrame(self.sheet.get_all_records())
            print(self.wb_acc)
        else:
            print("chices are only 0 and 1")

        self.user_name = self.sheet.col_values(1)
        self.account_password = self.sheet.col_values(2)

        self.track_comment = 0
        self.track_share = 0
        self.looper = len(self.user_name)

        self.wb_com = pd.read_excel("./accounts and comment/comments.xlsx")
        self.comment_list = self.wb_com['comments'].tolist()

        self.comment_percent()
        self.share_percent()

        try:
            f = open('./accounts info/Working_Accounts.txt', 'r+')
            x = f.readlines()
            y = len(x) - 1
            self.last_line = int(x[y])
            print("Last working account", self.last_line, self.looper)
            if self.last_line == self.looper:
                f = open('./accounts info/Working_Accounts.txt', 'r+')
                f.truncate()
                self.last_line = 0
        except:
            self.last_line = 0

        with console.status("[bold yellow]Work in progress . . .") as status:

            while self.last_line != self.looper:
                for self.i in range(self.last_line, self.looper):
                    delay = random.randint(5, 20)
                    console.print("Current account state ===> ",  self.i, "Account ", "  Last account ===>  ",
                                  self.looper, "Account ", justify="center", style="white on magenta")

                    self.username = self.user_name[self.i]
                    self.password = self.account_password[self.i]
                    self.comment = self.comment_list[self.i]

                    chrome_options = webdriver.ChromeOptions()
                    prefs = {
                        "profile.default_content_setting_values.geolocation": 2}
                    chrome_options.add_experimental_option("prefs", prefs)
                    chrome_options.add_argument("--disable-infobars")
                    chrome_options.add_argument("--start-maximized")
                    chrome_options.add_argument("--disable-notifications")
                    chrome_options.add_argument("--disable-popup-blocking")
                    chrome_options.add_argument("--incognito")

                    self.driver = webdriver.Chrome(service=Service(
                        ChromeDriverManager().install()), options=chrome_options)
                    delay = random.randint(5, 20)
                    # fill the login form and get to the home page
                    self.driver.get(home_url)
                    time.sleep(delay)
                    if (type(self.username) is float):
                        self.driver.find_element(By.XPATH,
                                                 "//input[@id='email']").send_keys(str(int(self.username)))
                    else:
                        self.driver.find_element(By.XPATH,
                                                 "//input[@id='email']").send_keys(str(self.username))

                    self.driver.find_element(By.XPATH,
                                             "//input[@id='pass']").send_keys(self.password)
                    time.sleep(delay)
                    self.driver.find_element(By.NAME, "login").click()
                    time.sleep(delay)
                    self.driver.implicitly_wait(30)

                    self.current_url = self.driver.current_url

                    if self.current_url == home_url:
                        console.print("Login Success", style="green")
                        f = open('./accounts info/Working_Accounts.txt', 'a+')
                        f.write(str(self.i) + '\n')
                        f.close()

                        time.sleep(delay)
                        self.target_link_perform()
                        time.sleep(delay)
                        self.logout()
                        time.sleep(delay)
                        self.driver.quit()

                        console.print(
                            "Next account loading . . .", style="yellow")

                    elif disbled_link in self.current_url:
                        console.print("Login Disabled", style="red")
                        f = open('./accounts info/Disabled_Accounts.txt', 'a')
                        f.write(str(self.i) + ' ' + str(self.username) + '\n')
                        f.close()

                        self.exit()
                        console.print(
                            "Next account loading . . .", style="yellow")

                    elif password_fail in self.current_url:
                        console.print("Password Fail", style="red")
                        f = open(
                            './accounts info/Password_Fail_Accounts.txt', 'a')
                        f.write(str(self.i) + ' ' + str(self.username) + '\n')
                        f.close()

                        self.exit()
                        console.print(
                            "Next account loading . . .", style="yellow")

                    else:
                        console.print("Login Failed", style="red")
                        f = open('./accounts info/Failed_Accounts.txt', 'a')
                        f.write(str(self.i) + ' ' + str(self.username) + '\n')
                        f.close()

                        self.exit()
                        console.print(
                            "Next account loading . . .", style="yellow")

                break
            console.log(
                f"[green]Working Done [/green] All {self.looper} Account")
            f = open('./accounts info/Working_Accounts.txt', 'r+')
            f.truncate()
        console.log(f'[bold][red]Done!')

    def exit(self):
        delay = random.randint(5, 20)
        self.driver.delete_all_cookies()
        self.driver.quit()
        time.sleep(delay)

    def comment_percent(self):
        if my_comment == "1":
            # print("You have selected 1.100%")
            self.percentile_comment = int(self.looper*100/100)
            print("Comment will be done by ===> ",
                  self.percentile_comment, "Accounts")
        elif my_comment == "2":
            # print("You have selected 2.75%")
            self.percentile_comment = int(self.looper*75/100)
            print("Comment will be done by ===> ",
                  self.percentile_comment, "Accounts")
        elif my_comment == "3":
            # print("You have selected 3.50%")
            self.percentile_comment = int(self.looper*50/100)
            print("Comment will be done by ===> ",
                  self.percentile_comment, "Accounts")
        elif my_comment == "4":
            # print("You have selected 4.25%")
            self.percentile_comment = int(self.looper*25/100)
            print("Comment will be done by ===> ",
                  self.percentile_comment, "Accounts")
        elif my_comment == "5":
            # print("You have selected Nothing")
            self.percentile_comment = int(self.looper*0/100)
            print("Comment will be done by ===> ",
                  self.percentile_comment, "Accounts")
        else:
            print("You must enter between 1 up to 5 for Comment")
            exit()

    def share_percent(self):
        if my_share == "1":
            # print("You have selected 1.100%")
            self.percentile_share = int(self.looper*100/100)
            print("Share will be done by ===>  ",
                  self.percentile_share, "Accounts")
        elif my_share == "2":
            # print("You have selected 2.75%")
            self.percentile_share = int(self.looper*75/100)
            print("Share will be done by ===>  ",
                  self.percentile_share, "Accounts")
        elif my_share == "3":
            # print("You have selected 3.50%")
            self.percentile_share = int(self.looper*50/100)
            print("Share will be done by ===>  ",
                  self.percentile_share, "Accounts")
        elif my_share == "4":
            # print("You have selected 4.25%")
            self.percentile_share = int(self.looper*25/100)
            print("Share will be done by ===>  ",
                  self.percentile_share, "Accounts")
        elif my_share == "5":
            # print("You have selected Nothing")
            self.percentile_share = int(self.looper * 0/100)
            print("Share will be done by ===>  ",
                  self.percentile_share, "Accounts")
        else:
            print("You must enter between 1 up to 5 for Share")
            exit()

    def get_falselink(self):
        false_file = open('./links/false_link.txt', 'r+')

        self.false_link = false_file.readline()

    def rand_false_link(self):
        delay = random.randint(5, 20)
        len_false_link = len(self.false_link)-1
        num = random.randrange(0, len_false_link)
        self.randomed_false_link = self.false_link[num]

    def like_post(self):
        delay = random.randint(5, 20)
        try:
            like_buttons = self.driver.find_elements(By.CLASS_NAME,
                                                     "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x5ve5x3")

            for like_button in like_buttons:
                cheker_like = like_button.get_attribute("aria-label")
                if cheker_like == "Like":
                    time.sleep(delay)
                    like_button.click()
                    print("Liked " + '\N{thumbs up sign}')
                    self.driver.implicitly_wait(30)
                    time.sleep(delay)
                    break
                else:
                    pass

        except Exception as e:
            pass

    def comment_post(self):
        delay = random.randint(5, 20)
        body = self.driver.find_element(By.TAG_NAME, 'body')
        try:
            comment_buttons = self.driver.find_elements(By.CLASS_NAME,
                                                        "pbevjfx6.icdlwmnq.om3e55n1.l4e6dv8b.notranslate")
            for comment_button in comment_buttons:
                cheker_comment = comment_button.get_attribute("aria-label")
                if cheker_comment == "Write a comment" or "Write a " in cheker_comment:
                    # page down
                    time.sleep(delay)
                    comment_button.click()
                    time.sleep(delay)
                    print(self.comment)
                    comment_button.send_keys(self.comment)
                    time.sleep(delay)
                    self.driver.implicitly_wait(30)
                    time.sleep(delay)
                    comment_button.send_keys(Keys.ENTER)
                    self.track_comment = self.track_comment + 1
                    with open('./links/comment_track.txt', 'w+') as f:
                        f.write(str(self.track_comment))
                        print("comment counter : ", self.track_comment)
                    body.send_keys(Keys.PAGE_DOWN)
                    time.sleep(delay)
                    self.driver.implicitly_wait(30)
                else:
                    pass

        except Exception as e:
            print(e)

    def share_post(self):
        delay = random.randint(2, 6)
        share_buttons = self.driver.find_elements(By.CLASS_NAME,
                                                  "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz")
        try:
            for share_button in share_buttons:
                checker_share = share_button.get_attribute("aria-label")
                print(checker_share)
                if checker_share == "Send this to friends or post it on your Timeline." or checker_share == "Send this to friends or post it on your timeline." or "Send this to friends or post it on your" in checker_share:
                    time.sleep(delay)
                    share_button.click()
                    self.driver.implicitly_wait(30)
                    sharenows = self.driver.find_elements(
                        By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x1lliihq")
                    for sharenow in sharenows:
                        print(sharenow.text)
                        if sharenow.text == "Share now (Public)" or sharenow.text == "Share now (Friends)" or "Share now" in sharenow.text:
                            time.sleep(delay)
                            sharenow.click()
                            self.driver.implicitly_wait(30)
                            self.track_share = self.track_share + 1
                            with open('./links/share_track.txt', 'w+') as f:
                                f.write(str(self.track_share))
                                print("Share counter : ", self.track_share)
                                time.sleep(delay)
                        else:
                            if sharenow.text == "Share now (Public)" or sharenow.text == "Share now (Friends)" or "Share now" in sharenow.text:
                                time.sleep(delay)
                                sharenow.click()
                                self.driver.implicitly_wait(30)
                                self.track_share = self.track_share + 1
                                with open('./links/share_track.txt', 'w+') as f:
                                    f.write(str(self.track_share))
                                    print("Share counter : ", self.track_share)
                                    time.sleep(delay)

        except:
            pass

    def scroll_up_down(self):
        delay = random.randint(5, 20)
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(delay)
        body.send_keys(Keys.PAGE_UP)
        time.sleep(delay)

    def page_like_scroll(self):
        delay = random.randint(20, 30)
        like = 0
        self.driver.get(self.randomed_false_link)
        time.sleep(delay)
        like_amount = random.randrange(4, 9)
        print(" To like button " + str(like_amount))
        while True:
            if like == like_amount:
                break
            self.like_post()
            like = like+1

            time.sleep(delay)
            self.scroll_up_down()
            time.sleep(delay)

    def Home_scroll(self):

        delay = random.randint(3, 5)
        like = 0
        self.driver.get(home_url)
        time.sleep(delay)
        like_amount = random.randrange(4, 9)
        print(" To like button " + str(like_amount))
        random_function = random.randint(1, 4)
        print(random_function)

        while True:
            if like == like_amount:
                break
            if random_function == 1:
                self.like_post()
            elif random_function == 2:
                self.share_post()
            else:
                self.like_post()
                time.sleep(delay)
                self.share_post()
                time.sleep(delay)
            like = like+1
            print(like)
            time.sleep(delay)
            self.scroll_up_down()
            time.sleep(delay)

    def target_link_perform(self):
        if read_link_from == "0":
            with open("./links/link.txt", 'r+') as f:
                self.link = f.readline()
                print(self.link)

        elif read_link_from == "1":
            delay = random.randint(5, 9)
            url = "https://api.telegram.org/bot5692464682:AAEKqvCKMsOKk2Po9m-dQP4_koR3OqumDjc/getUpdates?offset=-1"

            links = requests.get(url, verify=False)
            time.sleep(delay)

            getText = links.text

            data = json.loads(getText)

            try:
                self.link = data['result'][0]['message']['text']
            except:
                pass

            try:
                self.link = data['result'][0]['edited_message']['text']
            except:
                pass

        else:
            print("chices are only 0 and 1")

        console.print("Get Link From Bot :  " + self.link,
                      style="link green" + self.link)
        delay = random.randint(5, 20)
        time.sleep(delay)
        self.driver.get(self.link)
        time.sleep(delay)
        self.like_post()
        time.sleep(delay)
        if self.percentile_comment == self.track_comment:
            print("Not comment here !!!")
            pass
        else:
            time.sleep(delay)
            self.comment_post()
            time.sleep(delay)

        if self.percentile_share == self.track_share:
            print("Not share here !!!")
            pass
        else:
            time.sleep(delay)
            self.share_post()
            time.sleep(delay)

        if self.percentile_comment == self.track_comment and self.percentile_share == self.track_share:
            print("Not comment and share here !!!")
            time.sleep(delay)
            self.logout()
            time.sleep(delay)
            self.driver.delete_all_cookies()
            time.sleep(delay)
            self.driver.quit()
            ascii_banner = pyfiglet.figlet_format("C o m p l e t e d")
            print(ascii_banner.center(120))
            exit()

    """
    Check The IP Address And Change
    The Ip According to Ipcheck function
    """

    def ipCheck(self):
        delay = random.randint(5, 20)
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")

        driver2 = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=chrome_options)

        time.sleep(delay)
        driver2.get("https://ident.me/")
        try:
            self.pc_ip = driver2.find_element(By.XPATH, "/html/body/pre").text
            if str(self.pc_ip).count('.') == 3:
                pass
            else:
                driver2.get('https://ifconfig.me/ip')
                time.sleep(2)
                pc_ip = driver2.find_element(By.XPATH,
                                             "/html/body/pre").text
                pass
            time.sleep(3)
            driver2.quit()
        except Exception as e:
            pass

    def checkSameIp(self):
        delay = random.randint(5, 20)
        for _ in range(5):
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()))

            self.driver.get("https://ident.me/")
            self.driver.implicitly_wait(10)
            ip_curr = self.driver.find_element(By.XPATH,
                                               "/html/body/pre").text
            print(ip_curr)
            if self.pc_ip != ip_curr:
                print("Now WE can pass Because IP is changed",
                      self.pc_ip + "!=" + ip_curr)
                time.sleep(delay)
                break
            else:
                print("Try again!!!")
                print(self.pc_ip + "==" + ip_curr)
                print("Waiting for seconds to check again")
                self.con_disable()
                time.sleep(delay)
                print("Intiate Browser to enable")
                self.conn_enable()
                time.sleep(delay)
                break

    def conn_enable(self):
        delay = random.randint(5, 20)
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")

        driver = webdriver.Chrome(
            executable_path=r"/home/linuxlite/Desktop/seli/chromedriver", options=chrome_options)

        driver.get('http://192.168.8.1/html/home.html')
        time.sleep(10)
        xxx = driver.find_element(By.XPATH,
                                  '//*[@id="index_connection_status"]').text
        if xxx == 'Disconnected''\n' 'Connection Settings':
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH,
                                "//span[@id='mobile_connect_btn']").click()
            print('Connecting to internet...')
            time.sleep(delay)
            pass
        else:
            self.driver.quit()

    def con_disable(self):
        delay = random.randint(5, 20)
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=chrome_options)

        print("disable")
        self.driver.get('http://192.168.8.1/html/home.html')
        time.sleep(delay)
        xd = self.driver.find_element(By.XPATH,
                                      '//*[@id="index_connection_status"]').text
        if xd == 'Disconnected''\n' 'Connection Settings':
            self.driver.quit()
            pass
        else:
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH,
                                     "//span[@id='mobile_connect_btn']").click()
            time.sleep(delay)
            print('Connection disconnected')
            self.driver.quit()

    def logout(self):
        try:
            delay = random.randint(5, 8)
            print("LOG OUT . . .")
            logins = self.driver.find_elements(By.CLASS_NAME,
                                               "x1ja2u2z.x1n2onr6.x1s65kcs.x15zctf7.x78zum5.x6s0dn4")
            time.sleep(delay)
            self.driver.implicitly_wait(30)

            for login in logins:
                time.sleep(25)
                cheker_login = login.get_attribute("aria-label")
                print(cheker_login)
                if cheker_login == "Account controls and settings" or cheker_login == "Account controls" or cheker_login == "Account Controls and Settings":
                    time.sleep(delay)
                    self.driver.find_element(By.CLASS_NAME,
                                             "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xzsf02u.x1rg5ohu").click()
                    self.driver.implicitly_wait(30)
                    time.sleep(delay)
                    getLogins = self.driver.find_elements(By.CLASS_NAME,
                                                          "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x1lliihq")
                    for getLogin in getLogins:
                        print(getLogin.text)
                        if getLogin == "Log Out" or "Log" in getLogin.text:
                            time.sleep(delay)
                            getLogin.click()
                            self.driver.implicitly_wait(30)

        except:
            print("Log Out fail")
            for login in logins:
                time.sleep(delay)
                cheker_login = login.get_attribute("aria-label")
                print(cheker_login)
                if cheker_login == "Account controls and settings" or cheker_login == "Account" or cheker_login == "Account Controls and Settings":
                    time.sleep(delay)
                    # self.driver.find_element(By.CLASS_NAME,
                    # "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xzsf02u.x1rg5ohu").click()
                    self.driver.implicitly_wait(30)
                    time.sleep(delay)
                    getLogins = self.driver.find_elements(By.CLASS_NAME,
                                                          "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x1lliihq")
                    for getLogin in getLogins:
                        print(getLogin.text)
                        if getLogin == "Log Out" or "Log" in getLogin.text:
                            time.sleep(delay)
                            getLogin.click()
                            self.driver.implicitly_wait(30)

            pass


login = social_media()

login.login()
