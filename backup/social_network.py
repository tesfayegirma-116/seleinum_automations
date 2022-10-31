# import selinum
import threading
import openpyxl
from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys

first_delay = random.randint(1, 3)
second_delay = random.randint(2, 4)
one_sec_delay = random.randint(4, 5)
third_delay = random.randint(5, 6)
fouth_delay = random.randint(6, 9)
# create class and make function for login facebook using selinum


class social_media:
    def __init__(self, username, password):

        self.username = username
        self.password = password

        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(
                    executable_path=r"C:/Users/Meron/Desktop/meri/chromedriver", options=chrome_options)
        

        self.driver.get('https://www.facebook.com/')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(
            "//input[@id='email']").send_keys(self.username)
        time.sleep(one_sec_delay)
        self.driver.find_element_by_xpath(
            "//input[@id='pass']").send_keys(self.password)
        time.sleep(second_delay)
        self.driver.find_element_by_xpath(
            "//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/button[1]").click()
        self.driver.implicitly_wait(30)
        time.sleep(fouth_delay)
        self.driver.get('https://www.facebook.com/BelykBro')
        time.sleep(third_delay)

    def like_post(self):
        time.sleep(first_delay)
        body = self.driver.find_element_by_tag_name('body')
        screen_height = self.driver.execute_script(
            "return window.screen.height")
        i = 1
        while True:
            self.body = self.driver.find_element_by_tag_name('body')
            scroll_pause_time = 1
            i += 1
            time.sleep(scroll_pause_time)
            try:
                like_buttons = self.driver.find_elements_by_class_name(
                    "oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.pq6dq46d.btwxx1t3.abiwlrkh.p8dawk7l.lzcic4wl.gokke00a")

                for like_button in like_buttons:
                    cheker_like = like_button.get_attribute("aria-label")
                    if cheker_like == "Like":
                        time.sleep(fouth_delay)
                        like_button.click()
                        time.sleep(third_delay)
                        self.driver.implicitly_wait(30)
                        time.sleep(first_delay)
                    else:
                        pass
            except Exception as e:
                print(e)
            scroll_height = self.driver.execute_script(
                "return document.body.scrollHeight;")
            if (screen_height) * i > scroll_height:
                time.sleep(first_delay)
                continue

    def comment_post(self):
        time.sleep(first_delay)
        body = self.driver.find_element_by_tag_name('body')
        screen_height = self.driver.execute_script(
            "return window.screen.height")
        i = 1
        while True:
            self.body = self.driver.find_element_by_tag_name('body')
            scroll_pause_time = 1
            i += 1
            time.sleep(scroll_pause_time)
            try:
                comment_buttons = self.driver.find_elements_by_class_name(
                    "oo9gr5id.lzcic4wl.l9j0dhe7.gsox5hk5.notranslate")
                for comment_button in comment_buttons:
                    cheker_comment = comment_button.get_attribute("aria-label")
                    if cheker_comment == "Write a comment":
                        time.sleep(first_delay)
                        comment_button.click()
                        time.sleep(third_delay)

                        files = open("comment.txt", 'r')
                        comment = files.readline()
                        print(comment)
                        time.sleep(second_delay)
                        comment_button.send_keys(comment)

                        time.sleep(first_delay)
                    else:
                        pass

                time.sleep(fouth_delay)
            except Exception as e:
                print(e)
            scroll_height = self.driver.execute_script(
                "return document.body.scrollHeight;")
            if (screen_height) * i > scroll_height:
                time.sleep(first_delay)
                continue

    def share_post(self):
        time.sleep(first_delay)
        body = self.driver.find_element_by_tag_name('body')
        screen_height = self.driver.execute_script(
            "return window.screen.height")
        i = 1
        while True:
            self.body = self.driver.find_element_by_tag_name('body')
            scroll_pause_time = 1
            i += 1
            time.sleep(scroll_pause_time)
            share_buttons = self.driver.find_elements_by_class_name(
                "oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.pq6dq46d.btwxx1t3.abiwlrkh.p8dawk7l.lzcic4wl")
            try:
                for share_button in share_buttons:
                    checker_share = share_button.get_attribute("aria-label")
                    if checker_share == "Send this to friends or post it on your timeline.":
                        third_delay = random.randint(5, 6)
                        time.sleep(third_delay)
                        share_button.click()
                        time.sleep(one_sec_delay)
                        self.driver.find_element_by_xpath(
                            "//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
                        self.driver.implicitly_wait(30)

                        time.sleep(one_sec_delay)

                    else:
                        pass
            except Exception as e:
                print(e)
            scroll_height = self.driver.execute_script(
                "return document.body.scrollHeight;")
            if (screen_height) * i > scroll_height:
                time.sleep(first_delay)
                continue


workbook = openpyxl.load_workbook(filename="acc.xlsx")
sheet = workbook.active
username = sheet['A2'].value
password = sheet['B2'].value

login = social_media(username, password)

# run two method in one thread
t1 = threading.Thread(target=login.like_post)
t2 = threading.Thread(target=login.comment_post)
t3 = threading.Thread(target=login.share_post)

# #start two thread
t1.start()
t2.start()
t3.start()
