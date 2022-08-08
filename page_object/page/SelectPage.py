from appium import webdriver
from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage
from selenium.webdriver.common.by import By

class SelectedPage(BasePage):
    def addDefault(self):
        return self

    def gotoHS(self):
        self.findByText("沪深").click()
        return self
    def getPriceByName(self, name) -> float:
        #todo:
        # 使用priceLocator替换
        # self.driver\
        #     .find_element_by_xpath("//*[comtains(@resource-id,'stockName') and @text='"+name+"']"+
        #     "/../../..//*[contains(@resource-id),'currentPrice']").text
        priceLocator=(By.XPATH,"//*[comtains(@resource-id,'stockName') and @text='%s'])" %name +
                "/../../..//*[contains(@resource-id),'currentPrice')]")
        price=self.find(priceLocator).text
        return float(price)