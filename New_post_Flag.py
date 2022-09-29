import time
import random
import pyfiglet
import webbrowser
from rich import print
from rich.console import Console
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

console = Console()

delay = random.randint(5, 20)


ascii_banner = pyfiglet.figlet_format(
    "N  E  W    P  O  S  T ")
console.print(ascii_banner, justify="left")


class NewPostFlag(object):

    def choose_method(self):

        self.open_new_TAb()
        self.refersh_for_content()

    def read_links(self):

        self.converted_list = []
        
        with open('./links/flagpagelink.txt', 'r') as file:
            self.lines_next = file.readlines()
            for element in self.lines_next:
                self.converted_list.append(element.strip())

            print(self.converted_list)
        self.x = len((self.lines_next))

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

        self.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=chrome_options)
        time.sleep(delay)
        self.y = self.x-1
        for _ in range(1, self.x):
            self.driver.execute_script("window.open('');")

        for i in range(self.x):
            self.driver.switch_to.window(self.driver.window_handles[i])
            time.sleep(delay)
            self.driver.get(self.converted_list[i])
            time.sleep(delay)

    def refersh_for_content(self):
        time.sleep(delay)

        while True:
            print("in while loop")
            for self.i in range(self.x):
                self.driver.switch_to.window(
                    self.driver.window_handles[self.i])
                time.sleep(delay)
                self.driver.refresh()
                time.sleep(delay)
                page_time = random.uniform(0.5, 4.5)
                body_elem = self.driver.find_element(By.TAG_NAME, 'body')
                body_elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(page_time)
                body_elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(page_time)
                body_elem.send_keys(Keys.PAGE_UP)
                time.sleep(page_time)
                body_elem.send_keys(Keys.PAGE_UP)
                times = self.driver.find_elements(
                    By.CLASS_NAME, "oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.b1v8xokw")
                for ttime in times:
                    sttime = ttime.get_attribute("aria-label")
                    print(sttime)
                    time.sleep(delay)

                    if sttime == "Just now":
                        print("flag just now")
                        self.web = self.driver.current_url
                        with open("./links/file.txt", "a+") as f:
                            f.writelines("\n")
                            f.writelines("New Post on " + self.web)
                            f.writelines("\n")
                            f.close()
                        webbrowser.open("./links/file.txt")
                        time.sleep(delay)
                        with open("file.txt", 'a') as fs:
                            fs.seek(0)
                            fs.truncate()
                            fs.close()

                    elif sttime == "1 min":
                        print("flag just now")
                        self.web = self.driver.current_url
                        with open("./links/file.txt", "a") as f:
                            f.writelines("\n")
                            f.writelines("New Post on " + self.web)
                            f.writelines("\n")
                            f.close()
                        webbrowser.open("./links/file.txt")
                        time.sleep(delay)
                        with open("./links/file.txt", 'a') as fs:
                            fs.seek(0)
                            fs.truncate()
                            fs.close()

                    elif sttime == "5 mins":
                        print("flag just now")
                        self.web = self.driver.current_url
                        with open("./links/file.txt", "a") as f:
                            f.writelines("\n")
                            f.writelines("New Post on " + self.web)
                            f.writelines("\n")
                            f.close()
                        webbrowser.open("./links/file.txt")
                        time.sleep(delay)
                        with open("./links/file.txt", 'a') as fs:
                            fs.seek(0)
                            fs.truncate()
                            fs.close()
                    else:
                        pass


start = NewPostFlag()
start.choose_method()
