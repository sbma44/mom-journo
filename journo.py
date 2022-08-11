import time, sys, os
#from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

URL = 'https://www.journohq.com/journo/europe-in-6-19909'
driver = webdriver.Firefox()
driver.get(URL)

entries = driver.find_elements(By.CLASS_NAME, 'entry-box')
total_entries = len(entries)
for i in range(total_entries):
    driver.execute_script("var c = document.getElementsByClassName('entry-box'); for (var i=c.length;i--;i>=0) { if (i!==parseInt(arguments[0])) c[i].remove(); }", i)

    # click all comment links to expand them
    more_links = driver.find_elements(By.CLASS_NAME, 'more-less-btn')
    for ml in more_links:
        ml.click()

    driver.execute_script("var el = document.getElementsByClassName('lazy'); for(var i=0; i<el.length; i++) { if (el[i].attributes['data-src']) el[i].src = el[i].attributes['data-src'].value; }")
    driver.execute_script("document.getElementById('header').remove(); document.getElementById('footer').remove();")
    driver.execute_script("document.getElementsByClassName('journo-navbar-box')[0].remove();")
    driver.execute_script("document.getElementsByClassName('journo-cover-img-box')[0].remove();")
    driver.execute_script("document.getElementsByClassName('journo-view-box')[0].remove();")

    time.sleep(10) # wait for lazy loading images

    driver.get_full_page_screenshot_as_file('screenshots/ff_{}.png'.format(i))

    driver.refresh()