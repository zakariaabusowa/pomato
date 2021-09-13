from os import sep
from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
import dbutils
from time import sleep
import pandas as pd
import requests


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

class Amazon():
    def __init__(self):
        self.con = dbutils.getDBConnection(self)
        self.cur = self.con.cursor()


    def amazonCards(self):
        idn = 1
        cardsType=["rtx3090","rtx3080","rtx3070","rtx3060","rx6900","rx6800","rx6700"]
        for cardType in cardsType:
            myQuery = "select url from "+cardType+";"
            self.cur.execute(myQuery)
            urls = self.cur.fetchall()
            for row in urls:

                for key, value in row.items():
                    html = requests.get(value, headers= header).text
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












