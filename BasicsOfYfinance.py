import yfinance as yf
import pandas as pd

ticker = yf.Ticker('JPM') # the stock we want
ticker.history (interval ='1m', period = '7d') # The time and duration, period is the number of days months etc and interval is the minutes,hours,etc# gets the data info so info of apple
info = ticker.info # prints the info
calendar = ticker.calendar # prints the calendar
financials = ticker.financials # prints the financials
BalanceSheet = ticker.balance_sheet # prints the balance sheet 
CashFlow = ticker.cashflow # prints the cash flow 
options = ticker.options # options avaliable 
date = ticker.option_chain('2026-01-23') # options price and other info
IHolders = ticker.institutional_holders # holders of the stock
MHolders = ticker.major_holders # major holders of the stock
print(IHolders)


