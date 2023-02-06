import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_buy_item():
    """
    Test case SMOKE-1
    """
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") 
    chrome_options.add_argument("--disable-infobars") 
    chrome_options.add_argument("--disable-extensions") 

    service = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
		
    url = "https://www.saucedemo.com"
    driver.get(url=url)
		
    login = driver.find_element(By.ID, value ="user-name")
    login.click()
    login.send_keys("standard_user")

    password = driver.find_element(By.ID, value ="password")
    password.click()
    password.send_keys("secret_sauce")

    element = driver.find_element(by=By.CSS_SELECTOR, value="[class='submit-button btn_action']")
    element.click()

    x_path_label = '//*[@id="item_3_title_link"]/div'
    element = driver.find_element(by=By.XPATH, value=x_path_label)
    element.click()

    price_details = driver.find_element(By.CLASS_NAME, value="inventory_details_price")
		
    assert price_details.text == '$15.99', "Unexpected price_details"

    x_path_buttom_primary = '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]'
    buttom_primary = driver.find_element(by=By.XPATH, value = x_path_buttom_primary)
    buttom_primary.click()                              

    x_path_buttom_secondary = '//*[@id="remove-test.allthethings()-t-shirt-(red)"]'
    buttom_secondary = driver.find_element(by=By.XPATH, value = x_path_buttom_secondary) 
    assert buttom_secondary.text == 'REMOVE', "Unexpected NAME"

    basket = driver.find_element(By.CLASS_NAME, value="shopping_cart_link")
    basket.click()

    buttom_checkout = driver.find_element(By.ID, value ="checkout")
    buttom_checkout.click()

    first_name = driver.find_element(By.ID, value ="first-name")
    first_name.click()
    first_name.send_keys("Дмитрий")
    last_name = driver.find_element(By.ID, value ="last-name")
    last_name.click()
    last_name.send_keys("Назаров")
    postal_code = driver.find_element(By.ID, value ="postal-code")
    postal_code.click()
    postal_code.send_keys("446200")

    buttom_continue = driver.find_element(By.ID, value ="continue")
    buttom_continue.click()

    x_path_delivery = '//*[@id="checkout_summary_container"]/div/div[2]/div[4]'
    delivery = driver.find_element(by=By.XPATH, value=x_path_delivery)
		
    assert delivery.text == 'FREE PONY EXPRESS DELIVERY!', "Unexpected delivery"

    buttom_finish= driver.find_element(By.ID, value ="finish")
    buttom_finish.click()
