import time
import xlrd
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

console = Console()

ascii_banner = pyfiglet.figlet_format(
    "Report Account")
console.print(ascii_banner, justify="left")

home_url = 'https://www.facebook.com/'
disbled_link = 'checkpoint/disabled/?next'
password_fail = 'login/?privacy_mutation_token'


class report_account():

    def login(self):
        delay = random.randint(1, 5)

        self.wb_acc = xlrd.open_workbook(
            str('./accounts and comment/accounts.xlsx'))
        self.wb_com = xlrd.open_workbook(
            str('./accounts and comment/comments.xlsx'))
        self.sheet = self.wb_acc.sheet_by_index(0)
        self.sheetcom = self.wb_com.sheet_by_index(0)
        self.looper = self.sheet.nrows - 1

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
                    delay = random.randint(1, 5)
                    console.print("Current account state ===> ",  self.i, "Account ", "  Last account ===>  ",
                                  self.looper, "Account ", justify="center", style="white on magenta")

                    self.username = self.sheet.cell_value(self.i, 0)
                    self.password = self.sheet.cell_value(self.i, 1)
                    self.comment = self.sheetcom.cell_value(self.i, 0)

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
                    delay = random.randint(1, 2)
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

    def target_link_perform(self):
        delay = random.randint(1, 6)
        url = "https://api.telegram.org/bot5692464682:AAEKqvCKMsOKk2Po9m-dQP4_koR3OqumDjc/getUpdates?offset=-1"

        links = requests.get(url)
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
        try:
            with open("./links/link.txt", 'r+') as f:
                self.link = f.readline()
                print(self.link)
        except:
            print("No Link Found")
            exit()
        console.print("Get Link  :  " + self.link,
                      style="link green" + self.link)
        delay = random.randint(5, 10)
        time.sleep(delay)
        self.driver.get(self.link)
        time.sleep(delay)
        self.report_fb()
        time.sleep(delay)
        self.driver.delete_all_cookies()
        time.sleep(delay)
        self.driver.quit()

    def report_fb(self):
        print("Report ...")
        delay = random.randint(10, 15)

        try:
            button_links = self.driver.find_elements(By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.x2lwn1j.xeuugli.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xjyslct.xjbqb8w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x3nfvp2.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x3ajldb.x194ut8o.x1vzenxt.xd7ygy7.xt298gk.x1xhcax0.x1s928wv.x10pfhc2.x1j6awrg.x1v53gu8.x1tfg27r.xitxdhh")

            for button_link in button_links:
                checker = button_link.get_attribute("aria-haspopup")
                print(checker)
                if checker == "menu":
                    print("click...")
                    button_link.click()
                    print("clicked")
                    self.driver.implicitly_wait(30)

                    button_lists = self.driver.find_elements(
                        By.CLASS_NAME, "x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.xe8uvvx.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.xjyslct.x9f619.x1ypdohk.x78zum5.x1q0g3np.x2lah0s.x1w4qvff.x13mpval.xdj266r.xat24cr.x1n2onr6.x16tdsg8.x1ja2u2z.x6s0dn4.x1y1aw1k.x1sxyh0.xwib8y2.xurb0ha")
                    for button_list in button_lists:
                        checker = button_list.text
                        print(checker)
                        if checker == "Report post":
                            report_post = self.driver.find_element(
                                By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[3]")
                            button_list.click()
                            self.driver.implicitly_wait(30)

                            select_pro = self.driver.find_element(
                                By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]")
                            select_pro.click()
                            self.driver.implicitly_wait(30)

                            select_kind = self.driver.find_element(
                                By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
                            select_kind.click()
                            self.driver.implicitly_wait(30)

                            select_submit = self.driver.find_element(
                                By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[4]/div[1]")
                            select_submit.click()
                            self.driver.implicitly_wait(30)

                            select_thanks = self.driver.find_element(
                                By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]")
                            select_thanks.click()
                            self.driver.implicitly_wait(30)

        except Exception as e:
            print(e)
            exit()

    def exit(self):
        delay = random.randint(1, 5)
        self.driver.delete_all_cookies()
        self.driver.quit()
        time.sleep(delay)

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


start = report_account()

start.login()
