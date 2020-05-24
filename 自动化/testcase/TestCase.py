import unittest
from Business.Login import Login
from CommonLib.common import Commonshare


class testCase(unittest.TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")

    def test001(self):
        # Commonshare().open_url("https://passport.58.com/login/?path=https%3A//gz.58.com/searchjob/%3Fspm%3D158447418345.zhaopin_baidu%26utm_source%3D12345%26pts%3D1589385391190&PGTID=0d302409-0000-3dc7-3442-de108e0dd40c&ClickID=5")
        # # Login().login("", "")
        # Commonshare().click_btn("css", "#mask_body_item_login")
        # data = Commonshare().get_text("css", "div.error_msg:nth-child(7) > label:nth-child(2)")
        # # self.assertEqual(data, "您还未输入用户名", "值不相等")
        Login().login("18665432732", "asd123456")
        # data = Commonshare().get_text("css", "div.error_msg:nth-child(7) > label:nth-child(2)")
        # assert data == "您还未输入密码", "值不相等"
        # Commonshare().click_btn("id", "mask_body_item_login")

    def test002(self):
        Login().login("18665432732", "asd123456")
        # data = Commonshare().get_text("css", "div.error_msg:nth-child(7) > label:nth-child(2)")
        # assert data == "您还未输入密码", "值不相等"
        # Commonshare().click_btn("id", "mask_body_item_login")


if __name__ == "__main__":
    unittest.main()
