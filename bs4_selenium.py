from os import sep
from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
import dbutils
from time import sleep
import pandas as pd


#DRIVER_PATH = str(Path('chromedriver').resolve())
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
class Amazon():
    def __init__(self):
        self.con = dbutils.getDBConnection(self)
        self.cur = self.con.cursor()


    def amazonCards(self):
        idn = 1
        #make more queries to hold the other tables and create an if statment to check if the idn < 6 if so change the query to another card
        cardsType=["rtx3090","rtx3080","rtx3070","rtx3060","rx6900","rx6800","rx6700"]
        for cardType in cardsType:
            myQuery = "select url from "+cardType+";"
            self.cur.execute(myQuery)
            urls = self.cur.fetchall()
            for row in urls:
                for key, value in row.items():
                    driver.get(value)
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'lxml')
                    cards = soup.find_all('div', {'id': 'dp','class': 'pc en_US' })
                    for card in cards:
                        try:
                            price = card.find('span', class_='a-size-medium a-color-price').text.strip(',').strip()
                        except:
                            price = ''
                        else:
                            price = ''.join(price.split(','))
                            print(price)
                        try:
                            title = card.find('span', class_='a-size-large product-title-word-break').text.strip()
                        except:
                            title = ''
                        else:
                            title = ''.join(title.split(','))
                            print(title)

                        try:
                            rating = card.find('span', class_='a-icon-alt').text.strip()
                        except:
                            rating = ''
                        else:
                            rating = ''.join(rating.split(','))    
                            print (rating)
                        print("Done Scraping")

                        myQuery2 = "UPDATE "+cardType+" set title = %s, price = %s WHERE id = %s;"
                        try:
                            self.cur.execute(myQuery2,(title,price,idn))
                            self.con.commit()
                            idn=idn+1
                            print(idn)
                            rowCountResult = self.cur.rowcount
                            lastRowId = self.cur.lastrowid
                            if rowCountResult > 0:
                                self.con.close
                                print (lastRowId)
                                sleep(10)
                            else:
                                self.con.close
                        except Exception as e:
                            print('error::stockerDBMODEL::getData::{}'.format(str(e)))
                            self.con.close
                        
                        


            
'''
            data={'title': title,'price': price}
            print (data)
            return data
'''
'''
 def addCard(self, title, price):
        myQuery = "INSERT INTO `usa_rtx3090` (`title`,`price`) VALUES (%s,%s);"
        try:
            self.cur.execute(myQuery,(title,price))
            self.con.commit()
            rowCountResult = self.cur.rowcount
            lastRowId = self.cur.lastrowid
            if rowCountResult > 0:
                self.con.close
                return lastRowId
            else:
                self.con.close
                return 0
        except Exception as e:
            self.con.rollback
            self.con.close
            return 0
        
'''



''''
import requests
from bs4 import BeautifulSoup

url='https://www.amazon.com/dp/B08HR5SXPS/?coliid=IHXESHSBC60PX&colid=6GEW9TQ8VS1D&psc=0&ref_=lv_vv_lig_dp_it'

r = requests.get(url)

print(r.status_code)

soup = BeautifulSoup(r.content,"html.parser")

price = soup.find('class_=a-size-medium a-color-price').get_text()

def getTimeAlasr():
    return price

dd = getTimeAlasr()
print(dd)





URL = 'https://www.amazon.com/dp/B08HR5SXPS/?coliid=IHXESHSBC60PX&colid=6GEW9TQ8VS1D&psc=0&ref_=lv_vv_lig_dp_it' 
#headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

page = requests.get(URL)

soup = BeautifulSoup(page.content, "lxml")

title = soup.find(class_="a-size-medium a-color-price").get_text()#'span', class_='a-size-medium a-color-base a-text-normal').get_text()
print(title)
'''