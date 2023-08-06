from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")

driver.get("https://demoqa.com/")

print(driver.title)

driver.close()