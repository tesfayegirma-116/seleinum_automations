# import time
# import random
# import requests
# import datetime
# import pyfiglet
# from rich import print
# from rich.console import Console
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# console = Console()
# delay = random.randint(3, 6)

# ascii_banner = pyfiglet.figlet_format(
#     "N  E  W    P  O  S  T ")
# console.print(ascii_banner, justify="left")


# class NewPostFlag(object):

    def choose_method(self):

        self.open_new_TAb()
        self.refersh_for_content()

    def read_links(self):

        self.converted_list = []

        with open('./links/flagpagelink.txt', 'r') as file:
            self.lines_next = file.readlines()
            for element in self.lines_next:
                self.converted_list.append(element.strip())
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
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=chrome_options)
        time.sleep(delay)
        self.y = self.x-1
        for _ in range(1, self.x):
            self.driver.execute_script("window.open('');")

        for i in range(self.x):
            self.driver.switch_to.window(self.driver.window_handles[i])
            time.sleep(10)
            self.driver.get(self.converted_list[i])
            time.sleep(delay)

    def refersh_for_content(self):
        time.sleep(delay)

        with console.status("[bold yellow] Searching New Post . . .") as status:
            while True:
                time.sleep(10)
                for self.i in range(self.x):
                    self.driver.switch_to.window(
                        self.driver.window_handles[self.i])
                    time.sleep(delay)
                    self.driver.refresh()
                    time.sleep(delay)
                    times = self.driver.find_elements(
                        By.CLASS_NAME, "x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.xt0b8zv.xo1l8bm")
                    for ttime in times:
                        body_elem = self.driver.find_element(
                            By.TAG_NAME, 'body')
                        body_elem.send_keys(Keys.ARROW_DOWN)
                        time.sleep(delay)
                        body_elem.send_keys(Keys.ARROW_UP)
                        time.sleep(delay)
                        sttime = ttime.text
                        print(sttime)
                        time.sleep(delay)

                        if sttime == "Just now" or sttime == "1m" or sttime == "2m" or sttime == "1 m" or sttime == "2 m":
                            self.links = [elem.get_attribute('href') for elem in times]
                            with open("./links/file.txt", 'a+') as f:
                                self.lines = f.readlines()
                                if self.lines[len(self.lines)-1] != self.links:
                                    try:
                                        print("Here is New Link -->   ",
                                            str(self.links[0]))
                                        with open("./links/file.txt", 'a+') as f:
                                            f.writelines("\nNew Post on " + self.links[0])
                                        time.sleep(delay)
                                        self.notify_tg_bot()
                                    except:
                                        pass
                        else:
                            pass

    def notify_tg_bot(self):
        bot_token = '5698535655:AAGfcd8MAvLMCZzgWEp7_2ZEiPCtsMgxzMs'
        bot_chatID = '-615901499'

        current_time = datetime.datetime.now().strftime(
            "Post Date : %Y/%m/%d" + '\n' + '\n' + "Post Time : %H:%M:%S")

        message_body = str(current_time) + '\n' + \
            "Here Is The Link  \N{thumbs up sign}   :" + \
            '\n' + str(self.links[0])
        send_text = 'https://api.telegram.org/bot' + bot_token + \
            '/sendMessage?chat_id=' + bot_chatID + \
            '&text=' + str(message_body)
        time.sleep(delay)
        try:
            requests.post(send_text)
            print("Bot Send Link --> ", str(self.links[0]))
        except:
            print("No Link Found")
            pass


# start = NewPostFlag()
# start.choose_method()
