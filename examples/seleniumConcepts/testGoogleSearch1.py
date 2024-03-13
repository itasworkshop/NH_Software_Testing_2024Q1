from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


@allure.severity(allure.severity_level.NORMAL)
class TestGoogleSearch:

    @allure.severity(allure.severity_level.MINOR)
    def test_Google_Search(self):
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service=self.serv_obj)
        print("Getting you chrome browser!!!!")
        self.driver  = webdriver.Chrome()
        self.driver.maximize_window()
        #driver.implicitly_wait(3)
        #time.sleep(3)
        self.driver.get("https://www.google.com/")
        #search_box = driver.find_element("name","q")
        #search_box = driver.find_element("id","APjFqb")
        #search_box = driver.find_element(By.ID,"APjFqb")
        search_box = self.driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
        search_box.send_keys("hello")
        search_box.submit()
        time.sleep(3)
        self.driver.close()
        print("Closing your chrome browser!!!!")