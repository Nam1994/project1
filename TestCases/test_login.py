from selenium import webdriver
import  time

driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\Automation TESTER\pythonProject1\Drivers\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

elem =driver.find_element_by_id("username")
elem.send_keys("tomsmith")

elem= driver.find_element_by_id("password")
elem.send_keys("SuperSecretPassword!")

elem= driver.find_element_by_class_name("radius")
elem.click()

time.sleep(5)
driver.close()

