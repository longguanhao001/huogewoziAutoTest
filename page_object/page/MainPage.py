from selenium.webdriver.common.by import By
from appium import webdriver

from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage
from page_object.page.ProfilePage import ProfilePage
from page_object.page.SearchPage import SearchPage
from page_object.page.SelectPage import SelectedPage
from appium import webdriver




class MainPage(BasePage):
    _profile_button=(By.ID, "user_profile_icon")
    _search_button=(By.ID, "home_search")
    # def __init__(self):
    #     AndroidClient.restart_app()



    def gotoSelected(self):
        #调用全局的driver对象使用webdriver api操纵app
        # AndroidClient.driver.find_element(By.XPATH, "//*[@test='自选']")
        # AndroidClient.driver.find_element(By.XPATH, "//*[@test='自选']").click()
        # self.driver.find_element(By.XPATH, "//*[@test='自选']")
        # zixuan=(By.XPATH, "//*[@test='自选']")
        # self.find(zixuan)
        zixuan="自选"
        self.findByText(zixuan)
        self.findByText(zixuan).click
        # self.find(zixuan).click

        # 使用方法封装
        # self.driver.find_element_by_xpath( "//*[@test='自选']")
        # self.driver.find_element_by_xpath("//*[@test='自选']").click()
        return SelectedPage()

    def gotoSearch(self) -> SearchPage:

        self.find(self._search_button).click()
        return SearchPage()

    def gotoProfile(self):
        self.find(MainPage._profile_button).click()
        return ProfilePage()
