from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://pointerpointer.com/")
driver.maximize_window()
time.sleep(6)
point = driver.find_element(By.ID,"root")
print(point.size)
driver.implicitly_wait(10)
x = 0
y = 0
for i in range(500):
	actions = ActionChains(driver).move_by_offset(x, y).perform()
	x +=10
	y+=20
	time.sleep(4)

