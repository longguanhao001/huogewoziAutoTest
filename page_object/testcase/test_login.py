from page_object.page.APP import App
import pytest

class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.profilePage=App.main().gotoProfile()
    def setup_method(self):
        self.loginPage=self.profilePage.gotoLogin()

    @pytest.mark.parametrize("user, pw, msg", [
        ("156005347600", "1111111", "手机号码"),
        ("15600534760", "1111111", "手机号码"),
    ])
    def test_login_password(self, user, pw, msg):
        self.loginPage.loginByPassword("user", "pw")
        assert msg in self.loginPage.getErrorMsg()
        self.loginPage.back()

    def teardown_method(self):
        self.logingPage.back()