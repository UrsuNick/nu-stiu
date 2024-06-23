from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep 
driver = Chrome()
url_register="https://nu-stiu.vercel.app/register"
for i in range (1,100):
    
    driver.get(url_register)
    username_element = driver.find_element(By.NAME,"username")
    username_element.send_keys(f"test{i}")
    password_element = driver.find_element(By.CSS_SELECTOR,"body > form > input[type=password]:nth-child(2)")
    password_element.send_keys("test")
    submit_button = driver.find_element(By.CSS_SELECTOR,"body > form > button")
    submit_button.click()
sleep(5)