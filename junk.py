
def connect(self):
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.geolocation": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--incognito")
            driver3 = webdriver.Chrome(
                executable_path=desktop + "/ChromeDriver", options=chrome_options)
            host = 'https://web.telegram.org/#/login'
            driver3.get(host)
            time.sleep(5)
            try:
                print('Connection Established!!!')
                driver3.quit()
            except Exception as e:
                for ok in range(20):
                    time.sleep(first_delay)
                    driver3.refresh()
                    try:
                        mbs = driver3.find_element_by_xpath(
                            "//my-i18n[contains(text(),'Next')]").text
                        if mbs == 'Next':
                            print('Connection Established!!!')
                            break
                            pass
                    except Exception as e:
                        if ok == 3 or ok == 6 or ok == 7:
                            try:
                                time.sleep(5)
                                driver3.implicitly_wait(10)
                                fff = driver3.find_element_by_xpath(
                                    '//*[@id="main-message"]/h1').text
                                if fff == 'Your connection is not private':
                                    driver3.quit()
                                    chrome_options = webdriver.ChromeOptions()
                                    prefs = {"profile.default_content_setting_values.geolocation": 2}
                                    chrome_options.add_experimental_option("prefs", prefs)
                                    chrome_options.add_argument("--disable-infobars")
                                    chrome_options.add_argument("--start-maximized")
                                    chrome_options.add_argument("--disable-notifications")
                                    chrome_options.add_argument("--disable-popup-blocking")
                                    chrome_options.add_argument("--incognito")
                                    driver3 = webdriver.Chrome(
                                        executable_path=desktop + "/ChromeDriver", options=chrome_options)
                                    driver3.get(
                                        'http://192.168.8.1/html/home.html')
                                    time.sleep(5)
                                    xxo = driver3.find_element_by_xpath(
                                        '//*[@id="index_connection_status"]').text
                                    if xxo == 'Disconnected''\n' 'Connection Settings':
                                        driver3.implicitly_wait(10)
                                        driver3.find_element_by_xpath(
                                            "//span[@id='mobile_connect_btn']").click()
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
                            driver4 = webdriver.Chrome(
                                executable_path=desktop + "/weldrive/chromedriver", options=chrome_options)
                            driver4.get('http://192.168.8.1/html/home.html')
                            time.sleep(10)
                            xxx = driver4.find_element_by_xpath(
                                '//*[@id="index_connection_status"]').text
                            if xxx == 'Disconnected''\n' 'Connection Settings':
                                driver4.implicitly_wait(10)
                                driver4.find_element_by_xpath(
                                    "//span[@id='mobile_connect_btn']").click()
                                print('Connecting to internet...')
                                time.sleep(2)
                                driver4.quit()
                                time.sleep(first_delay)
                                pass
                            else:
                                driver4.quit()
                                pass
                        print('loading')
                        driver3.refresh()
                        time.sleep(5)
                        pass
                driver3.quit()


def check(self):
        for _ in range(10):
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.geolocation": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-popup-blocking")
            driver6 = webdriver.Chrome(
                executable_path=desktop + "/ChromeDriver", options=chrome_options)
            try:
                driver6.get("https://ident.me/")
                driver6.implicitly_wait(10)
                ip_curr = driver6.find_element_by_xpath("/html/body/pre").text
                print(ip_curr)
            except Exception as h:
                driver6.get("https://whatismyipaddress.com/")
                driver6.implicitly_wait(10)
                ip_curr = driver6.find_element_by_xpath(
                    '//*[@id="ipv4"]/a').text
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
                time.sleep(first_delay)
                self.con_disable()
                self.conn_enable()
                time.sleep(3)
                pass
        print("finished")


def con_disable(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")
        driver5 = webdriver.Chrome(
            executable_path=desktop + "/ChromeDriver", options=chrome_options)
        driver5.get('http://192.168.8.1/html/home.html')
        time.sleep(first_delay)
        xd = driver5.find_element_by_xpath(
            '//*[@id="index_connection_status"]').text
        if xd == 'Disconnected''\n' 'Connection Settings':
            driver5.quit()
            pass
        else:
            driver5.implicitly_wait(10)
            driver5.find_element_by_xpath(
                "//span[@id='mobile_connect_btn']").click()
            time.sleep(2)
            print('Connection disconnected')
            driver5.quit()

        time.sleep(second_delay)


def conn_enable(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")
        driver4 = webdriver.Chrome(
            executable_path=desktop + "/weldrive/chromedriver", options=chrome_options)
        driver4.get('http://192.168.8.1/html/home.html')
        time.sleep(10)
        xxx = driver4.find_element_by_xpath(
            '//*[@id="index_connection_status"]').text
        if xxx == 'Disconnected''\n' 'Connection Settings':
            driver4.implicitly_wait(10)
            driver4.find_element_by_xpath(
                "//span[@id='mobile_connect_btn']").click()
            print('Connecting to internet...')
            time.sleep(2)
            driver4.quit()
            time.sleep(fouth_delay)
            self.connect()
            pass
        else:
            driver4.quit()
            pass
