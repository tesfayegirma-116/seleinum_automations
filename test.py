import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class Connection:
    def connect(self):
            self.driver = webdriver.Chrome(
                    executable_path="/home/hope/Desktop/seli/chromedriver")
            self.driver.get("https://ident.me/")
            try:
                self.pc_ip = self.driver.find_element_by_xpath("/html/body/pre").text
                print(self.pc_ip)
                if str(self.pc_ip).count('.') == 3:
                    pass
                else:
                    self.driver.get('https://ifconfig.me/ip')
                    time.sleep(2)
                    self.pc_ip = self.driver.find_element_by_xpath("/html/body/pre")
                    print(self.pc_ip)
                    pass
                time.sleep(3)
            except Exception as h:
                print(h)


    def check(self):
            for _ in range(1):
                chrome_options = webdriver.ChromeOptions()
                prefs = {"profile.default_content_setting_values.geolocation": 2}
                chrome_options.add_experimental_option("prefs", prefs)
                chrome_options.add_argument("--disable-infobars")
                chrome_options.add_argument("--start-maximized")
                chrome_options.add_argument("--disable-notifications")
                chrome_options.add_argument("--disable-popup-blocking")
                driver = webdriver.Chrome(
                    executable_path="/home/hope/Desktop/seli/chromedriver", options=chrome_options)
                
                try:
                    driver.get("https://ident.me/")
                    driver.implicitly_wait(10)
                    ip_curr = driver.find_element_by_xpath("/html/body/pre").text
                    self.connect()
                except Exception as h:
                    driver.get("https://whatismyipaddress.com/")
                    driver.implicitly_wait(10)
                    ip_curr = driver.find_element_by_xpath(
                        '//*[@id="ipv4"]/a').text
                    time.sleep(3)
                    driver.quit()
                if self.pc_ip != ip_curr:
                    print("Now WE can pass")
                    driver.quit()
                    time.sleep(4)
                    break
                else:
                    print("Try again!!!")
                    print(self.pc_ip, ip_curr)
                    time.sleep(3)
                    pass
            print("finished")


run = Connection()
run.check()



