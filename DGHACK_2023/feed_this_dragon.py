from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException
import time, requests

url = "https://feedthisdragon4.chall.malicecyber.com/"

def server_call(session_uuid):
    url = "https://feedthisdragon4.chall.malicecyber.com/api/v1"
    headers = {
        "Cookie": f"uuid={session_uuid};",
        "Sec-Ch-Ua": "",
        "Itemuuid": "",
        "Sec-Ch-Ua-Mobile": "?0",
        "Authorization": "mynotsosecrettoken",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.110 Safari/537.36",
        "Content-Type": "application/json",
        "Shopuuid": "",
        "Update": "true",
        "Session": session_uuid,
        "Sec-Ch-Ua-Platform": "",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://feedthisdragon4.chall.malicecyber.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    response = requests.get(url, headers=headers)

driver = webdriver.Firefox()
driver.get(url)

play_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="nes-btn is-primary title--m" and text()="Play"]')))
session_uuid_text = driver.find_element(By.CLASS_NAME, 'session').text
session_uuid = session_uuid_text.split(": ")[1]

play_button.click()
score_container = driver.find_element(By.ID, 'ShopMenu')

coin_cap = [20, 80, 180, 320, 500,720, 980,1280,1620,2000,2440, 2880,3380,3920]
i = 0
tour = 0


initial_delay = 0.1


max_iterations = 1000000000000000000000000000000000000000000000000000000
for iteration in range(max_iterations):
    try:

        elements_to_click = driver.find_elements(By.XPATH, '//img[@alt="coin item" or @alt="burger item"  or @alt="gem item" or @alt="veggy item" or @alt="food item" or @alt="candy item" or @alt="life item" or @alt="secret item" or @alt="lilboo item" or @alt="midboo item" or @alt="bigboo item"]')
        elements_to_avoid = driver.find_elements(By.XPATH, '//img[@alt="fox item" or @alt="trap item"]')


        for element in elements_to_click:
            try:
                driver.execute_script("arguments[0].click();", element)
            except (StaleElementReferenceException, ElementNotInteractableException):
                pass


        for element in elements_to_avoid:
            try:
                driver.execute_script("arguments[0].style.visibility='hidden';", element)
            except (StaleElementReferenceException, ElementNotInteractableException):
                pass
        
        div_score = score_container.find_elements(By.TAG_NAME, "div")
        score = div_score[0].text.split()[1]

        if int(score) >= coin_cap[i]:
            div_score[1].click()

            driver.find_element(By.XPATH, '//span[contains(@class, "is-dark item-shop--name") and contains(text(), "Feed")]').click()
            driver.find_element(By.XPATH, '//span[contains(@class, "is-dark item-shop--name") and contains(text(), "Greed")]').click()
            driver.find_element(By.XPATH, '//span[contains(@class, "is-dark item-shop--name") and contains(text(), "Hard")]').click()
            driver.find_element(By.XPATH, '//span[contains(@class, "is-dark item-shop--name") and contains(text(), "Flee")]').click()
            driver.find_element(By.XPATH, '//span[contains(@class, "is-dark item-shop--name") and contains(text(), "Bag")]').click()

            close = driver.find_element(By.TAG_NAME, 'button')
            close.click()
            tour += 1
            if tour >= 5:
                i += 1
                tour = 0
        
        server_call(session_uuid)
        time.sleep(initial_delay)

    except Exception as e:
        print(f"Erreur : {e}")

    game_over_element_present = driver.find_elements(By.XPATH, '//div[@class="game-over-message"]')
    if game_over_element_present:
        print("Le jeu est terminé. Arrêt du script.")
        break


driver.quit()