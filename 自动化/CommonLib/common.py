from selenium import webdriver
import time


class Commonshare(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def open_url(self, url):
        self.driver.get(url)
        time.sleep(5)

    # 获取标签
    def get_element(self, locate_type, value):
        el = None
        if locate_type == 'id':
            el = self.driver.find_element_by_id(value)
        elif locate_type == 'class':
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == 'name':
            el = self.driver.find_element_by_name(value)
        elif locate_type == 'tag':
            el = self.driver.find_element_by_tag_name(value)
        elif locate_type == 'line_text':
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == 'partial':
            el = self.driver.find_element_by_partial_link_text(value)
        elif locate_type == 'css':
            el = self.driver.find_element_by_css_selector(value)
        elif locate_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
        if el is not None:
            return el

    # 输入内容
    def send_key(self, locate_type, value, content):
        self.get_element(locate_type, value).send_keys(content)

    # 点击
    def click_btn(self, locate_type, value):
        ell = self.get_element(locate_type, value)
        ell.click()

    # 获取文本
    def get_text(self, locate_type, value):
        data = self.get_element(locate_type, value).text
        return data

    def __del__(self):
        time.sleep(10)
        self.driver.close()