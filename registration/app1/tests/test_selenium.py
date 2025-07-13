import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


username = f"user_{datetime.now().strftime('%Y%m%d%H%M%S')}"
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture
def signup_url():
    return "http://127.0.0.1:8000" 

@pytest.fixture
def login_url():
    return "http://127.0.0.1:8000/login/"


def test_signup_is_functional(browser, signup_url, login_url):

    browser.get(signup_url)

    # Fill out the signup form
    browser.find_element(By.NAME, 'username').send_keys(username)
    browser.find_element(By.NAME, 'email').send_keys('bhals4@wgu.edu')
    browser.find_element(By.NAME, 'password1').send_keys('password')
    browser.find_element(By.NAME, 'password2').send_keys('password')

    # Submit the form
    browser.find_element(By.CSS_SELECTOR, 'button').click()

    # Wait for the redirect
    time.sleep(2)

    # Confirm we're on the login page
    assert browser.current_url == login_url


    # Inject visible confirmation message on the login page
    browser.execute_script(f"""
        const msg = document.createElement('div');
        msg.innerText = "✅ Signup completed for: {username} on {timestamp}";
        msg.style.position = 'fixed';
        msg.style.top = '10px';
        msg.style.left = '10px';
        msg.style.background = '#28a745';
        msg.style.color = 'white';
        msg.style.padding = '12px';
        msg.style.borderRadius = '6px';
        msg.style.zIndex = '9999';
        msg.style.fontSize = '16px';
        document.body.appendChild(msg);
    """)

    # Take a screenshot
    screenshot_name = f"registration_confirmation_{username}.png"
    browser.save_screenshot(screenshot_name)

    # Also print to the terminal
    print(f"\n Registration test completed for user: {username}")
    print(f" Date and Time: {timestamp}")
    print(f" WGU ID#: 011386373")
    print(f" Screenshot saved as: {screenshot_name}\n")


def test_sign_in(browser, login_url):
    
    browser.get(login_url)

    # Fill out the form
    browser.find_element(By.NAME, 'username').send_keys(username)
    browser.find_element(By.NAME, 'pass').send_keys('password')

    time.sleep(2)
    login_activity = f"login_activity_{username}.png"
    browser.save_screenshot(login_activity)
    
    # Submit the form
    browser.find_element(By.CSS_SELECTOR, 'button').click()

    # Wait for the redirect
    time.sleep(2)

    # Confirm we're on the home page
    assert browser.title == 'Home Page'

    # Take a screenshot
    screenshot_name = f"login_confirmation_{username}.png"
    browser.save_screenshot(screenshot_name)

    # Print to the terminal
    print(f"\n Login successful for: {username}")
    print(f" Date and time: {timestamp}")
    print(f" WGU ID#: 011386373")
    print(f" Screenshots saved as: {login_activity}, {screenshot_name}")
