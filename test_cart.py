from selenium.webdriver.common.by import By
import pytest

# adding item to cart from a catalog
def test_manage_cart(driver, login):
    #driver.get(url)
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    # check if the cart has 3 items
    assert driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == '3'

    # removing item from cart
    driver.find_element(By.ID, 'remove-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'remove-sauce-labs-bike-light').click()
    driver.find_element(By.ID, 'remove-sauce-labs-bolt-t-shirt').click()
    # check if the cart is empty
    cart_badges = driver.find_elements(By.CLASS_NAME, 'shopping_cart_badge')
    assert len(cart_badges) == 0, "Cart is not empty"

    # add items to cart form the item page
    driver.find_element(By.XPATH,"//div[contains(text(),'Sauce Labs Bike Light')]").click()
    driver.find_element(By.ID,'add-to-cart').click()

    assert driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == '1'

    # removing item from cart
    driver.find_element(By.ID, 'remove').click()


    # check if the cart is empty
    cart_badges = driver.find_elements(By.CLASS_NAME, 'shopping_cart_badge')
    assert len(cart_badges) == 0, "Cart is not empty"

    # add items to cart by title
    driver.find_element(By.XPATH, "//div[contains(text(), 'Sauce Labs Bike Light')]").click()
    #go back to the catalog
    driver.find_element(By.NAME, 'back-to-products').click()
    # add an item by image
    driver.find_element(By.CSS_SELECTOR, 'img[alt="Sauce Labs Bolt T-Shirt"]').click()
    driver.find_element(By.NAME, 'back-to-products').click()

    # placing an order
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    driver.find_element(By.ID, 'checkout').click()
    driver.find_element(By.ID, 'first-name').send_keys('John')
    driver.find_element(By.ID, 'last-name').send_keys('Doe')
    driver.find_element(By.ID, 'postal-code').send_keys('12345')
    driver.find_element(By.ID, 'continue').click()
    driver.find_element(By.ID, 'finish').click()
    assert driver.find_element(By.CLASS_NAME, 'complete-header').text == 'Thank you for your order!'
    #back to the catalog
    driver.find_element(By.NAME, 'back-to-products').click()

    # check sorting filter
    driver.find_element(By.CLASS_NAME, 'product_sort_container').click()
    driver.find_element(By.XPATH, "//option[contains(text(),'Price (low to high)')]").click()
    driver.find_element(By.CLASS_NAME, 'product_sort_container').click()
    driver.find_element(By.XPATH, "//option[contains(text(),'Price (high to low)')]").click()
    driver.find_element(By.CLASS_NAME, 'product_sort_container').click()
    driver.find_element(By.XPATH, "//option[contains(text(),'Name (A to Z)')]").click()
    driver.find_element(By.CLASS_NAME, 'product_sort_container').click()
    driver.find_element(By.XPATH, "//option[contains(text(),'Name (Z to A)')]").click()
    driver.find_element(By.CLASS_NAME, 'product_sort_container').click()

    assert driver.find_element(By.CLASS_NAME, 'product_sort_container').is_displayed() == True

    #tsting burger menu
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    driver.find_element(By.ID, 'about_sidebar_link').is_enabled()
    driver.find_element(By.ID, 'reset_sidebar_link').is_enabled()
    driver.find_element(By.ID, 'logout_sidebar_link').click()
    assert driver.find_element(By.ID, 'login-button').is_displayed() == True










