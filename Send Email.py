import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
browser = webdriver.Chrome()
def gmail_login():
    browser.get("https://www.gmail.com/")
    Email_Enter = browser.find_element_by_xpath('//*[@id="identifierId"]')
    Email_Enter.send_keys("cadets@larmans.com.au")
    Next_Button = browser.find_element_by_xpath('//*[@id="identifierNext"]/span')
    Next_Button.click()
    time.sleep(3)
    Password_Enter = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    Password_Enter.send_keys("larmans123")
    Next_Button2 = browser.find_element_by_xpath('//*[@id="passwordNext"]/span')
    Next_Button2.click()
    time.sleep(10)
def compose_email():
    Compose_Button = browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')
    Compose_Button.click()
    time.sleep(12)
    To_Email_Address = browser.find_element_by_name('to')
    Recipient_Email_Address = "ysoserious911@gmail.com"
    To_Email_Address.send_keys(Recipient_Email_Address)
    Subject = 'Testin for them BBH'
    Subject_Enter = browser.find_element_by_name('subjectbox')
    Subject_Enter.send_keys(Subject)
gmail_login()
compose_email()
    
