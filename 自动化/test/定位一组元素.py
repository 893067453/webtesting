from selenium import webdriver
import time

url = "https://gz.58.com/chuzu/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0000-351c-6b88-5fbce02eaf76&ClickID=2"

driver = webdriver.Chrome()

driver.get(url)

el_list = driver.find_elements_by_css_selector("li.house-cell> div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)")

print(el_list)

time.sleep(5)
driver.quit()

# li.house-cell> div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)