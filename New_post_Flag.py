import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
import webbrowser
url = 'https://www.facebook.com/'
path = "C:/Data/PageReport/"
path2 = "C:/Data/PersonalAccReport/"
path3 = "C:/Data/PagePromoteReport/"
links = "C:/Data/Tlink/"
pagelist = path + 'pages.txt'
tryskip = path + 'tryskip.txt'
sheetchange = path + 'sheetchange.txt'
working = path + 'working.txt'
dvalue = path + 'dvalue.txt'
linkss="flagpagelink.txt"
little_delay = random.uniform(3, 10)
small_delay = random.uniform(8, 18)
medium_delay = random.uniform(17, 35)
high_delay = random.uniform(120, 180)
home_time = random.uniform(2.5, 5.5)
scroll_speed = random.uniform(0.1, 1.5)
# pathfileaccountcontent="C:/Users/user/Desktop/Facebook/LSC/context.xlsx"
chrome_options = Options()
prefs = {"profile.default_content_setting_values.geolocation": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")

try:
    os.makedirs(path, exist_ok=True)
    os.makedirs(path2, exist_ok=True)
    os.makedirs(path3, exist_ok=True)
    os.makedirs(links, exist_ok=True)
    files = [path + 'password.txt', path + 'sheetchange.txt', path + 'SUSP.txt', path + 'tryskip.txt',
             path + 'unknown.txt', path + 'VPN.txt', path + 'working.txt', path + 'precheck.txt', path + 'dvalue.txt',
             path + 'pages.txt',
             links + 'flagpagelink.txt']
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



driver2= webdriver.Chrome(
    executable_path="/home/hope/Desktop/seli/chromedriver", options=chrome_options)
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

class NewPostFlag(object):


    def choose_method(self):

        self.open_new_TAb()
        self.refersh_for_content()

    def read_links(self):

        self.converted_list = []

        with open(linkss, 'r') as fff:
            self.lines_next = fff.readlines()
            print(self.lines_next)
            for element in self.lines_next:
                self.converted_list.append(element.strip())

            print(self.converted_list)
        self.x = len((self.lines_next))
        print(self.x)

    def open_new_TAb(self):

        self.read_links()

        chrome_options = Options()
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome(
            executable_path="/home/hope/Desktop/seli/chromedriver", options=chrome_options)
        time.sleep(little_delay)
        self.y=self.x-1
        for _ in range(1,self.x):
            self.driver.execute_script("window.open('');")


        for i in range(self.x):
            self.driver.switch_to.window(self.driver.window_handles[i])
            time.sleep(little_delay)
            self.driver.get(self.converted_list[i])
            time.sleep(little_delay)

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
            executable_path="/home/hope/Desktop/seli/chromedriver", options=chrome_options)
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
            executable_path="/home/hope/Desktop/seli/chromedriver", options=chrome_options)
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
                executable_path="/home/hope/Desktop/seli/chromedriver", options=chrome_options)
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
            #     driver6.close()
            # if pc_ip != ip_curr:
            #     print("Now WE can pass")
            #     driver6.quit()
            #     time.sleep(4)
            #     break
            else:
                print("Try again!!!")
                driver6.quit()
                time.sleep(little_delay)
                self.con_disable()
                self.conn_enable()
                time.sleep(3)
                pass
        print("finished")

    def refersh_for_content(self):
        time.sleep(little_delay)


        while True:
            print("in while loop")
            for self.i in range(self.x):
                self.driver.switch_to.window(self.driver.window_handles[self.i])
                time.sleep(little_delay)
                self.driver.refresh()
                time.sleep(little_delay)
                page_time = random.uniform(0.5, 4.5)
                body_elem = self.driver.find_element_by_tag_name('body')
                body_elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(page_time)
                body_elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(page_time)
                body_elem.send_keys(Keys.PAGE_UP)
                time.sleep(page_time)
                body_elem.send_keys(Keys.PAGE_UP)
                times = self.driver.find_elements_by_class_name("oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.b1v8xokw")
                # self.hew=self.driver.find_element_by_class_name("oajrlxb2.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.nhd2j8a9.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.i1ao9s8h.esuyzwwr.f1sip0of.abiwlrkh.p8dawk7l.lzcic4wl.bp9cbjyn.s45kfl79.emlxlaya.bkmhp75w.spb7xbtv.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.j83agx80.taijpn5t.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.tv7at329.thwo4zme.tdjehn4e")
                for ttime in times:
                    sttime = ttime.get_attribute("aria-label")
                    print(sttime)
                    time.sleep(medium_delay)

                    if sttime == "Just now":
                        print("flag just now")
                        self.web=self.driver.current_url
                        with open("file.txt", "a") as f:
                            f.writelines("\n")
                            f.writelines("New Post on "+  self.web)
                            f.writelines("\n")
                            f.close()
                        webbrowser.open("file.txt")
                        time.sleep(high_delay)
                        with open("file.txt", 'a') as fs:
                            fs.seek(0)
                            fs.truncate()
                            fs.close()


                    elif sttime == "1 min":
                        print("flag just now")
                        self.web = self.driver.current_url
                        with open("file.txt", "a") as f:
                            f.writelines("\n")
                            f.writelines("New Post on " + self.web)
                            f.writelines("\n")
                            f.close()
                        webbrowser.open("file.txt")
                        time.sleep(high_delay)
                        with open("file.txt", 'a') as fs:
                            fs.seek(0)
                            fs.truncate()
                            fs.close()

                    elif sttime == "2 mins":
                        print("flag just now")
                        self.web = self.driver.current_url
                        with open("file.txt", "a") as f:
                            f.writelines("\n")
                            f.writelines("New Post on " + self.web)
                            f.writelines("\n")
                            f.close()
                        webbrowser.open("file.txt")
                        time.sleep(high_delay)
                        with open("file.txt", 'a') as fs:
                            fs.seek(0)
                            fs.truncate()
                            fs.close()
                    else:
                        pass

cc=NewPostFlag()
cc.choose_method()
