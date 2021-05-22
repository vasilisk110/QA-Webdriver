import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

result_text = "Смартфони і мобільні телефони"
browser = webdriver.Chrome()
browser.get("https://allo.ua/")
time.sleep(3)
browser.find_element_by_css_selector('[id="search-form__input"]').send_keys("Телефон")
browser.find_element_by_css_selector('[id="search-form__input"]').send_keys(Keys.RETURN)
time.sleep(3)
actual_result = browser.find_element_by_css_selector('h1.v-catalog__title').text
assert result_text == actual_result
time.sleep(3)