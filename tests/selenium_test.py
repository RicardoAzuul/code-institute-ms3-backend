import pytest
import time
from selenium import webdriver
# Keys allows for emulating keyboard keys
from selenium.webdriver.common.keys import Keys

chrome_driver = webdriver.Chrome(r'C:\Users\Richard Blaauw\code-institute-ms3-backend\dev\chromedriver')
chrome_driver.maximize_window()


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


def test_webapp_brand_nav():
    """
    GIVEN a running Heroku app
    WHEN the client clicks the brand nav
    THEN check the url ends with get_books
    """    
    chrome_driver.get('https://code-institute-ms3-book-review.herokuapp.com/')

    url = "https://code-institute-ms3-book-review.herokuapp.com/get_books"

    brand_href = chrome_driver.find_element_by_class_name("navbar-brand")
    brand_href.click()

    assert url == chrome_driver.current_url

# idea from code from https://stackoverflow.com/questions/12323403/how-do-i-find-an-element-that-contains-specific-text-in-selenium-webdriver-pyth
def test_webapp_all_books_nav():
    """
    GIVEN a running Heroku app
    WHEN the client clicks the All Books button
    THEN check the url ends with get_books
    """    
    chrome_driver.get('https://code-institute-ms3-book-review.herokuapp.com/')

    url = "https://code-institute-ms3-book-review.herokuapp.com/get_books"

    all_books_href = chrome_driver.find_element_by_xpath("//a[text()='All Books ']")
    all_books_href.click()

    assert url == chrome_driver.current_url


def test_webapp_log_in_nav():
    """
    GIVEN a running Heroku app
    WHEN the client clicks the Log In nav
    THEN check the url ends with login
    """    
    chrome_driver.get('https://code-institute-ms3-book-review.herokuapp.com/')

    url = "https://code-institute-ms3-book-review.herokuapp.com/login"

    log_in_href = chrome_driver.find_element_by_xpath("//a[text()='Log In']")
    log_in_href.click()

    assert url == chrome_driver.current_url


def test_webapp_register_nav():
    """
    GIVEN a running Heroku app
    WHEN the client clicks the Register nav
    THEN check the url ends with register
    """    
    chrome_driver.get('https://code-institute-ms3-book-review.herokuapp.com/')

    url = "https://code-institute-ms3-book-review.herokuapp.com/register"

    register_href = chrome_driver.find_element_by_xpath("//a[text()='Register']")
    register_href.click()

    assert url == chrome_driver.current_url


def test_webapp_log_in_url():
    """
    GIVEN a running Heroku app
    WHEN the client clicks the Log In link at the bottom of the Register page
    THEN check the url ends with login
    """    
    chrome_driver.get('https://code-institute-ms3-book-review.herokuapp.com/register')

    url = "https://code-institute-ms3-book-review.herokuapp.com/login"

    login_href = chrome_driver.find_element_by_xpath("//p/a[text()='Log In']")
    login_href.click()

    assert url == chrome_driver.current_url


def test_webapp_register_url():
    """
    GIVEN a running Heroku app
    WHEN the client clicks the Register link at the bottom of the Log In page
    THEN check the url ends with register
    """    
    chrome_driver.get('https://code-institute-ms3-book-review.herokuapp.com/login')

    url = "https://code-institute-ms3-book-review.herokuapp.com/register"

    login_href = chrome_driver.find_element_by_xpath("//p/a[text()='Register Your Account']")
    login_href.click()

    assert url == chrome_driver.current_url

    chrome_driver.close()
