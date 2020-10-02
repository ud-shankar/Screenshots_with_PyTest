from selenium import webdriver


chromedriver = 'C:/Selenium/chromedriver.exe'
edgedriver = 'C:/Selenium/msedgedriver.exe'
driver = webdriver.Edge(edgedriver)
driver.maximize_window()
