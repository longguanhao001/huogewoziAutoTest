
import pytest
from appium import webdriver
from page_object.page.MainPage import MainPage
from page_object.page.APP import App


class TestSelected(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage=App.main()

    def test_price(self):
        assert self.mainPage().gotoSelected().gotoHS().getPriceByName("兴业银行") == 19.75

