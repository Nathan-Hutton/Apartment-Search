from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class SheetFiller:

    def __init__(self):
        service = Service("C:\important\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)

    def fill_form(self, address, price, link):
        self.driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfJvYvOzsJBH-57pzOfw0riFa-ZlYmTgZh65afYQ0VTBRjV6g/viewform?usp=sf_link')
        time.sleep(1)
        address_box = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_box = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_box = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        address_box.send_keys(address)
        price_box.send_keys(price)
        link_box.send_keys(link)
        button.click()
        time.sleep(300)


