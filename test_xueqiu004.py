from calendar import WEDNESDAY
from lib2to3.pgen2 import driver
from pydoc import describe
from appium import webdriver
import pytest
from appium.webdriver.commom.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
import time
class TestXueqiuAndroid(object):
    driver=WebDriver
    @classmethod
    def setup_class(cls):
        print("setup class 在当前类下的所有用例执行之前只执行一次")

        cls.driver=cls.install_app()

    def setup_method(self):
        print("setup method 在每个测试用例执行之前执行一次")

        self.driver=self.restart_app()
        self.driver = self.driver


    def test_login(self):
        el1 = self.driver.find_element_by_id("user_profile_icon")
        el1.click()
        el2 = self.driver.find_element_by_id("tv_login")
        el2.click()
        el3 = self.driver.find_element_by_id("tv_login_by_phone_or_others")
        el3.click()

    def test_基金(self):
        self.driver.find_element_by_xpath()

    def test_swipe(self):
        self.driver.find_element_by_xpath()
        for i in range():
            self.driver.swipe(1000,1000,200,200)

    def test_action(self):
        self.driver.find_element_by_xpath()
        action=TouchAction(self.driver)
        for i in range(5):
            action.press(x=1000,y=1000).move_to(x=200,y=200).release().perform()
            time.sleep(20)

    def test_action_p(self):
        react=self.driver.get_window_rect()
        self.driver.find_element_by_xpath()
        action = TouchAction(self.driver)
        for i in range(5);
        action\
            .press(x=rect['width']*0.8,y=rect['height']*0.8).move_to(x=rect['width']*0.2,y=rect['height']*0.2)\
            .release()\
            .perform()
        time.sleep(2)

    def test_window_size(self):
        print(self.driver.get_window_rect)

    def teardown_method(self):
        self.driver.quit()

    @classmethod
    ddf install_app(cls) -> WebDriver:
    cpas={}
    # 如果有必要，进行第一次安装
    caps["platformName"] = "android"
    caps["deviceName"] = "long"
    caps["appPackage"] = "com.xueqiu.android"
    caps["appActivity"] = ".view.WelcomeActivityAlias"

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(10)
    return driver

    @classmethod
    def restart_app(cls) -> WebDriver:

        cpas={}
        caps["platformName"] = "android"
        caps["deviceName"] = "long"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 为了更快的启动，并保留之前的数据，从而可以保存上一个擦色执行后的状态
        caps['noReset']=True

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

       