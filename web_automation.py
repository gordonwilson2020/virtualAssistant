from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/Users/gordonwilson/chromedriver')

    def play(self, name):
        self.name = name
        self.driver.get(url='https://www.youtube.com/results?search_query=' + name)
        video = self.driver.find_element_by_xpath('//*[id="dismissable"]')
        video.click()
