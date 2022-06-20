from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&dsh=S2064324210%3A1654786178857174&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")
driver.maximize_window()
text=driver.find_element_by_id('firstName')
text.send_keys('sai')
text=driver.find_element_by_id('lastName')
text.send_keys('reddy')
text=driver.find_element_by_name('Username')
text.send_keys('itforfun1234')
text=driver.find_element_by_name('Passwd')
text.send_keys('Soft#2021')
text=driver.find_element_by_name('ConfirmPasswd')
text.send_keys('Soft#2021')
button = driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button/span')
button. click()
time.sleep(5)
text=driver.find_element_by_xpath('//*[@id="phoneNumberId"]')
text.send_keys(9952612436)
time.sleep(5)
button = driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
button. click()
time.sleep(10)



