from appium import webdriver
from appium.webdriver.webdriver import WebDriver

# 安装app、启动app并且返回一个全局变量
# from xueqiuaction003 import caps


class AndroidClient(object):
    driver:WebDriver
    @classmethod
    def install_app(cls) -> WebDriver:
        caps = {}
        # 如果有必要，进行第一次安装
        caps["platformName"] = "android"
        caps["deviceName"] = "long"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 解决第一次启动的问题
        caps["autoGrantPermissions"] = "true"
        # caps['noReset']=True
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def restart_app(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "long"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        caps['noReset'] = True
        # caps['chromedriverExecutableDir']="/user/seveniruby/projects/chromedriver/2.20"
        caps['chromedriverExecutableDir'] = "/user/seveniruby/projects/chromedriver/2.20"
        caps['unicodeKeyboard']=True
        caps['resetKeyboard']='True'

        #caps["uudi]="emulator-5554"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

    # def installApp(self):
    #     pass
    #
    # def restart(self):
    #     pass