"""
页面对象类，用于实现业务流程，是整个POM设计核心
模板：URL 核心元素 核心业务

1.不同页面是不同URL来区分的 URL就是每个页面的地址
2.把定位方式写在配置文件里面

查询玩家页面，用于实现查询玩家业务流程
"""
import time

from selenium import webdriver

from Base.BasePage import BasePage
from PageObject.Login_page import LoginPage
from Util.ParseConfFile import ParseConfigFile
from Util.WebDriverWaitUtil import ExplicitWait


class SearchPlayerPage(BasePage):
    # # 调用解析ini配置文件方法
    par = ParseConfigFile()
    searchPlayerPage_Options = par.get_section("searchPlayer_page")

    # 从ini文件中读取定位元素，并切分
    # 元素-首页
    lt_homepage, le_homepage = searchPlayerPage_Options["sp_page.homepage"].split(":")
    # print(lt_homepage, le_homepage)

    # 元素-玩家管理
    lt_player_management, le_player_management = searchPlayerPage_Options["sp_page.player_management"].split(":")

    # 元素-查询玩家
    lt_search_player, le_search_player = searchPlayerPage_Options["sp_page.search_player"].split(":")

    # 元素-输入玩家ID
    lt_input_playerID, le_input_playerID = searchPlayerPage_Options["sp_page.input_player_id"].split(":")

    # 元素-点击查询
    lt_search_button, le_search_button = searchPlayerPage_Options["sp_page.search_click"].split(":")

    # 元素-添加经验值输入框
    lt_input_exp, le_input_exp = searchPlayerPage_Options["sp_page.add_exp"].split(":")

    # 元素-点击增加按钮
    lt_add_exp_button, le_add_exp_button = searchPlayerPage_Options["sp_page.exp_button"].split(":")

    element_homePage = (lt_homepage, le_homepage)  # 首页
    element_player_management = (lt_player_management, le_player_management)  # 玩家管理
    element_search_player = (lt_search_player, le_search_player)  # 查询玩家
    element_input_playerID = (lt_input_playerID, le_input_playerID)  # 输入ID
    element_search_button = (lt_search_button, le_search_button)  # 点击查询
    element_input_exp = (lt_input_exp, le_input_exp)  # 输入经验值
    element_add_exp_button = (lt_add_exp_button, le_add_exp_button)  # 点击增加按钮

    # 1.点击首页
    def click_homePage(self):
        try:
            # 添加显示等待
            ExplicitWait(self.driver, self.element_homePage)
            self.click(self.element_homePage)
            # time.sleep(5)
        except Exception as e:
            print(e)

    # 2.点击玩家管理
    def click_PlayerManagement(self):
        try:
            ExplicitWait(self.driver, self.element_player_management)
            self.click(self.element_player_management)
        except Exception as e:
            print(e)

    # 3.点击查询玩家
    def click_searchPlayer(self):
        try:
            ExplicitWait(self.driver, self.element_search_player)
            self.click(self.element_search_player)

        except Exception as e:
            print(e)

    # 4.输入玩家ID或者手机号
    def input_playerMessage(self, txt):
        ExplicitWait(self.driver, self.element_input_playerID)
        self.input(self.element_input_playerID, txt)
        time.sleep(5)

    # 5.点击查询按钮
    def click_search(self):
        ExplicitWait(self.driver, self.element_search_button)
        self.click(self.element_search_button)
        time.sleep(5)

    # 给玩家添加经验
    def input_exp(self, txt):
        ExplicitWait(self.driver, self.element_input_exp)
        self.input(self.element_input_exp, txt)

    # 6.点击增加按钮
    def add_exp_button(self):
        ExplicitWait(self.driver, self.element_add_exp_button)
        self.click(self.element_add_exp_button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://test.albcoininworld.com:9100/")
    login = LoginPage(driver)
    # time.sleep(15)
    # 添加隐式等待 替换强制等待
    # WebDriverWait(driver, 2).until(lambda driver: driver.login.input_username("admin"), "超时了")
    login.input_username("admin")
    login.input_password("123456")
    login.click_button()

    sp = SearchPlayerPage(driver)
    # sp.click_homePage() # 点击首页
    sp.click_PlayerManagement() # 点击玩家管理
    # sp.click_searchPlayer()
    time.sleep(30)
