from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import re
#from selenium import webdriver



'''
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')
'''



URL = 'https://www.amazon.com/b/ref=s9_acss_bw_h1_PCCH1201_md2_w?ie=UTF8&node=284822&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-1&pf_rd_r=QCXEZNQW6C3C51YKY6V4&pf_rd_t=101&pf_rd_p=bcef9d69-a799-4d66-9754-a5b56df4a0cf&pf_rd_i=193870011'
 
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "lxml")

title = soup.find(class_='a-size-medium a-color-base a-text-normal').get_text()#'span', class_='a-size-medium a-color-base a-text-normal').get_text()
print(title)

'''
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[5:11])

    img = soup.find_all('img', {'src':re.compile('.jpg')})

    print(converted_price)
'''

'''
    for item in img :
        print(item['src']+'\n')
'''


'''
if __name__ == '__main__':
    app.debug = True
    app.run()
   '''
    
'''
    get = driver.get(URL)

driver = webdriver.Firefox()


html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

title = soup.find(id="productTitle")

print(title.text.strip('/n'))'''
