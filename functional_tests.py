from selenium import webdriver
browser = webdriver.Firefox(executable_path=r"C:\Users\ajurc\PycharmProjects\geockdriver\geckodriver.exe")
browser.get('http://localhost:8000')

assert 'install' in browser.title