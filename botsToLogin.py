
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class bots :
    def __init__(self):
        pass
    def twoPhase(self,userName,passw):
        browser = webdriver.Firefox()
        url = "https://www.amazon.com/ap/signin/132-7298137-2634723?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%2F132-7298137-2634723%3Fie%3DUTF8%26%252AVersion%252A%3D1%26%252Aentries%252A%3D0"
        browser.get((url))

        # fill in username and hit the continue button for move to another page
        username = browser.find_element_by_id('ap_email')
        username.send_keys(userName)

        continueButton = browser.find_element_by_id('continue')
        continueButton.click()

        # wait for transition then continue to fill items
        password = WebDriverWait(browser, 8).until(EC.presence_of_element_located((By.NAME, "ap_password")))
        password.send_keys(passw)

        signInButton = browser.find_element_by_id('signInSubmit')
        signInButton.click()
    def onePhase(self,userName,passw):
        # if you want to change browser replace the browser variabel by th next comment
        #browser = webdriver.Chrome()
        browser = webdriver.Firefox()
        url = "https://en-gb.facebook.com/login/"
        browser.get(url)
        #Id attribute for email
        username = browser.find_element_by_id("email")
        #fill the username
        username.send_keys(userName)
        #Id attribute for password
        password = browser.find_element_by_id ("pass")
        #fill the password
        password.send_keys(passw)
        loginButton = browser.find_element_by_id("loginbutton")
        loginButton.click()
        browser.close()