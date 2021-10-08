import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get('https://google.com')
input = driver.find_element_by_name('q')
input.send_keys('Калькулятор')
input.send_keys(Keys.RETURN)

calc_input = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div')
calc_input.click()
calc_input.send_keys('(1+2)*3-40/5')
calc_input.send_keys(Keys.RETURN)

time.sleep(2)
driver.quit()
