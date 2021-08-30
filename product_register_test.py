from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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
    email_input.send_keys("adm@adm.com.br")

    # Preenche "senha"
    password_input = get_element_by_xpath(driver, "//div[@class='login-column']//input[@name='password']")
    password_input.send_keys("@adm123")

    # Envia formulário
    submit_button = get_element_by_xpath(driver, "//div[@class='login-column']//button[@value='login']")
    submit_button.click()

    # Confirma o alert 
    alert = driver.switch_to.alert
    alert.accept()

    # Clica em botão "Cadastro de Produtos"
    product_register_button = get_element_by_xpath(driver, "//div[@class='user-info-middle' and contains(.//p/text(), 'Cadastro de Produtos')]")
    product_register_button.click()

    # Clica em botão "Inserir Novo Produto"
    insert_product_button = get_element_by_xpath(driver, "//a[@class='end-link']")
    driver.get(insert_product_button.get_attribute("href"))

    # Insere nome do produto
    product_name_input = get_element_by_xpath(driver, "//input[@name='name']")
    product_name_input.clear()
    product_name_input.send_keys("Produto teste")

    # Insere preço do produto
    product_price_input = get_element_by_xpath(driver, "//input[@name='price']")
    product_price_input.clear()
    product_price_input.send_keys("34.90")

    # Insere descrição do produto
    product_description_input = get_element_by_xpath(driver, "//textarea[@name='description']")
    product_description_input.clear()
    product_description_input.send_keys("Esta é a descrição do produto")

    # Seleciona a categoria
    select_input = Select(get_element_by_xpath(driver, "//select[@name='categoryId']"))
    select_input.select_by_visible_text("Playstation > Jogos")

    # Seleciona a imagem
    image_input = get_element_by_xpath(driver, "//input[@id='img']")
    image_input.send_keys("/home/lucas.ramalho/Imagens/imagem_teste.png")

    time.sleep(0.5)

    # Clica no botão "Gravar"
    button = get_element_by_xpath(driver, "//button[@value='grava']")
    button.click()

    # Confirma o alert 
    alert = driver.switch_to.alert
    alert.accept()

    time.sleep(0.5)
finally:
    driver.close()
