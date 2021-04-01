
import pandas as pd
from iexfinance.stocks import Stock
from datetime import datetime
import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_data

table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
df.to_csv('S&P500-Info.csv')
df.to_csv("S&P500-Symbols.csv", columns=['Symbol'])
sp = pd.read_csv('S&P500-Symbols.csv', index_col=[0])


def getCompanyInfo(symbols):
    stock_batch = Stock(symbols,
                       token="sk_9f98381e7d8647169d9aa8d5137c5849" )
    company_info = stock_batch.get_company()
    return company_info

sp_company_info = getCompanyInfo(sp["Symbol"][:3].tolist())
print(sp_company_info)
company_info_to_df = []
for company in sp_company_info:
    company_info_to_df.append(sp_company_info[company])
    

columns = ['symbol', 'companyName', 'exchange',
           'industry', 'website', 'CEO', 'sector']
df = pd.DataFrame(company_info_to_df,columns=columns )
print(df['companyName'])
  

def getEarnings(symbol):
    stock_batch = Stock(symbol,
                        token="sk_9f98381e7d8647169d9aa8d5137c5849")
    earnings = stock_batch.get_earnings(last=4)
    return earnings

single_stock_earnings = getEarnings(sp["Symbol"][0])
print(single_stock_earnings)

#def getHistoricalPrices(stock):
 #   return get_historical_data(stock, start, end, 
 #                              output_format='pandas', 
 #                              token="sk_9f98381e7d8647169d9aa8d5137c5849")
 
#start = datetime(2016, 1, 1)
#end = datetime(2019, 7, 30)
#single_stock_history = getHistoricalPrices(sp["Symbol"][0])

#single_stock_history['close'].plot(label="3M Close")