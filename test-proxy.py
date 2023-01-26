#from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver
import time

URL = "https://whoer.net/"
PROXY = "144.168.217.88:8780"
PROXY_OPTIONS = {
    "proxy": {
        "https": "http://antuhwyr:b0udoj6j4zvl@144.168.217.88:8780"
    }
}

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          seleniumwire_options=PROXY_OPTIONS)

try:
    driver.get(URL)
    time.sleep(5)

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
