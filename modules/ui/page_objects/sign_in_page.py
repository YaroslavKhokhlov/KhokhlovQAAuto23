from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
class SignInPage(BasePage):
    URL1 = 'https://github.com/login'
    URL2 = "https://novaposhta.ua/"
    URL3 = "https://www.youtube.com/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL1)

    def try_login(self, username, password):
        
        login_elem = self.driver.find_element(By.ID, "login_field")
        login_elem.send_keys(username)
        pass_elem = self.driver.find_element(By.ID, "password")
        pass_elem.send_keys(password)
        btn_elem = self.driver.find_element(By.NAME, "commit")
        btn_elem.click()

    def check_title(self, expected_title1):
        return self.driver.title == expected_title1
    
    
    def go_to_n(self):
        self.driver.get(SignInPage.URL2)
    
    def enter_number_package(self, numb_package):
        track_down = self.driver.find_element(By.ID, "cargo_number")
        track_down.send_keys(numb_package)
        btn_elem = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][name='']")
        btn_elem.click()
    def check_title_n(self, expected_title2):
        return self.driver.title == expected_title2
    
    def go_to_u(self):
        self.driver.get(SignInPage.URL3)

    def search_video(self, name):
        
        search_v = self.driver.find_element(By.NAME, "search_query")
        search_v.send_keys(name)
        btn_elem = self.driver.find_element(By.ID, "search-icon-legacy")
        btn_elem.click()
        time.sleep(3)
        btn_elem = self.driver.find_element(By.CSS_SELECTOR, 'yt-formatted-string[aria-label*="Гімн України/ Anthem of Ukraine."]')
        btn_elem.click()
    
    def get_current_url(self):
        return self.driver.current_url
        
    

        

        

        
      

