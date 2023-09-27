from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from login_details import email, password
driver = webdriver.Firefox()
driver.get('https://tinder.com/')
try:
    sleep(2)
    cookies_btn = driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
    cookies_btn.click()
except:
    print('no cookies')
sleep(2)
login_btn = driver.find_element(
    By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_btn.click()
sleep(2)


def facebook_login():
    fb_btn = driver.find_element(
        By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
    fb_btn.click()
    sleep(2)
    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    email_in = driver.find_element(By.XPATH, '//*[@id="email"]')
    email_in.send_keys(email)
    password_in = driver.find_element(By.XPATH, '//*[@id="pass"]')
    password_in.send_keys(password)
    login_btn = driver.find_element(
        By.XPATH, '//*[@id="loginbutton"] //input[@type="submit"]')
    login_btn.submit()
    driver.switch_to.window(base_window)
    print('logged in')
    sleep(2)


facebook_login()
sleep(5)
try:
    allow_location_button = driver.find_element(
        'xpath', '/html/body/div[2]/main/div[1]/div/div/div[3]/button[1]')
    allow_location_button.click()
except:
    print('no location popup')
sleep(2)
try:
    allow_notification_button = driver.find_element(
        'xpath', '/html/body/div[2]/main/div/div/div/div[3]/button[2]')
    allow_notification_button.click()
except:
    print('no notification popup')
sleep(10)


def right_swipe():
    doc = driver.find_element('xpath', '//*[@id="Tinder"]/body')
    doc.send_keys(Keys.ARROW_RIGHT)


def left_swipe():
    doc = driver.find_element('xpath', '//*[@id="Tinder"]/body')
    doc.send_keys(Keys.ARROW_LEFT)


def auto_swipe():
    a = 0
    while True:
        sleep(2)
        try:
            right_swipe()
        except:
            a += 1
            print('match'+float(a))
            try:
                close_match()
            except:
                close = driver.find_element(
                    'xpath', '/html/body/div[2]/main/div/div[2]/button')
                close.click()
                print("error in auto swipe")
                driver.quit()


def close_match(self):
    match_popup = self.driver.find_element(
        'xpath', '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
    match_popup.click()
    sleep(2)
    match_profiles = driver.find_elements(
        'class name', 'matchListItem')
    if len(match_profiles) > 0:
        send_messages_to_matches(self)
    else:
        auto_swipe()


def get_matches():
    match_profiles = driver.find_elements('class name', 'matchListItem')
    message_links = []
    for profile in match_profiles:
        if profile.get_attribute('href') == 'https://tinder.com/app/my-likes' or profile.get_attribute('href') == 'https://tinder.com/app/likes-you':
            continue
        message_links.append(profile.get_attribute('href'))
    return message_links


def send_messages_to_matches():
    links = get_matches()
    for link in links:
        send_message(link)


def send_message(link):
    driver.get(link)
    sleep(2)
    contract_btn = driver.find_element(
        'xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/div/div[1]/button')
    contract_btn.click()
    sleep(2)
    snap_card = driver.find_element(
        'xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/div/div/div[1]/div[1]/div')
    snap_card.click()
    sleep(1)
    send_btn = driver.find_element(
        'xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button[2]')
    send_btn.click()
    sleep(1)
    driver.get('https://tinder.com/app/recs')
    auto_swipe()


try:
    print('swiping started')
    auto_swipe()
    # send_messages_to_matches()
except:
    print("error in auto swipe not started")
    driver.quit()
