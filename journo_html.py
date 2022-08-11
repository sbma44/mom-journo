import time, sys, os
import re, csv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

writer = csv.writer(open('image_urls.txt', 'w'))

re_img = re.compile(r'data-(src|original|large)="(.*?)"')

URL = 'https://www.journohq.com/journo/europe-in-6-19909'
driver = webdriver.Firefox()
driver.get(URL)

entries = driver.find_elements(By.CLASS_NAME, 'entry-box')
total_entries = len(entries)
for (idx, entry) in enumerate(entries):
    html = entry.get_attribute('outerHTML')
    for m in re_img.finditer(html):
        writer.writerow((m.group(1), m.group(2)))
    with open('html/{:03d}.html'.format(idx), 'w') as f:
        f.write(entry.get_attribute('outerHTML'))