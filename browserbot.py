import os

from time import sleep
from selenium import webdriver

IG_USERNAME = os.environ.get('IG_USERNAME')
IG_PASS = os.environ.get('IG_PASS')

# Initializes Firefox and sets it as browser
browser = webdriver.Firefox()

# Gets ready to look for the loaded element
browser.implicitly_wait(5)

# Goes to the IG URL
browser.get('https://www.instagram.com/')

# login_link = browser.find_element_by_xpath("//a[text()='Log In']")
# login_link.click()

# sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys(IG_USERNAME)
password_input.send_keys(IG_PASS)

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

# Gives you time to see it
sleep(8)

# Closes the browser
browser.close()
