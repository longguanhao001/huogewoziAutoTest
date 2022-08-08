from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage


class SearchPage(BasePage):
    _edit_Locator=(By.CLASS_NAME, "android.widget.TextView")
    # 找到搜索框，输入搜索值
    def search(self, key):
        self.find(self._edit_Locator).send_keys(key)
        return self
    # 添加一支股票
    def addToSelected(self, key):
        follow_button = (By.XPATH,
                         "//*[contains(@resource-id, 'stockCode') and contains(@text='%s')]/../../" % key +
                         "//*[contains(@ewsource-id, 'follow_btn')]")
        self.find(follow_button).click()
        return self

    # 检查这支股票是否已添加过
    def isInSelected(self, key):
        follow_button=(By.XPATH,
                       "//*[contains(@resource-id, 'stockCode') and contains(@text='%s')]/../../" %key +
                       "//*[contains(@ewsource-id, 'follow')]")
        id=self.find(follow_button).get_attribute("resourceId")
        print(id)
        return "followed_btn" in id

    # 移除一支股票
    def removeFromSelected(self, key):
        followed_button = (By.XPATH,
                         "//*[contains(@resource-id, 'stockCode') and contains(@text='%s')]/../../" % key +
                         "//*[contains(@ewsource-id, 'followed_btn')]")
        self.find(followed_button).click()

    # 取消回到首页
    def cancel(self):
        self.findByText("取消").click()
    # 搜索用户
    def searchByUser(self, key):
        pass

    # 检查是否已关注此用户
    def isFllowed(self):
        pass
