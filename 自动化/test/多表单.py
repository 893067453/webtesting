from selenium import webdriver
import time

url = "https://mail.163.com/"

driver = webdriver.Chrome()

driver.get(url)

driver.find_element_by_id("switchAccountLogin").click()

frame = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[3]/div[4]/div[1]/div/iframe")
driver.switch_to.frame(frame)

driver.find_element_by_class_name("j-inputtext").send_keys("zhuweijie")
driver.find_element_by_class_name("dlpwd").send_keys("Zwj168726865*")

time.sleep(3)

driver.quit()

