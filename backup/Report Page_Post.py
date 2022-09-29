import datetime
import os
import sys

import xlrd
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random

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




print('PRESS 1 : FOR ACCOUNT OR PAGE')
print('PRESS 2: FOR POST ::THEN PRESS ENTER')

tab = input('>>> ')


try:
    os.makedirs(path, exist_ok=True)
    os.makedirs(path2, exist_ok=True)
    os.makedirs(path3, exist_ok=True)
    os.makedirs(links, exist_ok=True)
    files = [path + 'password.txt', path + 'sheetchange.txt', path + 'SUSP.txt', path + 'tryskip.txt',
             path + 'unknown.txt', path + 'VPN.txt', path + 'working.txt', path + 'precheck.txt', path + 'dvalue.txt',
             path + 'pages.txt',
             links + 'Reportlink.txt']
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

chrome_options = Options()
prefs = {"profile.default_content_setting_values.geolocation": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")
#########################################################################
driver2= webdriver.Chrome(
    executable_path="C:/Users/user/Desktop/weldrive/chromedriver", options=chrome_options)
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
        time.sleep(2)
        pc_ip = driver2.find_element_by_xpath("/html/body/pre").text
        pass
    time.sleep(3)
    driver2.quit()
    print("2nd")
class shareeverywhere(object):
    def read_tryskip(self):
        try:
            with open(tryskip, 'r') as fff:
                lines_next = fff.readlines()
                last_line_next = lines_next[-1]

        except Exception as e:
            print(e)
            last_line_next = 0
        print(last_line_next)
        self.tryskip_value = int(last_line_next)

    def read_accounts(self):
        print("reading accounts...")
        accountpath = desktoppath + "/Facebook/LSC/passuser.xlsx"
        commentpath = desktoppath + "/Facebook/LSC/comment.xlsx"
        self.wb_acc = xlrd.open_workbook(str(accountpath))
        self.wb_comm = xlrd.open_workbook(str(commentpath))
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
        self.read_tryskip()
        self.read_accounts()
        self.read_link()
        print("login procedure started ...")
        print("tryskip value " + str(self.tryskip_value))
        self.looper = self.tryskip_value + 1
        self.accounts_end = self.sheet.nrows + 1
        for self.i in range(self.looper, self.accounts_end):
            print(self.i)
            random_prof = int(random.randrange(2, 5))
            print("randomizer : " + str(random_prof))

            x = self.sheet.nrows * random_prof
            print(" ip_changer value : " + str(x))

            if x % 3 == 0:
                print("procedure changing Ip initiated ....")
                self.con_disable()
                self.conn_enable()
                self.check()
            else:
                pass

            try:
                self.username = self.sheet.cell_value(self.i, 0)
                self.password = self.sheet.cell_value(self.i, 1)

                self.comment = self.sheet_comm.cell_value(self.i, 0)

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
            self.driver = webdriver.Chrome(executable_path=desktoppath + "/weldrive/chromedriver",
                                           options=chrome_options)
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
            # self.ProfileLiker()
            currenturl = self.driver.current_url
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

                    if x % 3 == 0:
                        print(" randomizer : " + str(x))
                        self.ProfileLiker()
                    else:
                        self.page_scroll()


                    if tab=="1":
                        self.Report_page()
                    else:
                        self.Report_post()


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

        home_time = random.uniform(0.1, 5.5)
        scroll_speed = random.uniform(0.1, 1.5)
        cous = 0
        like_amount = random.randrange(1, 6)
        liked = 0
        tre = 0  # error counter - if error 3x in a row, will refresh page
        i = 0  # index of like element in newsfeed
        self.driver.get(url)
        body_elem = self.driver.find_element_by_tag_name('body')
        print("Going to like", like_amount, "photos.")
        x = like_amount
        print(x)
        time.sleep(little_delay)
        self.likes = self.driver.find_elements_by_class_name(
            "oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.pq6dq46d.btwxx1t3.abiwlrkh.p8dawk7l.lzcic4wl.gokke00a")
        for self.rr in self.likes:
            self.ee = self.rr.get_attribute('aria-label')
            if self.ee == "Like":
                self.rr.click()
            else:
                pass
        while liked <= like_amount:
            print("Liked", liked, "/", like_amount)
            try:
                if i > 25:
                    print("Let's reload")
                    self.driver.get("http://www.facebook.com")
                    time.sleep(5)
                    i = 0


                if (random.randint(1, 100) < 67):
                    print("liking")
                    try:
                        try:
                            self.rr.click()
                        except:
                            pass


                        n = random.randint(1, 310)
                        n = n / 100
                        print(n, 3 ** n)

                        time.sleep(3 ** n)
                    except:
                        print("cant click")
                        time.sleep(home_time)
                        i += 1
                        body_elem.send_keys(Keys.ESCAPE)
                        time.sleep(home_time)
                        body_elem.send_keys(Keys.DOWN)
                        time.sleep(home_time)
                        body_elem.send_keys(Keys.DOWN)
                        time.sleep(home_time)
                        body_elem.send_keys(Keys.DOWN)
                        time.sleep(home_time)
                        body_elem.send_keys(Keys.DOWN)
                        time.sleep(home_time)
                        body_elem.send_keys(Keys.DOWN)

                else:
                    print("skipping")
                    i += 1
                try:
                    discover_el = self.driver.find_elements_by_xpath('//*[@id="appsNav"]/h4')
                except:
                    print("Couldn't locate the left panel placeholder. Terminating.")
                    time.sleep(home_time)
                    break
            except Exception as e:
               pass

    def page_scroll(self):

        little_delay = random.uniform(3, 10)
        small_delay = random.uniform(8, 18)
        print("page scroll")
        time.sleep(little_delay)

        self.driver.get(self.links[0])
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
            # try:
            #     for cc in range(int(like_rand)):
            #         self.buttonlike = self.driver.find_element_by_xpath(
            #             "//body[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[" + str(
            #                 cc) + "]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
            # except Exception as e:
            #     print(e)
            #     pass
            time.sleep(little_delay)
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
            body_elem.send_keys(Keys.PAGE_UP)

    def read_link(self):

        with open(link1, 'r') as fff:
            self.links = fff.readlines()


        print(self.links)

    def conn_enable(self):
        chrome_options = Options()
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")
        driver4 = webdriver.Chrome(
            executable_path="C:/Users/user/Desktop/weldrive/chromedriver", options=chrome_options)
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

            pass
        else:
            driver4.quit()
            pass

    def con_disable(self):
        chrome_options = Options()
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")
        driver5 = webdriver.Chrome(
            executable_path="C:/Users/user/Desktop/weldrive/chromedriver", options=chrome_options)
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
        chrome_options = Options()
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")
        for _ in range(10):
            chrome_options = Options()
            prefs = {"profile.default_content_setting_values.geolocation": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-popup-blocking")
            driver6 = webdriver.Chrome(
                executable_path="C:/Users/user/Desktop/weldrive/chromedriver", options=chrome_options)
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

    def logout(self):
        time.sleep(little_delay)
        self.driver.get(url)
        time.sleep(little_delay)
        self.driver.implicitly_wait(20)
        try:

            self.acc = self.driver.find_elements_by_class_name(
                "oajrlxb2.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.nhd2j8a9.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.i1ao9s8h.esuyzwwr.f1sip0of.abiwlrkh.p8dawk7l.lzcic4wl.bp9cbjyn.s45kfl79.emlxlaya.bkmhp75w.spb7xbtv.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.j83agx80.taijpn5t.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.qypqp5cg.q676j6op.tdjehn4e")
            for self.accd in self.acc:
                self.accounts = self.accd.get_attribute("aria-label")
                print(self.accounts)
                if self.accounts == "Account":
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

    def Report_post(self):
        self.driver.get(self.links[1])
        time.sleep(little_delay)
        mensu= self.driver.find_elements_by_class_name("oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.pq6dq46d.mg4g778l.btwxx1t3.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.abiwlrkh.p8dawk7l.dwo3fsh8.pzggbiyp.pkj7ub1o.bqnlxs5p.kkg9azqs.c24pa1uk.ln9iyx3p.fe6kdd0r.ar1oviwq.l10q8mi9.sq40qgkc.s8quxz6p.pdjglbur")
        for menu in mensu:
            finder=menu.get_attribute("aria-label")
            if finder == "Actions for this post":
                menu.click()
                time.sleep(little_delay)
                break

        self.driver.find_element_by_xpath("//span[contains(text(),'Find support or report post')]").click()
        time.sleep(little_delay)
        like_rand = random.randint(1, 3)
        if int(like_rand==1):

            try:
                self.driver.find_element_by_xpath("//span[contains(text(),'Hate Speech')]").click()
            except:
                self.driver.find_element_by_xpath("//span[contains(text(),'Race or Ethnicity')]").click()
                pass
        elif int(like_rand == 2):
                try:
                    self.driver.find_element_by_xpath("//span[contains(text(),'Social Caste')]").click()
                except:
                    self.driver.find_element_by_xpath("//span[contains(text(),'Violence')]").click()
                    pass


        else:
            try:
                self.driver.find_element_by_xpath("//span[contains(text(),'Religious Affiliation')]").click()
            except:
                self.driver.find_element_by_xpath("//span[contains(text(),'Terrorism')]").click()
                pass



        time.sleep(little_delay)
        self.driver.find_element_by_class_name("oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.pq6dq46d.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.l9j0dhe7.abiwlrkh.p8dawk7l.cbu4d94t.taijpn5t.k4urcfbm").click()

        time.sleep(little_delay)
        self.driver.find_element_by_xpath("//span[contains(text(),'Next')]").click()

        time.sleep(little_delay)
        self.driver.find_element_by_xpath("//span[contains(text(),'Done')]").click()
        time.sleep(little_delay)

    def Report_page(self):

        self.driver.get(self.links[0])
        time.sleep(little_delay)

        mees=self.driver.find_elements_by_class_name("oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.nhd2j8a9.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.abiwlrkh.p8dawk7l.lzcic4wl.rq0escxv.pq6dq46d.cbu4d94t.taijpn5t.l9j0dhe7.k4urcfbm")
        for mee in mees:
            ds=mee.get_attribute('aria-label')
            print(ds)

            if ds=="See Options":
                mee.click()
                time.sleep(little_delay)
                break

        time.sleep(little_delay)
        self.driver.find_element_by_xpath("//span[contains(text(),'Find support or report profile')]").click()
        time.sleep(little_delay)









        time.sleep(little_delay)

        try:
            self.driver.find_element_by_xpath("//span[contains(text(),'Fake Account')]").click()
            time.sleep(little_delay)
            self.er = self.driver.find_elements_by_class_name(
                "oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.nhd2j8a9.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.abiwlrkh.p8dawk7l.lzcic4wl.rq0escxv.pq6dq46d.cbu4d94t.taijpn5t.l9j0dhe7.k4urcfbm")
            for err in self.er:
                cerr = err.get_attribute('aria-label')
                if cerr == "Submit":
                    err.click()
                    time.sleep(little_delay)
                    self.driver.find_element_by_xpath("//span[contains(text(),'Next')]").click()
                    time.sleep(little_delay)

                    aa = self.driver.find_elements_by_class_name(
                        "a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7.ltmttdrg.g0qnabr5.ojkyduve")
                    for aaa in aa:
                        ee = aaa.text
                        if ee == "Hide":
                            aaa.click()
                            time.sleep(little_delay)
                            break
                    time.sleep(little_delay)


        except Exception as e:
            print(e)
            try:

                self.driver.find_element_by_xpath(
                    "//span[contains(text(),'Posting Inappropriate Things')]").click()
                time.sleep(little_delay)

            except Exception as e:
                print(e)

            pass



        sss=self.driver.find_elements_by_class_name("oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.pq6dq46d.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.l9j0dhe7.abiwlrkh.p8dawk7l.cbu4d94t.taijpn5t.k4urcfbm")
        for cc in sss:
            ss=cc.get_attribute('aria-label')
            print(ss)

            if ss == "Done":
                time.sleep(medium_delay)
                cc.click()
                time.sleep(little_delay)
                break




cc=shareeverywhere()
cc.read_tryskip()
cc.login()
