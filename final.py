from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import xlrd

first_delay = random.randint(1, 3)
second_delay = random.randint(2, 4)
one_sec_delay = random.randint(4, 5)
third_delay = random.randint(5, 6)
fouth_delay = random.randint(6, 9)


class social_media():

    def login(self):

        self.wb_acc = xlrd.open_workbook(str('acc.xlsx'))
        self.wb_com = xlrd.open_workbook(str('exl_comments.xlsx'))
        self.sheet = self.wb_acc.sheet_by_index(0)
        self.sheetcom = self.wb_com.sheet_by_index(0)

        self.looper = self.sheet.nrows - 1
        for self.i in range(0, self.looper):
            self.username = self.sheet.cell_value(self.i, 0)
            self.password = self.sheet.cell_value(self.i, 1)

            self.comment = self.sheetcom.cell_value(self.i, 0)
            # initalize the webdriver
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.geolocation": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--incognito")
            self.driver = webdriver.Chrome(
                "C:/Users/Meron/Desktop/meri/chromedriver", options=chrome_options)

            # fill the login form and get to the home page
            self.driver.get('https://www.facebook.com/')
            time.sleep(second_delay)
            self.driver.find_element_by_xpath(
                "//input[@id='email']").send_keys(self.username)
            time.sleep(third_delay)
            self.driver.find_element_by_xpath(
                "//input[@id='pass']").send_keys(self.password)
            time.sleep(fouth_delay)
            self.driver.find_element_by_xpath(
                "//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/button[1]").click()
            time.sleep(third_delay)
            self.driver.implicitly_wait(30)
            time.sleep(fouth_delay)
            self.driver.get(
                'https://www.facebook.com/soynosoyMEME/posts/285360866283681:0')
            time.sleep(third_delay)

            self.like_post()
            self.share_post()
            self.comment_post()

            self.driver.quit()

    def like_post(self):
        try:
            like_buttons = self.driver.find_elements_by_class_name(
                "oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.pq6dq46d.btwxx1t3.abiwlrkh.p8dawk7l.lzcic4wl.gokke00a")

            for like_button in like_buttons:
                cheker_like = like_button.get_attribute("aria-label")
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
        body = self.driver.find_element_by_tag_name('body')
        try:

            comment_buttons = self.driver.find_elements_by_class_name(
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
                    body.send_keys(Keys.PAGE_DOWN)
                    time.sleep(third_delay)
                    self.driver.implicitly_wait(30)
                else:
                    pass

        except Exception as e:
            print(e)

    def share_post(self):
        time.sleep(first_delay)
        body = self.driver.find_element_by_tag_name('body')
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


login = social_media()

login.login()
