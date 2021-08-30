from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def get_element_by_xpath(driver, selector):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, selector))
    )


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:8181")
driver.maximize_window()

try:
    login_button = get_element_by_xpath(driver, "//div[@class='login-header']/a") # Localizando botão de login para extrair o link da página

    driver.get(login_button.get_attribute("href")) # Visistando página para cadastro

    # Preenche "campo email"
    email_input = get_element_by_xpath(driver, "//div[@class='login-column']//input[@name='email']")
    email_input.send_keys("teste@teste.com.br")

    # Preenche "senha"
    password_input = get_element_by_xpath(driver, "//div[@class='login-column']//input[@name='password']")
    password_input.send_keys("@teste123")

    # Envia formulário
    submit_button = get_element_by_xpath(driver, "//div[@class='login-column']//button[@value='login']")
    submit_button.click()

    time.sleep(0.5)

    # Confirma o alert 
    alert = driver.switch_to.alert
    alert.accept()


    time.sleep(0.5)
finally:
    driver.close()
