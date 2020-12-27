from selenium import webdriver

class Movie():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/Users/gordonwilson/chromedriver')

    def get_movie(self, name):
        self.driver.get(url='https://google.com/')
        search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(name + " movie reviews")
        submit = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
        submit.click()

#bot = movie()
#bot.get_movie("liberty bell")
