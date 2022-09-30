import time
import xlrd
import random
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
delay = random.randint(5, 20)
# Home page of  Terminal

ascii_banner = pyfiglet.figlet_format(
    "F   A   C    E   B   O   O   K")
console.print(ascii_banner, justify="left")

console.rule(
    f"Enter the number of accounts for Comment and Share Below: Current Date & Time:  {datetime.now().ctime()}")
console.print("(1)  for   100%  accounts",
              justify="center", style="white on blue")
console.print("(2)  for   75%   accounts",
              justify="center", style="white on blue")
console.print("(3)  for   50%   accounts",
              justify="center", style="white on blue")
console.print("(4)  for   25%   accounts",
              justify="center", style="white on blue")
console.print("(5)  for   0%    accounts",
              justify="center", style="white on blue")


my_comment = input("Please Enter for Comment: ")
my_share = input("Please Enter for Share: ")


home_url = 'https://www.facebook.com/'
disbled_link = 'checkpoint/disabled/?next'
password_fail = 'login/?privacy_mutation_token'


class social_media():

    def login(self):
        self.track_comment = 0
        self.track_share = 0

        self.wb_acc = xlrd.open_workbook(
            str('./accounts and comment/accounts.xlsx'))
        self.wb_com = xlrd.open_workbook(
            str('./accounts and comment/comments.xlsx'))
        self.sheet = self.wb_acc.sheet_by_index(0)
        self.sheetcom = self.wb_com.sheet_by_index(0)
        self.looper = self.sheet.nrows - 1

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
        len_false_link = len(self.false_link)-1
        num = random.randrange(0, len_false_link)
        self.randomed_false_link = self.false_link[num]

    def like_post(self):
        try:
            like_buttons = self.driver.find_elements(By.CLASS_NAME,
                                                     "qi72231t.o9w3sbdw.nu7423ey.tav9wjvu.flwp5yud.tghlliq5.gkg15gwv.s9ok87oh.s9ljgwtm.lxqftegz.bf1zulr9.frfouenu.bonavkto.djs4p424.r7bn319e.bdao358l.fsf7x5fv.tgm57n0e.jez8cy9q.s5oniofx.m8h3af8h.l7ghb35v.kjdc1dyq.kmwttqpk.dnr7xe2t.aeinzg81.srn514ro.oxkhqvkx.rl78xhln.nch0832m.om3e55n1.cr00lzj9.rn8ck1ys.g4tp4svg.o9erhkwx.dzqi5evh.hupbnkgi.hvb2xoa8.fxk3tzhb.jl2a5g8c.f14ij5to.l3ldwz01.icdlwmnq.azwomqv7")

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
        time.sleep(delay)
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
                        print("comment track : ", self.track_comment)
                    body.send_keys(Keys.PAGE_DOWN)
                    time.sleep(delay)
                    self.driver.implicitly_wait(30)
                else:
                    pass

        except Exception as e:
            print(e)

    def share_post(self):
        time.sleep(delay)
        body = self.driver.find_element(By.TAG_NAME, 'body')
        share_buttons = self.driver.find_elements(By.CLASS_NAME,
                                                  "qi72231t.o9w3sbdw.nu7423ey.tav9wjvu.flwp5yud.tghlliq5.gkg15gwv.s9ok87oh.s9ljgwtm.lxqftegz.bf1zulr9.frfouenu.bonavkto.djs4p424.r7bn319e.bdao358l.fsf7x5fv.tgm57n0e.jez8cy9q.s5oniofx.m8h3af8h.l7ghb35v.kjdc1dyq.kmwttqpk.dnr7xe2t.aeinzg81.srn514ro.oxkhqvkx.rl78xhln.nch0832m.om3e55n1.cr00lzj9.rn8ck1ys.s3jn8y49.g4tp4svg.o9erhkwx.dzqi5evh.hupbnkgi.hvb2xoa8.fxk3tzhb.jl2a5g8c.f14ij5to.l3ldwz01.icdlwmnq")
        try:
            for share_button in share_buttons:
                time.sleep(delay)
                checker_share = share_button.get_attribute("aria-label")
                if checker_share == "Send this to friends or post it on your Timeline." or "Send this to friends or post it on your" in checker_share:
                    time.sleep(delay)
                    self.driver.implicitly_wait(30)
                    share_button.click()
                    self.driver.implicitly_wait(30)
                    sharenows = self.driver.find_elements(
                        By.CLASS_NAME, "qi72231t.o9w3sbdw.nu7423ey.tav9wjvu.flwp5yud.tghlliq5.gkg15gwv.s9ok87oh.s9ljgwtm.lxqftegz.bf1zulr9.frfouenu.bonavkto.djs4p424.r7bn319e.bdao358l.fsf7x5fv.tgm57n0e.jez8cy9q.s5oniofx.m8h3af8h.l7ghb35v.kjdc1dyq.kmwttqpk.dnr7xe2t.aeinzg81.srn514ro.oxkhqvkx.rl78xhln.nch0832m.om3e55n1.cr00lzj9.rn8ck1ys.s3jn8y49.g4tp4svg.jl2a5g8c.f14ij5to.l3ldwz01.icdlwmnq.h8391g91.m0cukt09.kpwa50dg.ta68dy8c.b6ax4al1")
                    self.driver.implicitly_wait(30)
                    for sharenow in sharenows:
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
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(delay)
        body.send_keys(Keys.PAGE_UP)
        time.sleep(delay)

    def page_like_scroll(self):
        delay = random.randint(3, 5)
        delay = random.randint(15, 20)
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
        delay = random.randint(15, 20)
        delay = random.randint(20, 30)
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
        """
        Fetch Link From Telegram
              BOT
        """
        import requests
        import json
        url = "https://api.telegram.org/bot5692464682:AAEKqvCKMsOKk2Po9m-dQP4_koR3OqumDjc/getUpdates?offset=-1"

        links = requests.get(url)

        data = json.loads(links.text)

        for i in data['result']:
            try:
                if 'edited_message' in i:
                    self.link = i['edited_message']['text']
                else:
                    self.link = i['message']['text']
            except:
                print("No links found")
                exit()

        console.print("Get Link From Bot :  " + self.link,
                      style="link green" + self.link)
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

    """
    Check The IP Address And Change
    The Ip According to Ipcheck function
    """

    def ipCheck(self):
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
            time.sleep(2)
            print('Connection disconnected')
            self.driver.quit()

    def logout(self):
        print("LOG OUT . . .")
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.DOWN)
        self.driver.find_element(By.XPATH,
                                 "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/span[1]/div[1]/div[1]").click()
        self.driver.implicitly_wait(30)

        time.sleep(delay)
        self.driver.find_element(By.XPATH,
                                 "//span[contains(text(),'Log Out')]").click()


login = social_media()

login.login()
