from selenium import webdriver

SERVER_URL = 'http://login-server:8080'

def chrome_example():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(BASE_URL)
    print(browser.page_source)

    browser.quit()

if __name__ == '__main__':
    chrome_example()
