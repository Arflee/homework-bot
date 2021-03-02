import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pathlib

load_dotenv()

URL = os.getenv('URL')
DIARY_LOGIN = os.getenv('DIARY_LOGIN')
DIARY_PASSWORD = os.getenv('DIARY_PASSWORD')

path_to_driver = str(pathlib.Path().absolute()) + '/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=path_to_driver)
driver.get(URL)

login_element = driver.find_element_by_xpath('//*[@id="session_login"]')
password_element = driver.find_element_by_xpath('//*[@id="session_password"]')

login_element.send_keys(DIARY_LOGIN)
password_element.send_keys(DIARY_PASSWORD)
password_element.send_keys(Keys.ENTER)