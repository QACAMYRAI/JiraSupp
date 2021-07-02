from selenium import webdriver
import requests
import pickle

options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

options.add_argument("--disable-blink-features=AutomationControlled")

browser = webdriver.Chrome(options=options)

browser.implicitly_wait(3)

url = 'https://sso.fraglab.com/adfs/ls/?SAMLRequest=hZLNTsMwEIRfJfI9zV9Jg5VGCmkrVSoItcCBCzLuhho5dvA6Bd4eJxXQHignS%2BsZ73y7zpE1sqVlZ3dqDW8doPU%2BGqmQDhdT0hlFNUOBVLEGkFpON%2BX1isajkLZGW821JEeW8w6GCMYKrYi3nE3JUxqm8VV6MS8nUZmNq0VYZdk8LsfhZZykYTUn3gMYdPopcXZnQuxgqdAyZV0pjCM%2FnPhhdBdlNIlokjwSb%2BYYhGJ2cO2sbZEGAaIe1Ya9SPY84roJ2LbGQGJAvEorhP61c7n5QUR5Z4w7fdG0UnBhibfQhsMwvimpmUToQ946TrGHn0r5jd036xowGzB7weF%2BvfqN%2BCoMO8kIattqoWzQarRrwLYPQYq8HzMdJmGKv8x5cKzKD1u%2BcVzL2a120T%2F74A37B7uviK1fD1JqDVMoHL4DklK%2FVwaYdZDWdECC4tDy9C8VXw%3D%3D&RelayState=https%3A%2F%2Fjira.fraglab.com%2Fbrowse%2FLI-3671&SigAlg=http%3A%2F%2Fwww.w3.org%2F2000%2F09%2Fxmldsig%23rsa-sha1&Signature=hxU09Wglu7%2FZ93Wt7TRV7sDH6BHRdyIGo9Xb5zW%2BEEfjRfjSA61SRXWe6oGtUecPvZwMbS0h0cwuINQkYHOpnnFb5e65utNPA7AMgdCVemERywzi4%2FTQ%2Bx56o0rIsuI9jk7auv0oRxrG2eV26nwvDL7nrBYdDh9%2FJl3Wc8geEehOYsMVUSl8l5RlTtqZInCCvfnJhtQw2lUz2SmSrCXeCntAlsp1ZtJSLqNIBmit6wjrjxE2QHWiUs6KGo1koJmdCyebUd5oyUHqwZxx1HPuDz959iPInGi4wOQbu%2FQFK5fzQJBcnzLTbAG%2Bft7uyeWTcJD%2FAVLc28jayAsKcImaqA%3D%3D&client-request-id=2fc9bde8-0cdf-48f9-0002-0080010000fa'

jiraauth = browser.get(url)

entername = browser.find_element_by_xpath('//input[@id="userNameInput"]')
entername.send_keys(r'FRAGLAB\bytex')

enterpassword = browser.find_element_by_xpath('//input[@id="passwordInput"]')
enterpassword.send_keys('Fty3w6yvyt@du6r')

checkbox = browser.find_element_by_xpath('//input[@type="checkbox"]').click()

enter = browser.find_element_by_xpath('//span[@id="submitButton"]').click()

tokin = browser.find_element_by_xpath('//input[@id="otpvalue"]')
tokin.send_keys("6584728526")

enter2 = browser.find_element_by_xpath('//input[@id="submitButton"]').click()


for cookie in pickle.load(open('session', 'rb')):
    browser.add_cookie(cookie)

print("Куки загружены")
browser.get(url)