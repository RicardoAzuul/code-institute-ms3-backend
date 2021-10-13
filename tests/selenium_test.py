import pytest
import time
from selenium import webdriver
# Keys allows for emulating keyboard keys
from selenium.webdriver.common.keys import Keys

chrome_driver = webdriver.Chrome(r'C:\Users\Richard Blaauw\code-institute-ms3-backend\dev\chromedriver')


def test_webapp_title():
    """
    GIVEN a running Heroku app
    WHEN the client browses to /
    THEN check the title is "Bookable"
    """    
    chrome_driver.get('https://code-institute-ms3-book-review.herokuapp.com/')

    title = "Bookable"
    assert title == chrome_driver.title


def test_webapp_register_existing_user():
    """
    GIVEN an existing username
    WHEN the client tries to register the existing username
    THEN check for the "Sorry, your username has already been taken!" flash message
    """    
    chrome_driver.get('https://code-institute-ms3-book-review.herokuapp.com/register')

    existing_user = "hank.schrader"
    password = "Passw0rd"

    username_element = chrome_driver.find_element_by_name("username")
    password_element = chrome_driver.find_element_by_name("password")
    register_button = chrome_driver.find_element_by_class_name("btn-primary")

    username_element.send_keys(existing_user)
    password_element.send_keys(password)
    register_button.click()

    assert "Sorry, your username has already been taken!" in chrome_driver.page_source

    chrome_driver.close()    

