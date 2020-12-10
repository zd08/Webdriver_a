# Webdriver_auto
from selenium.webdriver.remote.webdriver import WebDriver
import os
import time
from log.Log import info

class Screenshoot_web:
    def __init__(self,webdriver):
        self.webdriver:WebDriver = webdriver
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.path_screenshoot = os.path.join(self.path,str(time.strftime('%Y_%m_%d_%M_%I_%S' , time.localtime()))+'.png')
        # print(self.path_screenshoot)
    def screenshoot(self):
        try:
            self.webdriver.get_screenshot_as_file(self.path_screenshoot)
        except:
            info('截图失败')

if __name__ == "__main__":
    Screenshoot_web(1)
