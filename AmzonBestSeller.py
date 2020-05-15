from selenium import webdriver
class Amazon:
    def __init__(self):
        self.MAX_NUM_PAGE = 75
        pass
    def init_csv_file(self,csv_name):
        with open(csv_name + ".csv","w") as f :
            f.write("book_name , author_name  , book_price , book_link \n")

    def init_webdriver_chrome(self):
        return webdriver.Chrome()

    def init_webdriver_firefox(self):
        return webdriver.Firefox()

    def url_to_navigate(self,url,driver):
        driver.get(url)
    def scrab_data(self,csvName):
        driver = self.init_webdriver_firefox()
        url = "https://www.amazon.com/s?i=stripbooks&rh=n%3A5%2Cp_72%3A1250221011&page="+"1"+"&pf_rd_i=5&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=f8dbb647-d3f1-57c0-b290-0fccc6fd7ba2&pf_rd_r=17V244FAA3AFK5GE7YC2&pf_rd_s=merchandised-search-11&pf_rd_t=101&qid=1589041008&ref=sr_pg_2"
        self.url_to_navigate(url,driver)
        #book_name = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
        #author_name = driver.find_elements_by_xpath("//a[@class='a-size-base a-link-normal']")
        #prices = driver.find_elements_by_xpath("//span[@class='a-price-whole']")
        whole_div = driver.find_elements_by_xpath("//div[@class='sg-col-inner']")
        book_name = whole_div[0].find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
        author_name = whole_div[0].find_elements_by_xpath("//a[@class='a-size-base a-link-normal']")
        prices = whole_div[0].find_elements_by_xpath("//span[@class='a-price-whole']")
        #with open(csvName+".csv",'a') as f :
        for index in range(len(book_name)):
            book_link = driver.find_element_by_link_text(book_name[index].text)
            print(book_link.text)

            #book_link = driver.find_element_by_link_text(book_name[index].text)
            #print(book_name[index].text + " , " + author_name[index].text+ " , " + prices[index].text )
        """for page in range(1,self.MAX_NUM_PAGE):
            url = "https://www.amazon.com/s?i=stripbooks&rh=n%3A5%2Cp_72%3A1250221011&page="+page+"&pf_rd_i=5&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=f8dbb647-d3f1-57c0-b290-0fccc6fd7ba2&pf_rd_r=17V244FAA3AFK5GE7YC2&pf_rd_s=merchandised-search-11&pf_rd_t=101&qid=1589041008&ref=sr_pg_2"
            self.url_to_navigate(url,driver)
            book_name = driver.find_elements_by_xpath("//div[@class='a-size-medium a-color-base a-text-normal']")
            author_name = driver.find_elements_by_xpath("//div[@class='a-size-base a-link-normal']")
            prices = driver.find_elements_by_xpath("//div[@class='a-price-whole']")
            #with open(csvName+".csv",'a') as f :
            for index in range(len(book_name)):
                book_link = driver.find_element_by_link_text(book_name[index].text)
                print(book_name[index].text + "," + author_name[index].text+ "," + prices[index].text + "," + book_link)
                   #f.write(book_name[index].text + "," + author_name[index].text+ "," + prices[index].text + "," + book_link +"\n" )"""

a = Amazon()
#a.scrab_data("Amazon_computer & tech_data")
driver = webdriver.Firefox()
url = "https://www.amazon.com/s?i=stripbooks&rh=n%3A5%2Cp_72%3A1250221011&page="+"1"+"&pf_rd_i=5&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=f8dbb647-d3f1-57c0-b290-0fccc6fd7ba2&pf_rd_r=17V244FAA3AFK5GE7YC2&pf_rd_s=merchandised-search-11&pf_rd_t=101&qid=1589041008&ref=sr_pg_2"
driver.get(url)
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    print(elem.get_attribute("href"))