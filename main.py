import time
from loguru import logger
from selenium import webdriver
import undetected_chromedriver as uc


#HOST = "selenoid"
HOST = "localhost"
#HOST = "172.17.0.2"

def test_firefox():
    logger.info('Iniciando bot Firefox')
    
    options = webdriver.FirefoxOptions()
    firefox = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST),options=options)
    
    firefox.get('https://www.google.com')
    print('firefox', firefox.title)
    firefox.quit()


def test_chrome():
    logger.info('Iniciando bot Google')
    
    options = webdriver.ChromeOptions()
    chrome = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST),options=options)
    
    chrome.get('https://www.google.com')
    print('chrome', chrome.title)
    chrome.quit()
    

def get_ssid_and_cookies():
    logger.info('Iniciando bot')
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST),options=options)

    driver.get('https://www.google.com')
    logger.success(driver.title)

    
    with open('success.txt', 'w+', encoding='utf-8') as f:
            f.write(f"Titulo: {driver.title}\nSelenium com selenoid e docker funcionou com sucesso.")
    driver.quit()
    
    # Restante do seu código

n=0
while True:
    time.sleep(10)
    n+=1
    get_ssid_and_cookies()
    test_firefox()
    test_chrome()
    print(f'Quantiade de dexecução: {n}')