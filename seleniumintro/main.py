from selenium import webdriver

page = webdriver.Chrome("chromedriver.exe")
page.get('http://')
page.set_page_load_timeout(60)
page.implicitly_wait(30)
page.get_screenshot_as_file('cap.png')

page.quit()