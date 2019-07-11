from selenium import webdriver



## Step1: Populate stock_value information and write to disk

## Step2: Use the lib iexfinance to find the historic value of the stocks found in step1

stock_list = []

undervalued_large_caps = "undervalued_large_caps"

aggressive_small_caps = "aggressive_small_caps"



screening = undervalued_large_caps # 'screening' appears to be yahooesse for 'filter for'

number_of_stocks = 3



def step1_getTickerIDs(num_of_stocks_to_collect):

    path_to_chrome_driver = "C://Users//squar//jars//chromedriver_win32//chromedriver"

    driver = webdriver.Chrome(path_to_chrome_driver)

    

    url = "https://finance.yahoo.com/screener/predefined/{0}?offset=0&count={1}".format(screening, number_of_stocks )

    driver.get(url)

    # print(driver.page_source)



    for i in range(num_of_stocks_to_collect):

        try:    

            xpath = '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{0}]/td[1]/a'.format(i + 1)

            foundSeleniumObject = driver.find_element_by_xpath(xpath)

            print("Loop {0} of {1} for {2}".format(i, num_of_stocks_to_collect, foundSeleniumObject.text))

            stock_list.append(foundSeleniumObject.text)

            # print( dir( ticker))

        except Exception as e: 

            print("Boom! On loop {0} because {1}".format(i, e))



    driver.quit()

    n = 0

    for stock in stock_list:

        n += 1

        print("n|{0}|ticker|{1}|category|{2}".format(n, stock, screening))

step1_getTickerIDs(number_of_stocks)