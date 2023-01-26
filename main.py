from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get('https://orteil.dashnet.org/cookieclicker/')
driver.maximize_window()

wait = WebDriverWait(driver, 1000)
wait.until(EC.element_to_be_clickable((By.ID, 'prompt')))
lan_selectors = driver.find_elements(By.CLASS_NAME, 'langSelectButton')

for lan in lan_selectors:
    if "English" in lan.get_attribute('innerHTML'):
        lan.click()
        break

actions = ActionChains(driver)

wait.until(EC.element_to_be_clickable((By.ID, 'productPrice1')))

items = [driver.find_elements(By.ID, 'productPrice' + str(i)) for i in range(1, -1, -1)]

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, 'cookies')

actions.click(cookie)

for i in range(6000):
    cookie.click()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item[0].text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item[0])
            upgrade_actions.click()
            upgrade_actions.perform()
