from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from basics.login import login

def main():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Faça login
    login(driver)

    # more code...

main()
