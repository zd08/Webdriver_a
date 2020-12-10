# Webdriver_auto
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from flow_auto_path.test_element_path import test_path


class Main:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

        self.driver.get("http://192.168.9.165")
        self.now_handle = self.driver.current_window_handle
        self.driver = test_path(self.driver)


Main()
