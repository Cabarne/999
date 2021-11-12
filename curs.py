
import requests
from bs4 import BeautifulSoup


link = 'https://www.bnm.md/ru/content/obmennye-stavki'


responce  = requests.get(link).text

soup = BeautifulSoup(responce, 'lxml')

block = soup.find( 'div', id="ajax-wrapper-table")

block_currency = block.find_all('tr')[13] # block currency Euro

exchange = block.find_all('span')[12].text # exchange rate

currency = block_currency.find_all('td')[0].text # currency

result_exchange = f"Curency EUR - MDL >>> {exchange} MDL"

total_exchange = float(exchange) 


# print(total_exchange)



