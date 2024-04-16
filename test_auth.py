from selenium.webdriver.common.by import By

def test_auth_positive(login_page):
    login_page.open()
    login_page.is_visible((By.ID, 'startTest')).click()
    login_page.is_visible((By.ID, 'login')).send_keys('admin')
    login_page.is_visible((By.ID, 'password')).send_keys('123')
    login_page.is_visible((By.ID, 'agree')).click()
    login_page.is_visible((By.ID, 'register')).click()

    assert login_page.is_visible((By.ID, 'successMessage')).text == 'Вы успешно зарегистрированы!'






