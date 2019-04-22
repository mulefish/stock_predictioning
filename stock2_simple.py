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
        
def preloadedStocks():
    stock_list=[]
    #stock_list.append("XON")
    #stock_list.append("DNR")
    #stock_list.append("AKS")
    #stock_list.append("AKRX")
    #stock_list.append("BRS")
    #stock_list.append("JCP")
    #stock_list.append("ESV")
    #stock_list.append("SNBR")
    #stock_list.append("LL")
    #stock_list.append("CPE")
    #stock_list.append("aapl")

    stock_list.append("XON")
    stock_list.append("DNR")
    stock_list.append("AKS")
    stock_list.append("TIGR")
    stock_list.append("AKRX")
    stock_list.append("BRS")
    stock_list.append("JCP")
    stock_list.append("ESV")
    stock_list.append("SNBR")
    stock_list.append("LL")
    stock_list.append("CPE")
    stock_list.append("TXMD")
    stock_list.append("CRZO")
    stock_list.append("WTW")
    stock_list.append("CDE")
    stock_list.append("NE")
    stock_list.append("SNH")
    stock_list.append("SPN")
    stock_list.append("OBE")
    stock_list.append("AVP")
    stock_list.append("IRWD")
    stock_list.append("AG")
    stock_list.append("WTI")
    stock_list.append("HOME")
    stock_list.append("EPE")
    stock_list.append("LTHM")
    stock_list.append("TVTY")
    stock_list.append("DFRG")
    stock_list.append("GCI")
    stock_list.append("ANF")
    stock_list.append("MUX")
    stock_list.append("NVRO")
    stock_list.append("HMY")
    stock_list.append("BOOT")
    stock_list.append("SCWX")  
    stock_list.append("PDS")
    stock_list.append("CASA")
    stock_list.append("RCII")
    stock_list.append("EGO")
    stock_list.append("SEMG")  
    stock_list.append("MCRN")
    stock_list.append("BCRX")
    stock_list.append("TPH")
    stock_list.append("DBD")
    stock_list.append("PEI")
    stock_list.append("ELY")
    stock_list.append("CCS")
    stock_list.append("EAT")
    stock_list.append("MGNX")
    stock_list.append("FET")
    stock_list.append("BFR")
    stock_list.append("ASMB")
    stock_list.append("TIVO")
    stock_list.append("HOLI")
    stock_list.append("RMBS")
    stock_list.append("KOPN")   
    stock_list.append("INGN")
    stock_list.append("SGRY")
    stock_list.append("WDR")
    stock_list.append("MRC")
    stock_list.append("PLCE")
    stock_list.append("QHC")
    stock_list.append("NEW")
    stock_list.append("MHLD")
    stock_list.append("QUOT")
    stock_list.append("LBRT")
    stock_list.append("TTMI")
    stock_list.append("ACRS")
    stock_list.append("CROX")
    stock_list.append("GLOG")
    stock_list.append("AIMT")
    stock_list.append("INVA")
    stock_list.append("JMEI")
    stock_list.append("SOI")
    stock_list.append("CSIQ")
    stock_list.append("LPSN")
    stock_list.append("BPFH")
    stock_list.append("BLDR")
    stock_list.append("QNST")
    stock_list.append("TRVG")
    stock_list.append("IRTC")
    stock_list.append("ECHO")
    stock_list.append("JKS")
    stock_list.append("CBAY")
    stock_list.append("OR")
    stock_list.append("SFLY")
    stock_list.append("ITCI")
    stock_list.append("FOE")
    stock_list.append("TLGT")
    stock_list.append("SNCR")
    stock_list.append("ANGO")
    stock_list.append("FCF")
    stock_list.append("VSTO")
    stock_list.append("ABR")
    stock_list.append("JELD")
    stock_list.append("PMT")
    stock_list.append("WGO")
    stock_list.append("HCC")
    stock_list.append("WPRT")
    stock_list.append("FORM")



    for x in stock_list:
        try:
            predictData(x, 5)
        except Exception as e:
            print("BOOM! {0}   {1}".format(x,e))

        
preloadedStocks()

print("The end")
