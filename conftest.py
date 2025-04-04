from selenium import webdriver
from selenium.webdriver.chrome.options import Options #Если требуется запуск на Gitlabs/режим без окна
import pytest

#Открытие браузера
@pytest.fixture
def driver(): #Driver - это браузер
    options = Options() #Опция, если будем выполнять тесты на Gitlabs
    options.add_argument('--headless') #Браузер открыть без режима окна, если проходить тесты на Gitlabs
    driver = webdriver.Chrome(options=options) #Выбираем браузер, options - если нужно запуск без окна
    driver.maximize_window() #Окно на весь экран
    driver.implicitly_wait(3) #Задержка 3 секунды
    yield driver
    driver.close() #Закрыть браузер после автотестам(на всякий, хоть Chrome и сам закрывается)
