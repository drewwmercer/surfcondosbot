from time import sleep
from selenium import webdriver

# Initializes Firefox and sets it as browser
browser = webdriver.Firefox()

# Goes to the IG URL
browser.get('https://www.instagram.com/')

# Gives you time to see it
sleep(8)

# Closes the browser
browser.close()
