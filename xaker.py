from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://xakep.ru/issues/xa/')
time.sleep(3)

num = 1
while True:
    num+=1
    driver.get(f'https://xakep.ru/issues/xa/page/{num}/')
    time.sleep(1)
    links_pdf = driver.find_elements(By.CLASS_NAME, 'download-button')
    for link_pdf in links_pdf:
        link_pdf.click()
        time.sleep(10)
