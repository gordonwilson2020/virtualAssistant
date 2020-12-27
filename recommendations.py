from selenium import webdriver

class recom():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/Users/gordonwilson/chromedriver')

    def recom_info(self):
        self.driver.get(url="https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm")
        select = self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]')
        select.click()

#bot = recom()
#bot.recom_info()