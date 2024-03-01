# Автоматическое тестирование с помощью Selenium

## Определение

Selenium WebDriver — это инструмент для автоматизации действий веб-браузера. В большинстве случаев используется для тестирования Web-приложений, но этим не ограничивается. В частности, он может быть использован для решения рутинных задач администрирования сайта или регулярного получения данных из различных источников.

## Установка

Selenium WebDriver доступен для различных языков программирования. Примеры представлены для python.

Установить можно через pip командой:

```
pip install selenium
```

Также потребуется скачать драйвер для нужного браузера

## Работа с Selenium. Примеры с лекции

### Авторизация, взаимодействие с кнопками

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time

import settings

service = webdriver.ChromeService(executable_path = './chromedriver')
driver = webdriver.Chrome(service=service)

url = 'https://cabinet.vvsu.ru'

try:
    driver.get(url)
    time.sleep(2)

    login = driver.find_element(By.ID, 'login')
    login.send_keys(settings.login)

    password = driver.find_element(By.ID, 'password')
    password.send_keys(settings.password)

    time.sleep(2)

    button = driver.find_element(By.ID, 'accept')
    button.click()

    time.sleep(2)

    sc_button = driver.find_element(By.CSS_SELECTOR, 'div.red')
    sc_button.click()

    sc = driver.find_element(By.CSS_SELECTOR, 'div.jcarousel-container')
    print(sc.text)

    time.sleep(2)

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
```