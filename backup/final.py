import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import xlrd
import os
import openpyxl
from rich import print
import pyfiglet
from webdriver_manager.chrome import ChromeDriverManager



# delay timer for random time
first_delay = random.randint(10, 30)
second_delay = random.randint(20, 40)
one_sec_delay = random.randint(40, 50)
third_delay = random.randint(50, 80)
fouth_delay = random.randint(20, 50)
# links variable
home_url = 'https://www.facebook.com/'
disbled_link = 'checkpoint/disabled/?next'
password_fail = 'login/?privacy_mutation_token'

# check percentage of success
hunderd_percent = 100
seventyfive_percent = 75
fifty_percent = 50
twentyfive_percent = 25
zero_percent = 0

# Home page of  Terminal
ascii_banner = pyfiglet.figlet_format("F a c e b o o k  Bot")
print(ascii_banner)

print("Please enter your choice for comment and share as listed below:", end="\n")
print("(1) ----------------> 100%")
print("(2) ----------------> 75%")
print("(3) ----------------> 50%")
print("(4) ----------------> 25%")
print("(5) ----------------> Nothing")
my_comment = input("Please Enter your choice for Comment: ")
my_share = input("Please Enter your choice for Share: ")


# Check current Ip

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

time.sleep(first_delay)
driver2.get("https://ident.me/")
try:
    pc_ip = driver2.find_element(By.XPATH, "/html/body/pre").text
    print(pc_ip)
    if str(pc_ip).count('.') == 3:
        pass
    else:
        driver2.get('https://ifconfig.me/ip')
        time.sleep(2)
        pc_ip = driver2.find_element(By.XPATH,
            "/html/body/pre").text
        pass
    time.sleep(3)
    driver2.quit()
    # print("1st")
except Exception as e:
    time.sleep(first_delay)
    driver2.get("https://whatismyipaddress.com/")
    driver2.implicitly_wait(10)
    pc_ip = driver2.find_element(By.XPATH,
        '//*[@id="ipv4"]/a').text
    # print(pc_ip)
    if str(pc_ip).count('.') == 3:
        pass
    else:
        driver2.get('https://ifconfig.me/ip')
        time.sleep(first_delay)
        pc_ip = driver2.find_element(By.XPATH,
            "/html/body/pre").text
        pass
    time.sleep(first_delay)
    driver2.quit()


class social_media():

    def create(self):
        desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
        folder = os.path.join(desktop, 'Facebook')
        # print(folder)

        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        subfolder1 = os.path.join(folder, 'Urls')

        if not os.path.exists(subfolder1):
            os.makedirs(subfolder1, exist_ok=True)
        subfolder2 = os.path.join(folder, 'Accounts Status')

        if not os.path.exists(subfolder2):
            os.makedirs(subfolder2, exist_ok=True)
        subfolder3 = os.path.join(folder, 'Accounts & Passwords')

        if not os.path.exists(subfolder3):
            os.makedirs(subfolder3, exist_ok=True)
        subfolder = os.path.join(folder, 'ChromeDriver')

        if not os.path.exists(subfolder):
            os.makedirs(subfolder, exist_ok=True)

        else:
            # print('Folder already exists')
            pass

        # file creation begins here
        try:
            with open(os.path.join(subfolder1 + '/', 'links.txt'), 'w') as f:
                f.write('')
                f.close()
        except FileNotFoundError:
            print('File not found')

        try:
            with open(os.path.join(subfolder2 + '/', 'DisableAccounts.txt'), 'w') as f:
                f.write('')
                f.close()
            with open(os.path.join(subfolder2 + '/', 'WorkingAccounts.txt'), 'w') as f:
                f.write('')
                f.close()
            with open(os.path.join(subfolder2 + '/', 'PasswordFail.txt'), 'w') as f:
                f.write('')
                f.close()
        except FileNotFoundError:
            print('Files alrady exists')

        try:
            wb = openpyxl.Workbook()
            wb.save(os.path.join(subfolder3 + '/', 'Accounts.xlsx'))
            wb.save(os.path.join(subfolder3 + '/', 'Comments.xlsx'))
            wb.close()
        except FileNotFoundError:
            print('File alraedy exists')

    def comment_percent(self):
        if my_comment == "1":
            # print("You have selected 1.100%")
            self.percentile_comment = int(self.looper*hunderd_percent/100)
            print("The percentile is: ", self.percentile_comment)
        elif my_comment == "2":
            # print("You have selected 2.75%")
            self.percentile_comment = int(self.looper*seventyfive_percent/100)
            print("The percentile is: ", self.percentile_comment)
        elif my_comment == "3":
            # print("You have selected 3.50%")
            self.percentile_comment = int(self.looper*fifty_percent/100)
            print("The percentile is: ", self.percentile_comment)
        elif my_comment == "4":
            # print("You have selected 4.25%")
            self.percentile_comment = int(self.looper*twentyfive_percent/100)
            print("The percentile is: ", self.percentile_comment)
        elif my_comment == "5":
            # print("You have selected Nothing")
            self.percentile_comment = int(self.looper*zero_percent/100)
            print("The percentile is: ", self.percentile_comment)
        else:
            print("You have entered an invalid choice")

    def share_percent(self):
        if my_share == "1":
            # print("You have selected 1.100%")
            self.percentile_share = int(self.looper*hunderd_percent/100)
            print("The percentile is: ", self.percentile_share)
        elif my_share == "2":
            # print("You have selected 2.75%")
            self.percentile_share = int(self.looper*seventyfive_percent/100)
            print("The percentile is: ", self.percentile_share)
        elif my_share == "3":
            # print("You have selected 3.50%")
            self.percentile_share = int(self.looper*fifty_percent/100)
            print("The percentile is: ", self.percentile_share)
        elif my_share == "4":
            # print("You have selected 4.25%")
            self.percentile_share = int(self.looper*twentyfive_percent/100)
            print("The percentile is: ", self.percentile_share)
        elif my_share == "5":
            # print("You have selected Nothing")
            self.percentile_share = int(self.looper*zero_percent/100)
            print("The percentile is: ", self.percentile_share)
        else:
            print("You have entered an invalid choice")

    def get_link(self):
        file = open('link.txt', 'r+')

        self.link = file.readline()

    def get_falselink(self):
        false_file = open('false_link.txt', 'r+')

        self.false_link = false_file.readline()

    def rand_false_link(self):
        len_false_link = len(self.false_link)-1
        num = random.randrange(0, len_false_link)
        self.randomed_false_link = self.false_link[num]

    def login(self):
        # self.create()
        print("Check IP . . .")
        self.check()
        self.track_comment = 0
        self.track_share = 0

        self.wb_acc = xlrd.open_workbook(str('accounts.xlsx'))
        self.wb_com = xlrd.open_workbook(str('exl_comments.xlsx'))
        self.sheet = self.wb_acc.sheet_by_index(0)
        self.sheetcom = self.wb_com.sheet_by_index(0)
        self.looper = self.sheet.nrows-1

        # truncate working_accounts.txt if it already equal to self.looper

        try:

            f = open('Working_Accounts.txt', 'r')
            x = f.readlines()
            y = len(x) - 1
            self.last_line = int(x[y])
            print(self.last_line, "is the last line",
                  self.looper, "is the looper")
            if self.last_line == self.looper:
                f = open('Working_Accounts.txt', 'w')
                f.truncate()
                self.last_line = 0
                print("All accounts have been used")
        except:
            self.last_line = 0

        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        B = [1, 2, 3]
        Randomizer = ['even', 'odd']
        max = 5
        changed_counter = 0
        for self.i in range(self.last_line, self.looper):
            first_delay = random.randint(1, 3)
            second_delay = random.randint(2, 4)
            one_sec_delay = random.randint(4, 5)
            third_delay = random.randint(5, 8)
            fouth_delay = random.randint(2, 5)
            self.username = self.sheet.cell_value(self.i, 0)
            self.password = self.sheet.cell_value(self.i, 1)
            # self.comment = self.sheetcom.cell_value(self.i, 0)
            # initalize the webdriver

            s = random.choice(A)
            z = random.choice(B)
            c = s*z
            print("value of c:", c)

            Randf = random.choice(Randomizer)

            # if c % 2 == 0 and Randf == 'even' and changed_counter < max:
            #     print('even.................change IP')
            #     self.con_disable()
            #     self.conn_enable()
            #     self.check()

            #     changed_counter += 1

            # elif c % 2 != 0 and Randf == 'odd' and changed_counter < max-1:
            #     print('odd.................change IP')
            #     changed_counter += 1
            #     self.con_disable()
            #     self.conn_enable()
            #     self.check()

            # if changed_counter == 0 and self.i % 5 == 0:
            #     print('Max Ip changed')
            #     self.con_disable()
            #     self.conn_enable()
            #     self.check()
            # if changed_counter == max:

            #     changed_counter = 0
            #     self.driver.quit()

            # else:
            #     pass

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

            # fill the login form and get to the home page
            self.driver.get(home_url)
            time.sleep(second_delay)
            self.driver.find_element(By.XPATH,
                                     "//input[@id='email']").send_keys(self.username)
            time.sleep(third_delay)
            self.driver.find_element(By.XPATH,
                                     "//input[@id='pass']").send_keys(self.password)
            time.sleep(fouth_delay)
            self.driver.find_element(By.NAME, "login").click()
            time.sleep(third_delay)
            self.driver.implicitly_wait(30)

            self.current_url = self.driver.current_url
            print(self.current_url)
            if self.current_url == home_url or self.current_url=="https://www.facebook.com/mobileprotection?source=mobile_mirror_nux":
                print("login success")
                f = open('Working_Accounts.txt', 'a')
                f.write(str(self.i) + '\n')
                f.close()

                self.comment_percent()
                # print("The comment with : ", self.percentile_comment , "accounts")
                self.share_percent()
                # print("The share with : ", self.percentile_share , "accounts")
                time.sleep(second_delay)
                # self.get_link()
                self.get_falselink()
                print("false here")
                # self.chop_chop()
                time.sleep(third_delay)
                # self.rand_false_link()

                # # self.driver.get(self.link)
                # time.sleep(one_sec_delay)
                # self.random_functions()
                # time.sleep(third_delay)

                self.target_link_perform()
                # time.sleep(second_delay)

                # self.random_functions()""

                time.sleep(second_delay)
                try:
                    self.logout()
                except:
                    pass

                self.exit()

            elif disbled_link in self.current_url:
                print("login disabled")
                f = open('Disabled_Accounts.txt', 'a')
                # f.write(str(self.username + '\n'))
                f.write(str(self.i) + '\n')
                f.close()
                fouth_delay = random.randint(20, 30)

                self.exit()

            elif password_fail in self.current_url:
                print("password fail")
                f = open('Password_Fail_Accounts.txt', 'a')
                # f.write(str(self.username + '\n'))
                f.write(str(self.i) + '\n')
                f.close()

                self.exit()

            else:
                print("login failed")
                f = open('Failed_Accounts.txt', 'a')
                # f.write(str(self.username + '\n'))
                f.write(str(self.i) + '\n')
                f.close()

                self.exit()

    def exit(self):
        fouth_delay = random.randint(20, 30)
        self.driver.delete_all_cookies()
        time.sleep(fouth_delay)
        self.driver.quit()
        fouth_delay = random.randint(20, 30)
        time.sleep(fouth_delay)

    def like_post(self):
        print("liking")
        try:
            # like_buttons = self.driver.find_elements(By.CLASS_NAME,
            #                                          "oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.pq6dq46d.btwxx1t3.abiwlrkh.p8dawk7l.lzcic4wl.gokke00a")
            like_buttons = self.driver.find_elements(By.CLASS_NAME,
                                                     "qi72231t.o9w3sbdw.nu7423ey.tav9wjvu.flwp5yud.tghlliq5.gkg15gwv.s9ok87oh.s9ljgwtm.lxqftegz.bf1zulr9.frfouenu.bonavkto.djs4p424.r7bn319e.bdao358l.fsf7x5fv.tgm57n0e.jez8cy9q.s5oniofx.m8h3af8h.l7ghb35v.kjdc1dyq.kmwttqpk.dnr7xe2t.aeinzg81.srn514ro.oxkhqvkx.rl78xhln.nch0832m.om3e55n1.cr00lzj9.rn8ck1ys.g4tp4svg.o9erhkwx.dzqi5evh.hupbnkgi.hvb2xoa8.fxk3tzhb.jl2a5g8c.f14ij5to.l3ldwz01.icdlwmnq.azwomqv7")

            for like_button in like_buttons:
                cheker_like = like_button.get_attribute("aria-label")
                print(cheker_like)
                if cheker_like == "Like":
                    time.sleep(fouth_delay)
                    like_button.click()
                    self.driver.implicitly_wait(30)
                    time.sleep(third_delay)

                    break
                else:
                    pass

        except Exception as e:
            print(e)

    def comment_post(self):

        time.sleep(first_delay)
        body = self.driver.find_element(By.TAG_NAME, 'body')
        try:

            comment_buttons = self.driver.find_elements(By.CLASS_NAME,
                                                        "oo9gr5id.lzcic4wl.l9j0dhe7.gsox5hk5.notranslate")
            for comment_button in comment_buttons:
                cheker_comment = comment_button.get_attribute("aria-label")
                if cheker_comment == "Write a comment":
                    # page down
                    time.sleep(first_delay)
                    comment_button.click()
                    time.sleep(third_delay)
                    print(self.comment)
                    comment_button.send_keys(self.comment)
                    time.sleep(third_delay)
                    self.driver.implicitly_wait(30)
                    time.sleep(first_delay)
                    comment_button.send_keys(Keys.ENTER)
                    self.track_comment = self.track_comment + 1
                    with open('comment_track.txt', 'w') as f:
                        f.write(str(self.track_comment))
                        print("comment track : ", self.track_comment)

                    body.send_keys(Keys.PAGE_DOWN)
                    time.sleep(third_delay)
                    self.driver.implicitly_wait(30)
                else:
                    pass

        except Exception as e:
            print(e)

    def share_post(self):
        # time.sleep(first_delay)
        print("I am in share")
        body = self.driver.find_element(By.TAG_NAME, 'body')
        # share_buttons = self.driver.find_elements(By.CLASS_NAME,
        #                                           "oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.pq6dq46d.btwxx1t3.abiwlrkh.p8dawk7l.lzcic4wl")
        share_buttons = self.driver.find_elements(By.CLASS_NAME,
                                                  "qi72231t.o9w3sbdw.nu7423ey.tav9wjvu.flwp5yud.tghlliq5.gkg15gwv.s9ok87oh.s9ljgwtm.lxqftegz.bf1zulr9.frfouenu.bonavkto.djs4p424.r7bn319e.bdao358l.fsf7x5fv.tgm57n0e.jez8cy9q.s5oniofx.m8h3af8h.l7ghb35v.kjdc1dyq.kmwttqpk.dnr7xe2t.aeinzg81.srn514ro.oxkhqvkx.rl78xhln.nch0832m.om3e55n1.cr00lzj9.rn8ck1ys.s3jn8y49.g4tp4svg.o9erhkwx.dzqi5evh.hupbnkgi.hvb2xoa8.fxk3tzhb.jl2a5g8c.f14ij5to.l3ldwz01.icdlwmnq")
        try:
            for share_button in share_buttons:
                time.sleep(first_delay)
                checker_share = share_button.get_attribute("aria-label")

                print(checker_share)
                if checker_share == "Send this to friends or post it on your Timeline." or "Send this to friends or post it on your" in checker_share:
                    print("    SHARE NOW      ")
                    third_delay = random.randint(5, 6)
                    time.sleep(third_delay)
                    print("SHARE NOW ")
                    share_button.click()
                    self.driver.implicitly_wait(30)
                    time.sleep(first_delay)
                    try:
                        self.driver.find_element(By.XPATH,"//span[contains(text(),'Share now (Friends)')]").click()
                    except Exception as e:
                        print(e)
                        try:
                             self.driver.find_element(By.XPATH,"//span[contains(text(),'Share now (Public)')]").click()
                        except Exception as e:
                            print(e)
                            try:
                                sharenows = self.driver.find_elements(
                                    By.CLASS_NAME, "goun2846.mk2mc5f4.ccm00jje.s44p3ltw.rt8b4zig.sk4xxmp2.n8ej3o3l.agehan2d.rq0escxv.j83agx80.buofh1pr.g5gj957u.i1fnvgqd.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.qt6c0cv9.l9j0dhe7.du4w35lb.bp9cbjyn.btwxx1t3.dflh9lhu.scb9dxdr")
                                self.driver.implicitly_wait(30)
                                for sharenow in sharenows:
                                    print(sharenow.text)
                                    if sharenow.text == "Share now (Public)" or sharenow.text == "Share now (Friends)":
                                        time.sleep(third_delay)
                                        sharenow.click()
                                        print("share now")
                                        self.driver.implicitly_wait(30)


                            except Exception as e:
                                print(e)
                        self.track_share = self.track_share + 1
                        with open('share_track.txt', 'w') as f:
                            f.write(str(self.track_share))
                            print("share track : ", self.track_share)

                        time.sleep(one_sec_delay)

                else:
                    pass
        except Exception as e:
            print(e)

    def scroll_up_down(self):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(one_sec_delay)
        body.send_keys(Keys.PAGE_UP)
        time.sleep(one_sec_delay)

    def chop_chop(self):
        stringg = self.link
        self.page = ''
        count = 0
        for val in stringg:
            self.page = self.page+val
            if "/" == val:
                count += 1

                if count == 4:
                    break

        print(self.page)

    def random_functions(self):

        self.driver.get(home_url)
        time.sleep(one_sec_delay)
        random_function = random.randint(1, 3)
        print(random_function)
        if random_function == 1:
            self.page_like_scroll()
        elif random_function == 2:
            self.Home_scroll()
        elif random_function == 3:
            self.scroll_up_down()

    def page_like_scroll(self):

        first_delay = random.randint(3, 5)
        third_delay = random.randint(15, 20)
        fouth_delay = random.randint(20, 30)
        like = 0
        self.driver.get(self.randomed_false_link)
        time.sleep(first_delay)
        like_amount = random.randrange(4, 9)
        print(" To like button " + str(like_amount))
        while True:
            if like == like_amount:
                break
            self.like_post()
            like = like+1

            time.sleep(fouth_delay)
            self.scroll_up_down()
            time.sleep(third_delay)

    def Home_scroll(self):

        first_delay = random.randint(3, 5)
        third_delay = random.randint(15, 20)
        fouth_delay = random.randint(20, 30)
        like = 0
        self.driver.get(home_url)
        time.sleep(first_delay)
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
                time.sleep(first_delay)
                self.share_post()
                time.sleep(second_delay)
            like = like+1
            print(like)
            time.sleep(fouth_delay)
            self.scroll_up_down()
            time.sleep(third_delay)

    def target_link_perform(self):
        second_delay = random.randint(2, 4)
        one_sec_delay = random.randint(4, 5)
        third_delay = random.randint(5, 9)
        time.sleep(second_delay)
        with open('link.txt', 'r') as f:
            self.link = f.read()
        print(self.link)
        self.driver.get(self.link)
        time.sleep(third_delay)
        self.like_post()
        time.sleep(third_delay)
        # self.share_post()
        # time.sleep(second_delay)
        # # only comment with persntage of account
        if self.percentile_comment == self.track_comment:
            print("not comment")
            self.share_post()
            pass
        else:
            time.sleep(third_delay)
            self.comment_post()
            time.sleep(third_delay)

        # self.comment_post()
        time.sleep(third_delay)
        if self.percentile_share == self.track_share:
            print("not share")
            pass
        else:
            self.share_post()
            time.sleep(third_delay)

        if self.percentile_comment == self.track_comment and self.percentile_share == self.track_share:
            print("not comment and share")
            time.sleep(third_delay)
            # close the browser and clear all the cookies
            # self.logout()
            # time.sleep(third_delay)
            # self.driver.delete_all_cookies()
            # time.sleep(third_delay)
            # self.driver.quit()

        # self.share_post()
        # if self.track_comment < int(self.percentile_comment+1):
        #     self.comment_post()
        #     self.share_post()
        # if self.track_share < int(self.percentile_share+1):
        #     self.comment_post()
        #     self.share_post()
        # else:
        #     pass

    def logout(self):
        print("I ABOUT TO LOG OUT . . .")
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.DOWN)
        self.driver.find_element(By.XPATH,
                                 "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/span[1]/div[1]/div[1]").click()
        self.driver.implicitly_wait(30)

        time.sleep(third_delay)
        self.driver.find_element(By.XPATH,
                                 "//span[contains(text(),'Log Out')]").click()
        self.driver.implicitly_wait(30)
        time.sleep(fouth_delay)
        self.driver.delete_all_cookies()

    def check(self):
        for _ in range(5):
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                
            self.driver.get("https://ident.me/")
            self.driver.implicitly_wait(10)
            ip_curr = self.driver.find_element(By.XPATH,
                "/html/body/pre").text
            print(ip_curr)
            if pc_ip != ip_curr:
               print("Now WE can pass Because IP is changed",
                      pc_ip + "!=" + ip_curr)
               time.sleep(second_delay)
               break
            else:
                print("Try again!!!")
                print(pc_ip + "==" + ip_curr)
                print("Waiting for seconds to check again")
                self.con_disable()
                time.sleep(fouth_delay)
                print("Intiate Browser to enable")
                self.conn_enable()
                time.sleep(first_delay)
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

        print("Enable . . . ")
        driver.get('http://192.168.8.1/html/home.html')
        time.sleep(10)
        xxx = driver.find_element(By.XPATH,
            '//*[@id="index_connection_status"]').text
        if xxx == 'Disconnected''\n' 'Connection Settings':
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, 
                "//span[@id='mobile_connect_btn']").click()
            print('Connecting to internet...')
            time.sleep(fouth_delay)
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
        time.sleep(first_delay)
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


login = social_media()

login.login()
