from PObject.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import ddt
import warnings
from time import sleep


@ddt.ddt()
class RegisterTestcase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.reg_url = "file:///F:/workspace/Webtesting/register/jQueryReg/index.html"
        self.driver = webdriver.Chrome()
        self.driver.get(self.reg_url)
        # self.driver.maximize_window()
        self.rb = RegisterBusiness(self.driver)

    def tearDown(self):
        self.driver.close()

    @ddt.data(
        # 邮箱 用户名 密码 手机号码
        ['zwjzsq@qq.com', 'zwjzs', '123456', '13800138000'],
        ['zwjzsq@qq.com', 'zwjzsq', '12345', '13800138000'],
        ['zwjzsq@qq.com', 'zwjzsq', '123456', '1380013800']
    )
    @ddt.unpack
    def test_register(self, email, name, password, mobile):
        self.rb.common_register(email, name, password, mobile)


if __name__ == '__main__':
    unittest.main()
