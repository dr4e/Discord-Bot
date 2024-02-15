from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class WebScrappingAttribute:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        self.options.add_argument("--headless=new")
        self.options.add_argument(f'user-agent={user_agent}')
        self.driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def getAttributeByXPATH(self, link, xpath, attribute):
        self.driver.get(link)
        attribute = self.driver.find_element(By.XPATH, xpath).get_attribute(attribute)
        self.driver.quit()
        return attribute