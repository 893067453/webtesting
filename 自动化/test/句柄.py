from selenium import webdriver
import time

url = "https://www.baidu.com/"

driver = webdriver.Chrome()
driver.get(url)

print(driver.window_handles)
print(driver.current_url)
print("-----------------------------")

driver.find_element_by_partial_link_text("hao").click()
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()

print(driver.window_handles)
print(driver.current_url)
print("-----------------------------")

driver.switch_to.window(driver.window_handles[1])

time.sleep(3)
driver.close()

time.sleep(3)
driver.quit()