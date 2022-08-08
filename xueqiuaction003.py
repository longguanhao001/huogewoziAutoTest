# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "long"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

driver.swipe(1000,1000,200,200)
"""
action.press(x=1000,y=1000).move_to(x=200,y=200).release().perform()
"""

# 获取屏幕的高度、宽度
def test_window_size(self):
    print(self.driver.get_window_rect())

