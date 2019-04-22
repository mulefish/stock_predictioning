import numpy as np
from datetime import datetime
import smtplib
import time
from selenium import webdriver
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm
# from sklearn import cross_validation
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
#For Stock Data

# console.log("get_quote " + aapl.get_quote())

import iexfinance
from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data
#from iexfinance import Share

def predictData(stock, days):
    print("stock {0}   days {1}".format(stock, days ))
    start = datetime(2017, 1, 1)
    end = datetime.now()
    #Outputting the Historical data into a .csv for later use
    df = get_historical_data(stock, start=start, end=end,     output_format='pandas')
    # csv_name = ('Exports/' + stock + '_Export.csv')
    csv_name = ('C:\\Users\\squar\\ml\stock\\' + stock + '_Export.csv')
    print("Writing to {0}".format( csv_name ))
    df.to_csv(csv_name)
    df['prediction'] = df['close'].shift(-1)
    df.dropna(inplace=True)
    forecast_time = int(days)
    
    X = np.array(df.drop(['prediction'], 1))
    Y = np.array(df['prediction'])
    X = preprocessing.scale(X)
    X_prediction = X[-forecast_time:]
#    X_train, X_test, Y_train, Y_test =         cross_validation.train_test_split(X, Y, test_size=0.5)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5)

    #Performing the Regression on the training data
    clf = LinearRegression()
    clf.fit(X_train, Y_train)
    prediction = (clf.predict(X_prediction))

    #Sending the SMS if the predicted price of the stock is at least 1 greater than the previous closing price
    last_row = df.tail(1)
    s = str(stock)
    c = str(last_row['close'])
    p1 = str(prediction[0])
    p5 = str(prediction[4])

    if (float(prediction[4]) > (float(last_row['close']))):
        # output = ("Stock:" + str(stock) + "\nPrior Close:\n" +         str(last_row['close']) + "\n\nPrediction in 1 Day: " + str(prediction[0]) + "\nPrediction in 5 Days: " + str(prediction[4]))
        msg = "YAY Stock:{0} Prior Close:{1} Prediction in 1 Day: {2} Prediction in 5 Days: {3}".format(s,c,p1,p5)
        print(msg)
    else:
        msg = "BOO Stock:{0} Prior Close:{1} Prediction in 1 Day: {2} Prediction in 5 Days: {3}".format(s,c,p1,p5)
        print(msg)
        
def getYahooStocks(n):
    #Navigating to the Yahoo stock screener
    path_to_chrome_driver = "C://Users//squar//jars//chromedriver_win32//chromedriver"
    driver = webdriver.Chrome(path_to_chrome_driver)
    url = "https://finance.yahoo.com/screener/predefined/aggressive_small_caps?offset=0&count=202"
    driver.get(url)
    stock_list = []
    n += 1
    print("About to loop")
    for i in range(1, n):
        try:
            xpath = '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{0}]/td[1]/a'.format(i)
            ticker = driver.find_element_by_xpath(xpath)
            print("looping and currently i={0} and the text is {1}".format(i, ticker.text))
            stock_list.append(ticker.text)
        except Exception as e: 
            print("Boom! On loop {0}".format(i))
            print(e)
    count = 0 
    print("Out of the loop")
    for x in stock_list:
        count += 1
        print( "{0} has {1}".format(count,x))
    driver.quit()


    #Using the stock list to predict the future price of the stock a specificed amount of days
    for i in stock_list:
        try:
            predictData(i, 5)
        except:
            print("Stock: " + i + " was not predicted")


def preloadedStocks():
    stock_list=[]
    stock_list.append("XON")
    stock_list.append("DNR")
    #stock_list.append("AKS")
    #stock_list.append("AKRX")
    #stock_list.append("BRS")
    #stock_list.append("JCP")
    #stock_list.append("ESV")
    #stock_list.append("SNBR")
    #stock_list.append("LL")
    #stock_list.append("CPE")
    #stock_list.append("aapl")
    for x in stock_list:
        try:
            predictData(x, 5)
        except Exception as e:
            print("BOOM! {0}   {1}".format(x,e))

        
# preloadedStocks()

getYahooStocks(10)
print("The end")
