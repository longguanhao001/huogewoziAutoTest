# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import pytest

class TestXueqiuAndroid(object):
    def test_login(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "long"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)

        el3 = driver.find_element_by_id("com.xueqiu.android:id/stock_name_four")
        el3.click()
        el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView")
        el4.click()
        el5 = driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others")
        el5.click()

        # driver.quit()