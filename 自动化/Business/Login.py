from CommonLib.common import Commonshare


class Login(Commonshare):
    def login(self, user, pwd):
        self.open_url("https://passport.58.com/login/?path=https%3A//gz.58.com/searchjob/%3Fspm%3D158447418345.zhaopin_baidu%26utm_source%3D12345%26pts%3D1589385391190&PGTID=0d302409-0000-3dc7-3442-de108e0dd40c&ClickID=5")
        self.send_key("id", "mask_body_item_username", user)
        self.send_key("id", "mask_body_item_newpassword", pwd)
        self.click_btn("id", "mask_body_item_login")


if __name__ == '__main__':
    lg = Login()
    lg.login("18665432732", "asd123456")