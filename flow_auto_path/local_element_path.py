# Webdriver_auto
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from log.Log import info
import time
class Flow_element():
    def __init__(self,driver):
        self.driver:WebDriver = driver
        # print(self.driver)
    def location(self,location_method=None,locaton_element=None):
        try:
            if location_method != None and locaton_element != None:

                if location_method == 'css':
                    # print(locaton_element)
                    self.locat = self.driver.find_element(By.CSS_SELECTOR,locaton_element)

                elif location_method == 'xpath':
                    self.locat = self.driver.find_element(By.XPATH,locaton_element)
                elif location_method == 'id':
                    self.locat = self.driver.find_element(By.ID,locaton_element)
                else:
                    info("无定位方法")

            else:
                info('定位错误：%s %s'%(location_method,locaton_element))
        except Exception as e:
            info("定位失败：%s"%e)
    def operation(self,send_operation=None,data=None):
        try:
            if send_operation == 'send_keys' :
                self.locat.send_keys(Keys.CONTROL + 'a')
                self.locat.send_keys(Keys.BACKSPACE)
                if data != None:
                    self.locat.send_keys(data)
            elif send_operation == 'click':
                self.locat.click()
            elif send_operation == "backspace":#清空输入框
                self.locat.send_keys(Keys.CONTROL + 'a')
                self.locat.send_keys(Keys.BACKSPACE)
            elif send_operation == "actionchains":#鼠标悬停
                ActionChains(self.driver).move_to_element(self.locat).perform()
            elif send_operation == "refresh":
                self.driver.refresh()
            elif send_operation == "text":
                data_text = self.locat.text
                return data_text,self.driver
            elif send_operation == 'value':
                # print(self.driver.page_source)
                return [self.locat.get_attribute('value')]

        except Exception as e:
            info("操作失败:%s"%e)
