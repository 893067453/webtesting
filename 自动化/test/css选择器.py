from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://www.tmall.com/"

driver.get(url)

driver.find_element_by_css_selector(".inner-con2 > a:nth-child(2) > img:nth-child(1)").click()


time.sleep(5)
driver.close()
 # firepath :.inner-con2.clearfix>a>img
 # firebug:html.ks-gecko35.ks-gecko.ks-firefox35.ks-firefox body.w1230 div#mallPage.mui-global-biz-mallfp div#content div.main-nav div.inner-con0 div.inner-con1 div.inner-con2.clearfix a img