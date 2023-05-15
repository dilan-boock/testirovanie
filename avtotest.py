from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.by import By

link = "http://localhost:3000/"

driver = webdriver.Firefox()
driver.get(link)

ch1 = driver.find_element(By.ID, "p_logo")
ch2 = "Сделайте свой дом умнее себя - дайте роботам шанс!"

time.sleep(1)

if ch1 == ch2:
    print("Passed")
else:
    print("Failed")
