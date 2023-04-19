import selenium as se
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time



def initialize_driver():
    caps = DesiredCapabilities.CHROME
    caps["goog:loggingPrefs"] = {"performance": "ALL"}
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_argument(
        "'user-agent'= 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'"
    )
    # option.add_argument('--headless')
    # option.add_argument("window-size=1920x1080")
    option.add_argument("--disable-crash-reporter")
    option.add_argument("--disable-in-process-stack-traces")
    option.add_argument("--disable-logging")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--log-level=3")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    option.add_argument("user-data-dir=C:\\Users\\Pwnzerer\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 5")
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    initialized_driver = webdriver.Chrome(
    executable_path="chromedriver.exe", options=option, desired_capabilities=caps
    )
    return initialized_driver


def get_product_data(driver,url):
    driver.get(url)
    product_title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[1]/div[2]/div[3]/div[1]/span")))
    product_price = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[1]/div[2]/div[3]/div[1]/div[2]/p")))
    product_image = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div/div/img")))
    product_overall_rating = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[1]/div[2]/div[5]/div[4]/div/div/div/div/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/span[2]")))
    product_rating_count = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "bv_numReviews_text")))
    product_brand = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div[1]/div[2]/div[3]/div[1]/a")))
    path_elemnts = driver.find_elements(By.CSS_SELECTOR, "[itemprop='name']")
    path_string = ""
    for el in path_elemnts:
        if el.text != "":
            path_string = path_string + el.text + " > "
    data_dict= {}
    data_dict["product_title"] = product_title.get_attribute("textContent")
    data_dict["product_price"] = product_price.get_attribute("textContent")
    data_dict["product_image"] = product_image.get_attribute("src")
    data_dict["product_overall_rating"] = product_overall_rating.text
    data_dict["product_rating_count"] = product_rating_count.text
    data_dict["product_brand"] = product_brand.get_attribute("textContent")
    data_dict["Categories"] = path_string
    print(data_dict)
    return data_dict

new_driver = initialize_driver()
get_product_data(new_driver,"https://well.ca/products/navitas-naturals-organic-acai-powder_99112.html")