import time
from loguru import logger
from selenium import webdriver
import undetected_chromedriver as uc


HOST = "selenoid"
#HOST = "localhost"
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
    
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "",
        "selenoid:options": {
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor='http://{}:4444/wd/hub'.format(HOST),
        desired_capabilities=capabilities)
    
    driver.get('https://www.google.com')
    print('chrome', driver.title)
    
    driver.quit()
    



def get_ssid_and_cookies():
    logger.info('Iniciando bot')
    
    options = uc.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')

    capabilities = {
        'goog:loggingPrefs': {'performance': 'ALL'},
        'browserName': 'chrome',
        'version': 'latest',
        'enableVNC': True,
        'enableVideo': True,
        'goog:chromeOptions': options.to_capabilities()
    }

    # driver = webdriver.Remote(
    #     command_executor=f'172.17.0.2:4444/wd/hub',
    #     desired_capabilities=capabilities
    # )
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST), options=options)

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