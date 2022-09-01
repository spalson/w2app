from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# inicjacja chromedrivera z pliku (bez błędu)
service = Service('/Users/mateuszspalik/Downloads/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)

# fullscreen
# driver.maximize_window()

# czeka 2 sekundy
time.sleep(2)
driver.get('https://web2app.app/')

# prezentacja strony głównej tryb ciemny
# akceptacja cookies
driver.find_element(By.ID, "rcc-confirm-button").click()

# smooth scrolling
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
time.sleep(1)

# przejście na górę strony
driver.find_element(By.CLASS_NAME, "myLogo").click()
time.sleep(1)

# prezentacja tryby jasnego
driver.find_element(By.XPATH, "//button[@class='header__StyledButton-i6ilmw-3 lkbvGE']").click()
time.sleep(1)

# ponowne zejście w dół
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
time.sleep(1)

# ponowne przejście na górę strony
driver.find_element(By.CLASS_NAME, "myLogo").click()
time.sleep(1)

# zakładka developers
action = ActionChains(driver)
firstLevelMenu = driver.find_element(By.XPATH, "//button[@class='menu__StyledMenu-sc-1ri7r1k-0 dclcXL']")
action.move_to_element(firstLevelMenu).perform()
secondLevelMenu = driver.find_element(By.XPATH, "//p[@class='menu__StyledTitle-sc-1ri7r1k-5 jninuv']")
action.move_to_element(secondLevelMenu).perform()
secondLevelMenu.click()
time.sleep(1)

# zamknięcie githuba zamyka drugą otwartą kartę
driver.switch_to.window(driver.window_handles[1])
driver.close()
time.sleep(2)

# powrót do dark mode'a / trzeba przełączyć na pierwsze okno
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, "//button[@class='header__StyledButton-i6ilmw-4 hTxOpD']").click()
time.sleep(1)

# zakładka community
# pierwsza opcja Facebook
driver.find_element(By.XPATH, "//span[normalize-space()='Community']").click()
driver.find_element(By.XPATH, "//p[normalize-space()='Facebook']").click()

# zamknięcie facebooka zamyka drugą otwartą kartę
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.close()
time.sleep(2)

# druga opcja discord
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, "(//span[normalize-space()='Community'])[1]").click()
driver.find_element(By.XPATH, "(//p[normalize-space()='Discord'])[1]").click()
time.sleep(2)

# zamknięcie discorda zamyka drugą otwartą kartę
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.close()
time.sleep(2)

# powrót do main tabu
driver.switch_to.window(driver.window_handles[0])

# wejście do download our app
driver.find_element(By.XPATH, "(//a[normalize-space()='Download our app'])[1]").click()
time.sleep(3)

# aktywacja tabu download our app
driver.switch_to.window(driver.window_handles[1])
driver.close()

# powrót do main tabu
driver.switch_to.window(driver.window_handles[0])

# Demo - free Demo przejścia
driver.find_element(By.XPATH, "(//a[@href='#offer'])[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "(//a[@href='#up'])[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "(//a[@href='#offer'])[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "(//a[@href='#up'])[1]").click()

# test ikony github w footerze
driver.find_element(By.XPATH, "(//a)[13]").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.close()

# powrót do main tabu
driver.switch_to.window(driver.window_handles[0])

# test ikony discord w footerze
driver.find_element(By.XPATH, "(//a)[14]").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.close()

# powrót do main tabu
driver.switch_to.window(driver.window_handles[0])

# powrót na górę
driver.find_element(By.CLASS_NAME, "myLogo").click()
time.sleep(1)

# zamyka okno przeglądarki
driver.quit()
