from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

URL = "https://www.instagram.com/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    driver.get(URL)
    time.sleep(2)
    driver.maximize_window()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
