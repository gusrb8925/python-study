from selenium.webdriver.common.keys import Keys
from selenium import webdriver

browser = webdriver.Chrome()  # "./chromedriver.exe" 같은경로에 있을 때
browser.get("https://www.naver.com/")

# elem = browser.find_element_by_class_name("link_login")
# elem.click()
# browser.back()
# browser.forward()
# browser.refresh()
# browser.back()
elem = browser.find_element_by_id("query")
elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
# elem = browser.find_element_by_name("q")
# elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
# elem.click()
# browser.quit()
