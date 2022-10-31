import sys

import xlrd
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import random
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from operator import itemgetter

import os

desktop = os.path.expanduser("~\Desktop")
print(desktop)
# Prints the string by replacing all
desktoppath=desktop.replace(" \ ",  " / ")
print(desktoppath)


little_delay = random.uniform(8, 30)
small_delay = random.uniform(8, 18)
medium_delay = random.uniform(17, 35)
high_delay = random.uniform(120, 180)
home_time = random.uniform(0.1, 5.5)
scroll_speed = random.uniform(0.1, 1.5)

url = 'https://www.facebook.com/'
path = "C:/Data/PageReport/"
path2 = "C:/Data/PersonalAccReport/"
path3 = "C:/Data/PagePromoteReport/"
links = "C:/Data/Tlink/"



pagelist = path + 'pages.txt'
tryskip = path + 'tryskip.txt'
sheetchange = path + 'sheetchange.txt'
working = path + 'working.txt'
notworking = path + 'notworking.txt'
dvalue = path + 'dvalue.txt'

link1 = links + 'link1.txt'


try:
    os.makedirs(path, exist_ok=True)
    os.makedirs(path2, exist_ok=True)
    os.makedirs(path3, exist_ok=True)
    os.makedirs(links, exist_ok=True)
    files = [path + 'password.txt',  path + 'SUSP.txt', path + 'tryskip.txt',
             path + 'unknown.txt',  path + 'working.txt', path + 'precheck.txt',

             links + 'link1.txt',
             links + 'link2.txt', links + 'link3.txt', links + 'link4.txt', links + 'link5.txt']
    for file in files:
        with open(file, "a") as a:
            a.close()
    files = [path2 + 'password.txt', path2 + 'sheetchange.txt', path2 + 'SUSP.txt', path2 + 'tryskip.txt',
             path2 + 'unknown.txt', path2 + 'VPN.txt', path2 + 'working.txt', path2 + 'dvalue.txt', path2 + 'pages.txt',
             path2 + 'precheck.txt']
    for file in files:
        with open(file, "a") as a:
            a.close()
    files = [path3 + 'password.txt', path3 + 'sheetchange.txt', path3 + 'SUSP.txt', path3 + 'tryskip.txt',
             path3 + 'unknown.txt', path3 + 'VPN.txt', path3 + 'working.txt', path3 + 'dvalue.txt', path3 + 'pages.txt',
             path3 + 'precheck.txt']
    for file in files:
        with open(file, "a") as a:
            a.close()
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)
link1 = links + 'link1.txt'
link2 = links + 'link2.txt'
link3 = links + 'link3.txt'
link4 = links + 'link4.txt'
link5 = links + 'link5.txt'





######################################################################
print("*" * 54)
print("*" * 11, "WELCOME AT FACEBOOK  MASS LIKER ,COMMENT AND SHARE PROGRAM ", "*" * 11)
print("*" * 54)
#####################################################################


# account selector input first
print('WOULD U LIKE TO RUN PERSONAL ACCOUNT ,PAGE PROMOTE OR PAGE? :PRESS')
print('PRESS 1 : FOR PAGE ::THEN PRESS ENTER')
# print('PRESS 2: FOR PERSONAL ACCOUNT ::THEN PRESS ENTER')
# print('PRESS 3 : FOR PAGE PROMOTE ::THEN PRESS ENTER')
tab = input('>>> ')
# THIS IS PATH SELECTOR FOR ALL PROJECTS ###########################

if tab == '1':
    pass




else:
    print('*****************INCORRECT VALUE********************')
    print("please Stop the Program and Rerun it by Entering the correct Value")
    print('')
    print('')
    print('WOULD U LIKE TO RUN PERSONAL ACCOUNT ,PAGE PROMOTE OR PAGE? :PRESS')
    print('PRESS 1 : FOR PAGE ::THEN PRESS ENTER')
    # print('PRESS 2: FOR PERSONAL ACCOUNT ::THEN PRESS ENTER')
    # print('PRESS 3 : FOR PAGE PROMOTE ::THEN PRESS ENTER')
    tab = input('>>> ')
    # THIS IS PATH SELECTOR FOR ALL PROJECTS ###########################
# ###############################################################################


# ###################################################################################


# check if it is new link or not to start the program from scratch
print('        IS THIS NEW LINK OR SAME LINK AS BEFORE ? :PRESS')
print('N OR n : IF IT IS NEW LINK ::THEN ENTER')
print('ANY-KEY: IF IT IS SAME LINK AS BEFORE ::THEN PRESS ENTER')
state = input('>>> ')
if state == 'n' or state == 'N':
    with open(tryskip, 'w') as tr:
        tr.close()
else:
    pass






chrome_options = Options()
prefs = {"profile.default_content_setting_values.geolocation": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")

driver2= webdriver.Chrome(
    executable_path="/home/hope/Desktop/seli/chromedriver", options=chrome_options)
time.sleep(little_delay)
driver2.get("https://ident.me/")
try:
    pc_ip = driver2.find_element_by_xpath("/html/body/pre").text
    print(pc_ip)
    if str(pc_ip).count('.') == 3:
        pass
    else:
        driver2.get('https://ifconfig.me/ip')
        time.sleep(2)
        pc_ip = driver2.find_element_by_xpath("/html/body/pre").text
        pass
    time.sleep(3)
    driver2.quit()
    print("1st")
except Exception as e:
    time.sleep(little_delay)
    driver2.get("https://whatismyipaddress.com/")
    driver2.implicitly_wait(10)
    pc_ip = driver2.find_element_by_xpath('//*[@id="ipv4"]/a').text
    print(pc_ip)
    if str(pc_ip).count('.') == 3:
        pass
    else:
        driver2.get('https://ifconfig.me/ip')
        time.sleep(small_delay)
        pc_ip = driver2.find_element_by_xpath("/html/body/pre").text
        pass
    time.sleep(little_delay)
    driver2.quit()
    print("2nd")


class FacebookLSC:

    def Check_Connection(self):
        driver = webdriver.Chrome(executable_path="/home/hope/Desktop/seli/chromedriver", options=chrome_options)
        driver.get(url)
        try:
            driver.implicitly_wait(30)
            fff = driver.find_element_by_xpath('//*[@id="main-message"]/h1').text
            if fff == 'Your connection is not private':
                driver.quit()

                while True:

                    self.con_disable()
                    self.conn_enable()

                    driver.get(url)
                    time.sleep(little_delay)
                    fff = driver.find_element_by_xpath('//*[@id="main-message"]/h1').text

                    if fff == 'Your connection is not private':
                        time.sleep(small_delay)

                        driver.quit()
                    else:
                        break



                pass
            else:
                pass
        except Exception as e:
            pass

    def read_tryskip(self):
        try:
            with open(tryskip, 'r') as fff:
                lines_next = fff.readlines()
                last_line_next = lines_next[-1]

        except Exception as e:
            print(e)
            last_line_next = 0
        print(last_line_next)
        self.tryskip_value=int(last_line_next)

    def read_accounts(self):
        print("reading accounts...")
        accountpath="accounts.xlsx"
        commentpath="exl_comments.xlsx"
        self.wb_acc = xlrd.open_workbook(str(accountpath))
        self.wb_comm=xlrd.open_workbook(str(commentpath))
        self.sheet = self.wb_acc.sheet_by_index(0)
        self.sheet_comm = self.wb_comm.sheet_by_index(0)
        print("number of rows" + str(self.sheet.nrows))
        print("number of comment rows" + str(self.sheet_comm.nrows))
        if self.sheet.nrows == 0:
            sys.exit()
        if self.sheet_comm.nrows == 0:
            sys.exit()
        else:
            pass

    def login(self):
        print("login procedure started ...")
        print("tryskip value "+ str(self.tryskip_value))
        self.looper=self.tryskip_value+1
        self.accounts_end=self.sheet.nrows+ 1
        for self.i in range( self.looper,self.accounts_end):
            print(self.i)
            random_prof = int(random.randrange(2, 5))
            print("randomizer : " + str(random_prof))

            x=self.sheet.nrows* random_prof
            print(" ip_changer value : " + str(x))

            if x%3 ==0:
                print("procedure changing Ip initiated ....")
                self.con_disable()
                self.conn_enable()
                self.check()
            else:
                pass

            try:
                self.username=self.sheet.cell_value(self.i, 0)
                self.password=self.sheet.cell_value(self.i, 1)

                self.comment=self.sheet_comm.cell_value(self.i, 0)

                print(self.username)
                print(self.password)
                print(self.comment)
                time.sleep(3)
            except Exception as e:
                print(e)
                sys.exit()

            chrome_options = Options()
            prefs = {"profile.default_content_setting_values.geolocation": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--incognito")
            self.driver = webdriver.Chrome(executable_path="/home/hope/Desktop/seli/chromedriver", options=chrome_options)
            time.sleep(little_delay)
            self.driver.get(url)

            time.sleep(little_delay)
            self.driver.find_element_by_id('email').send_keys(self.username)
            time.sleep(small_delay)
            self.driver.find_element_by_id('pass').send_keys(self.password)
            time.sleep(small_delay)
            try:
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_name('login').click()
            except Exception as e:
                print(e)

            time.sleep(little_delay)
            self.ProfileLiker()
            currenturl=self.driver.current_url
            print(currenturl)
            if currenturl == url:
                with open(tryskip, "a") as f:
                    f.writelines("\n")
                    f.writelines(str(self.username))
                    f.writelines("\n")
                    f.writelines(str(self.i))
                    time.sleep(little_delay)

                print("tab value: " + tab)
                if tab == str(1):
                    print("inside page ")

                    random_prof = int(random.randrange(3, 6))
                    print("randomizer : " + str(random_prof))

                    x = self.sheet.nrows * random_prof

                    if x %3==0:
                        print(" randomizer : " + str(x))
                        self.ProfileLiker()

                    self.insidepage()
                else:

                    with open(notworking, "a") as f:
                        f.writelines("\n")
                        f.writelines(str(self.username))
                        f.writelines("\n")
                        f.writelines(str(self.i))
                        time.sleep(little_delay)
                    self.driver.delete_all_cookies()
                    time.sleep(little_delay)
                    self.driver.quit()
                    n = random.randint(1, 310)
                    n = n / 100
                    print("sleeping for : " + str(3 ** n) + " seconds")
                    time.sleep(3 ** n)

                pass

    def ProfileLiker(self):
        cous = 0
        like_amount = random.randrange(1, 6)
        liked = 0

        body_elem = self.driver.find_element_by_tag_name('body')
        print("Going to like", like_amount, "photos.")
        x = like_amount
        print(x)
        breaker=0
        yy=int(random.randint(1, 10))
        print("yy :"+ str(yy))
        body_elem.send_keys(Keys.PAGE_DOWN)

        time.sleep(little_delay)
        self.likebuttons=self.driver.find_elements_by_class_name("oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.pq6dq46d.btwxx1t3.abiwlrkh.p8dawk7l.lzcic4wl.gokke00a")

        for vall in self.likebuttons:
            breaker = breaker + 1
            self.checker=vall.get_attribute("aria-label")
            print(self.checker)
            if self.checker =="Like":
                # vall.click()

                ActionChains(self.driver).move_to_element(vall).click(vall).perform()
                print("Let's reload")
                page_time = random.uniform(0.5, 4.5)
                page_time_a = random.uniform(0.3, 3.5)
                body_elem = self.driver.find_element_by_tag_name('body')
                body_elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(page_time)
                body_elem.send_keys(Keys.ARROW_DOWN)
                time.sleep(page_time_a)
                body_elem.send_keys(Keys.PAGE_DOWN)
                body_elem.send_keys(Keys.ARROW_DOWN)
                time.sleep(page_time_a)
                body_elem.send_keys(Keys.ARROW_DOWN)
                body_elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(page_time)
                body_elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(page_time_a)
                body_elem.send_keys(Keys.PAGE_UP)
                body_elem.send_keys(Keys.ARROW_UP)
                time.sleep(page_time)
                body_elem.send_keys(Keys.ARROW_DOWN)
                body_elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(page_time_a)
                body_elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(page_time)
                body_elem.send_keys(Keys.PAGE_UP)
                time.sleep(page_time)

                liked += 1
                n = random.randint(1, 310)
                n = n / 100
                print("sleeping for : " + str(3 ** n) + " seconds")
                time.sleep(3 ** n)

                print("liked " + str(liked))



            if breaker ==yy:
                print(breaker)
                print(yy)
                break
            else:
                print("skipping")
        n = random.randint(1, 310)
        n = n / 100
        print("sleeping for : " + str(3 ** n) + " seconds")
        time.sleep(3 ** n)

    def page_scroll(self):

        time.sleep(little_delay)
        page_time = random.uniform(0.5, 4.5)
        page_time_a = random.uniform(0.3, 3.5)
        try:
            body_elem = self.driver.find_element_by_tag_name('body')
            body_elem.send_keys(Keys.DOWN)
        except Exception as e:
            time.sleep(small_delay)
            body_elem = self.driver.find_element_by_tag_name('body')
            body_elem.send_keys(Keys.DOWN)
        scrol_len = random.randint(5, 9)
        for s in range(scrol_len):
            body_elem = self.driver.find_element_by_tag_name('body')
            body_elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(page_time)
            body_elem.send_keys(Keys.ARROW_DOWN)
            time.sleep(page_time_a)
            body_elem.send_keys(Keys.PAGE_DOWN)
            body_elem.send_keys(Keys.ARROW_DOWN)
            time.sleep(page_time_a)
            body_elem.send_keys(Keys.ARROW_DOWN)
            body_elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(page_time)
            body_elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(page_time_a)
            body_elem.send_keys(Keys.PAGE_UP)
            body_elem.send_keys(Keys.ARROW_UP)
            time.sleep(page_time)
            body_elem.send_keys(Keys.ARROW_DOWN)
            body_elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(page_time_a)
            body_elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(page_time)
            body_elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(page_time_a)
            body_elem.send_keys(Keys.ARROW_UP)
            time.sleep(page_time)
            body_elem.send_keys(Keys.ARROW_UP)
            time.sleep(page_time_a)
            body_elem.send_keys(Keys.ARROW_DOWN)
            time.sleep(page_time_a)
        body_elem.send_keys(Keys.HOME)
        n = random.randint(1, 310)
        n = n / 100
        print("sleeping for : " + str(3 ** n) + " seconds")
        time.sleep(3 ** n)
        # driver.get(webPage_link)


    def insidepage(self):
        try:
            print("inside")
            with open(link1, 'r') as fff:
                lines_next = fff.readlines()
                print(lines_next)

            self.page_link=lines_next[0]
            self.post_link=lines_next[1]

            print(self.page_link)
            print(self.post_link)
            #
            self.driver.get(self.page_link)
            time.sleep(little_delay)

            random_prof=int(random.randrange(1, 6))
            random_no_prof=int(random.randrange(1, 6))

            if random_prof==random_no_prof:
                print(random_prof)
                print(random_no_prof)
                print("procedure randomization initiated........")
                self.ProfileLiker()
            else:
                pass

            time.sleep(little_delay)


            self.page_scroll()
            time.sleep(little_delay)
            self.driver.get(self.post_link)

            time.sleep(little_delay)
            self.page_like_post()
            time.sleep(little_delay)
            self.page_share_post()
            time.sleep(little_delay)

            random_prof = int(random.randrange(3, 6))
            print("randomizer : " + str(random_prof))

            x = self.sheet.nrows * random_prof

            if x % 3 == 0:
                self.driver.get(url)
                time.sleep(little_delay)
                print(" randomizer : " + str(x))
                self.ProfileLiker()
            self.logout()
            time.sleep(high_delay)

        except Exception as e:
            print(e)

    def logout(self):
        time.sleep(little_delay)
        self.driver.get(url)
        time.sleep(little_delay)
        self.driver.implicitly_wait(20)
        try:

            self.acc =self.driver.find_elements_by_class_name("oajrlxb2.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.nhd2j8a9.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.i1ao9s8h.esuyzwwr.f1sip0of.abiwlrkh.p8dawk7l.lzcic4wl.bp9cbjyn.s45kfl79.emlxlaya.bkmhp75w.spb7xbtv.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.j83agx80.taijpn5t.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.qypqp5cg.q676j6op.tdjehn4e")
            for self.accd in self.acc:
                self.accounts=self.accd.get_attribute("aria-label")
                print(self.accounts)
                if self.accounts =="Account":
                    self.accd.click()
                    time.sleep(little_delay)
                    try:
                        self.driver.find_element_by_xpath("//span[contains(text(),'Log Out')]").click()

                    except Exception as e:
                        print(e)



        except Exception as e:
            print(e)

        time.sleep(little_delay)
        self.driver.delete_all_cookies()
        time.sleep(little_delay)
        self.driver.quit()
        n = random.randint(1, 310)
        n = n / 100
        print("sleeping for : " + str(3 ** n) + " seconds")
        time.sleep(3 ** n)


    def page_like_post(self):
        print("like passed")
        self.driver.implicitly_wait(30)
        # butts = driver.find_elements_by_css_selector("body._6s5d._71pn._-kb.segoe:nth-child(2) div.rq0escxv.l9j0dhe7.du4w35lb div.rq0escxv.l9j0dhe7.du4w35lb:nth-child(6) div.du4w35lb.l9j0dhe7.cbu4d94t.j83agx80 div.j83agx80.cbu4d94t.l9j0dhe7.jgljxmt5.be9z9djy div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb:nth-child(1) div.l9j0dhe7.dp1hu0rb.cbu4d94t.j83agx80:nth-child(1) div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0:nth-child(4) div.d2edcug0.oh7imozk.tr9rh885.abvwweq7.ejjq64ki:nth-child(1) div.du4w35lb.k4urcfbm.l9j0dhe7.sjgh65i0 div.du4w35lb.l9j0dhe7 div.lzcic4wl div.j83agx80.cbu4d94t div.rq0escxv.l9j0dhe7.du4w35lb div.j83agx80.l9j0dhe7.k4urcfbm div.rq0escxv.l9j0dhe7.du4w35lb.hybvsw6c.io0zqebd.m5lcvass.fbipl8qg.nwvqtn77.k4urcfbm.ni8dbmo4.stjgntxs.sbcfpzgs div.stjgntxs.ni8dbmo4.l82x9zwi.uo3d90p7.h905i5nu.monazrh9 div:nth-child(1) div.tvfksri0.ozuftl9m div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.ph5uu5jm.b3onmgus.e5nlhep0.ecm0bbzt.nkwizq5d.roh60bw9.mysgfdmx.hddg9phg div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.n8tt0mok.hyh9befq.iuny7tx3.ipjc6fyt:nth-child(1) > div.oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.pq6dq46d.mg4g778l.btwxx1t3.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.abiwlrkh.p8dawk7l:nth-child(1)")[0]
        butt = self.driver.find_elements_by_class_name(
            "oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.pq6dq46d.btwxx1t3.abiwlrkh.p8dawk7l.lzcic4wl.gokke00a")
        for bytts in butt:

            # butts = driver.find_elements_by_css_selector("body._6s5d._71pn._-kb.segoe:nth-child(2) div.rq0escxv.l9j0dhe7.du4w35lb div.rq0escxv.l9j0dhe7.du4w35lb:nth-child(6) div.du4w35lb.l9j0dhe7.cbu4d94t.j83agx80 div.j83agx80.cbu4d94t.l9j0dhe7.jgljxmt5.be9z9djy div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb:nth-child(1) div.l9j0dhe7.dp1hu0rb.cbu4d94t.j83agx80:nth-child(1) div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0:nth-child(4) div.d2edcug0.oh7imozk.tr9rh885.abvwweq7.ejjq64ki:nth-child(1) div.du4w35lb.k4urcfbm.l9j0dhe7.sjgh65i0 div.du4w35lb.l9j0dhe7 div.lzcic4wl div.j83agx80.cbu4d94t div.rq0escxv.l9j0dhe7.du4w35lb div.j83agx80.l9j0dhe7.k4urcfbm div.rq0escxv.l9j0dhe7.du4w35lb.hybvsw6c.io0zqebd.m5lcvass.fbipl8qg.nwvqtn77.k4urcfbm.ni8dbmo4.stjgntxs.sbcfpzgs div.stjgntxs.ni8dbmo4.l82x9zwi.uo3d90p7.h905i5nu.monazrh9 div:nth-child(1) div.tvfksri0.ozuftl9m div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.ph5uu5jm.b3onmgus.e5nlhep0.ecm0bbzt.nkwizq5d.roh60bw9.mysgfdmx.hddg9phg div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.n8tt0mok.hyh9befq.iuny7tx3.ipjc6fyt:nth-child(1) > div.oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.pq6dq46d.mg4g778l.btwxx1t3.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.abiwlrkh.p8dawk7l:nth-child(1)")[0]
            like_status1 = str(bytts.get_attribute('aria-label'))
            print("ok yes sir---" + like_status1)
            if like_status1 == "Like":
                try:
                    self.driver.implicitly_wait(20)
                    print("Liking........")
                    bytts.click()
                except Exception as ed:
                    print("inside exception")


            elif like_status1 == "Remove Like":
                print('already liked')
                pass
            break



    def page_share_post(self):

        little_delay = random.uniform(8, 30)
        time.sleep(little_delay)
        count=0
        while True:
            little_delay = random.uniform(8, 30)
            time.sleep(little_delay)
            self.share_butt=self.driver.find_elements_by_class_name("oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.pq6dq46d.btwxx1t3.abiwlrkh.p8dawk7l.lzcic4wl")
            for self.share_butts in self.share_butt:
                self.sharebutttt=self.share_butts.get_attribute('aria-label')
                print( self.sharebutttt)
                if self.sharebutttt =="Send this to friends or post it on your timeline." or self.sharebutttt == "Send this to friends or post it on your Timeline.":
                    self.share_butts.click()
                    time.sleep(little_delay)
                    break
            try:
                little_delay = random.uniform(8, 30)
                self.driver.find_element_by_xpath("//span[contains(text(),'Share to a group')]").click()
                time.sleep(little_delay)
                self.groups=self.driver.find_elements_by_class_name("d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.mdeji52x.a5q79mjw.g1cxx5fr.ekzkrbhg.oo9gr5id.hzawbc8m")
                time.sleep(little_delay)
                if count <21:
                    print(count)
                    self.groups[count].click()

                    time.sleep(little_delay)
                    self.postbut=self.driver.find_elements_by_class_name("oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.nhd2j8a9.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.abiwlrkh.p8dawk7l.lzcic4wl.rq0escxv.pq6dq46d.cbu4d94t.taijpn5t.l9j0dhe7.k4urcfbm")
                    for asd in self.postbut:
                        sd=asd.get_attribute("aria-label")
                        print(sd)
                        time.sleep(little_delay)
                        if sd =="Post":
                            time.sleep(little_delay)
                            asd.click()
                            time.sleep(little_delay)
                            break
                    time.sleep(little_delay)

                    try:
                        action = ActionChains(self.driver)
                        action.send_keys(Keys.ENTER).perform()
                    except Exception as e:
                        print(e)

                    self.driver.refresh()

                    time.sleep(little_delay)
                    count=count+1
            except Exception as e:
                print(e)

            if count >19:
                print("breaking...................")
                break
            else:
                pass















        # try:
        #     driver.implicitly_wait(30)
        #     driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div").click()
        # except Exception as e:
        #     try:
        #         driver.implicitly_wait(30)
        #         driver.find_element_by_xpath("//span[contains(text(),'Share to News Feed')]").click()
        #         time.sleep(little_delay)
        #         driver.find_element_by_xpath("//div[contains(text(),'Post')]").click()
        #     except Exception as d:
        #         print(d)
        #         pass
    def connect(self):
        driver3 = webdriver.Chrome(
    executable_path= "/home/hope/Desktop/seli/chromedriver", options=chrome_options)
        host = 'https://web.telegram.org/#/login'
        driver3.get(host)
        time.sleep(5)
        try:

            # mbs = driver3.find_element_by_xpath("//my-i18n[contains(text(),'Next')]").text
            # if mbs == 'Next':
            print('Connection Established!!!')
            driver3.quit()
        except Exception as e:
            for ok in range(20):
                time.sleep(small_delay)
                driver3.refresh()
                try:
                    mbs = driver3.find_element_by_xpath("//my-i18n[contains(text(),'Next')]").text
                    if mbs == 'Next':
                        print('Connection Established!!!')
                        break
                        pass
                except Exception as e:
                    if ok == 3 or ok == 6 or ok == 7:
                        try:
                            time.sleep(5)
                            driver3.implicitly_wait(10)
                            fff = driver3.find_element_by_xpath('//*[@id="main-message"]/h1').text
                            if fff == 'Your connection is not private':
                                driver3.quit()
                                driver3 =webdriver.Chrome(
                                            executable_path="/home/hope/Desktop/seli/chromedriver", options=chrome_options)
                                driver3.get('http://192.168.8.1/html/home.html')
                                time.sleep(5)
                                xxo = driver3.find_element_by_xpath('//*[@id="index_connection_status"]').text
                                if xxo == 'Disconnected''\n' 'Connection Settings':
                                    driver3.implicitly_wait(10)
                                    driver3.find_element_by_xpath("//span[@id='mobile_connect_btn']").click()
                                    time.sleep(5)
                                    print('Connecting to internet...')
                                    driver3.quit()
                                    self.connect()
                                    break
                                else:
                                    print(xxo)
                                    pass
                            else:
                                print(fff)
                                pass
                        except Exception as e:
                            print(driver3.current_url)
                            pass
                    if ok == 4:
                        self.con_disable()
                        driver4 =webdriver.Chrome(
                            executable_path= "/home/hope/Desktop/seli/chromedriver", options=chrome_options)
                        driver4.get('http://192.168.8.1/html/home.html')
                        time.sleep(10)
                        xxx = driver4.find_element_by_xpath('//*[@id="index_connection_status"]').text
                        if xxx == 'Disconnected''\n' 'Connection Settings':
                            driver4.implicitly_wait(10)
                            driver4.find_element_by_xpath("//span[@id='mobile_connect_btn']").click()
                            print('Connecting to internet...')
                            time.sleep(2)
                            driver4.quit()
                            time.sleep(medium_delay)
                            pass
                        else:
                            driver4.quit()
                            pass
                    print('loading')
                    driver3.refresh()
                    time.sleep(5)
                    pass
            driver3.quit()

    def conn_enable(self):
        driver4 = webdriver.Chrome(
            executable_path= "/home/hope/Desktop/seli/chromedriver", options=chrome_options)
        driver4.get('http://192.168.8.1/html/home.html')
        time.sleep(10)
        xxx = driver4.find_element_by_xpath('//*[@id="index_connection_status"]').text
        if xxx == 'Disconnected''\n' 'Connection Settings':
            driver4.implicitly_wait(10)
            driver4.find_element_by_xpath("//span[@id='mobile_connect_btn']").click()
            print('Connecting to internet...')
            time.sleep(2)
            driver4.quit()
            time.sleep(high_delay)
            self.connect()
            pass
        else:
            driver4.quit()
            pass

    def con_disable(self):
        driver5 = webdriver.Chrome(
    executable_path= "/home/hope/Desktop/seli/chromedriver", options=chrome_options)
        driver5.get('http://192.168.8.1/html/home.html')
        time.sleep(little_delay)
        xd = driver5.find_element_by_xpath('//*[@id="index_connection_status"]').text
        if xd == 'Disconnected''\n' 'Connection Settings':
            driver5.quit()
            pass
        else:
            driver5.implicitly_wait(10)
            driver5.find_element_by_xpath("//span[@id='mobile_connect_btn']").click()
            time.sleep(2)
            print('Connection disconnected')
            driver5.quit()

        time.sleep(medium_delay)

    def check(self):
        for _ in range(10):
            chrome_options = Options()
            prefs = {"profile.default_content_setting_values.geolocation": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-popup-blocking")
            driver6 = webdriver.Chrome(
                    executable_path= "/home/hope/Desktop/seli/chromedriver", options=chrome_options)
            try:
                driver6.get("https://ident.me/")
                driver6.implicitly_wait(10)
                ip_curr = driver6.find_element_by_xpath("/html/body/pre").text
                print(ip_curr)
            except Exception as h:
                driver6.get("https://whatismyipaddress.com/")
                driver6.implicitly_wait(10)
                ip_curr = driver6.find_element_by_xpath('//*[@id="ipv4"]/a').text
                time.sleep(3)
                driver6.close()
            if pc_ip != ip_curr:
                print("Now WE can pass")
                driver6.quit()
                time.sleep(4)
                break
            else:
                print("Try again!!!")
                driver6.quit()
                time.sleep(little_delay)
                self.con_disable()
                self.conn_enable()
                time.sleep(3)
                pass
        print("finished")




ss=FacebookLSC()
ss.read_tryskip()
ss.read_accounts()
ss.login()
