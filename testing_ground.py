'''
def get_value(_key):
    for key, value in my_dict.items():
        if _key == key:
            return value
    return "value not exist"

my_dict ={"java":100, "python":112,"c":11}
print(get_value('java'))
print(get_value('c'))
'''
'''
import json
data= {}
data['3090asus']=[]


data['3090asus'].append({
    'price' : '1000'
})

with open('mydata.json', 'w') as f:
    json.dump(data, f)
'''
'''
import pandas as pd
import json
f = open('myurls.json')
urls_pd= json.load(f)
#urls = urls_pd.url
for urls_pd['url'][0+1] in enumerate(urls_pd):
    print('1211')
    '''
'''
import dbutils
class Amazon():
    def __init__(self):
        self.con = dbutils.getDBConnection(self)
        self.cur = self.con.cursor()


    def L(self):
        myQuery = "select url from usa_rtx3090urls;"
        self.cur.execute(myQuery)
        urls = self.cur.fetchall()
        for row in urls:
            for key, value in row.items():
                print(value)    
'''
'''


import dbutils
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('stocker-929ba-firebase-adminsdk-vewwh-6c7f47e220.json')

firebase_admin.initialize_app(cred, {

    'databaseURL' : 'https://stocker-929ba-default-rtdb.firebaseio.com/'
})



class STOCKCheck():
    def __init__(self):
        self.con = dbutils.getDBConnection(self)
        self.cur = self.con.cursor()
        self.priceHasChanged = {}

    def usaRtx3090(self):
        idn = 1
        myQuery= "SELECT price FROM usa_rtx3090;"
        myQuery2="SELECT last_price FROM usa_rtx3090 WHERE id = %s;"
        myQuery3="SELECT last_price FROM usa_rtx3090 WHERE id = %s;"
        myQuery4="UPDATE usa_rtx3090 SET last_price = %s where id = %s;"
        try:
            self.cur.execute(myQuery)
            getPriceByIdResult = self.cur.fetchall()
            getPriceByIdCount = self.cur.rowcount
            if getPriceByIdCount > 0:
                for row in getPriceByIdResult:
                    for key, value in row.items():
                        if key == 'price':
                            if idn < 6:
                                theQuery = myQuery2
                            elif idn > 6:
                                theQuery = myQuery3
                            self.cur.execute(theQuery,(idn))
                            last_price=self.cur.fetchone()
                            for key2, value2 in last_price.items():
                                if value != value2 :
                                    ref = db.reference('rtx3080')
                                    ref.update( {'price' : value} )

                                    print('......... Something Have Changed :):) .........')#testing
                                    
                                    self.cur.execute(myQuery4,(value,idn))
                                    self.con.commit()
                                    self.con.close
                                    idn = idn+1
                                else:
                                    idn = idn+1
                        else:
                            return "value not exist"
            else:
                self.con.close
                return "", 0
        except Exception as e:
            print('error::stockerDBMODEL::getData::{}'.format(str(e)))
            self.con.close


'''


'''
        myQuery2= "SELECT price FROM usa_rtx3090 where id = '2';"
        try:
            self.cur.execute(myQuery2)
            getCardByIdResult = self.cur.fetchone()
            getCardByIdCount = self.cur.rowcount
            if getCardByIdCount > 0:
                for key, value in getCardByIdResult.items():
                    if key == 'price':
                        f = open('mydata2.json')
                        self.priceHasChanged = json.load(f)

                        if value != self.priceHasChanged :
                            ref = db.reference('USA')
                            ref.update( {'graphicCards/nvidia/rtx3090/firstcard/price' : value} )

                            print('......... Something Have Changed :):) .........')#testing

                            self.priceHasChanged = value
                            with open('mydata2.json', 'w') as f:
                                json.dump(self.priceHasChanged, f)
                    else:
                        return "value not exist"
            else:
                self.con.close
                return "", 0
        except Exception as e:
            print('error::stockerDBMODEL::getData::{}'.format(str(e)))
            self.con.close
'''



'''
import dbutils
class STOCKCheck():
    def __init__(self):
        self.con = dbutils.getDBConnection(self)
        self.cur = self.con.cursor()
    def l(self):
        myQuery1="SELECT name FROM tablesnames"
        myQuery= "SELECT price FROM %s;"

        self.cur.execute(myQuery1)
        getPriceByIdResult = self.cur.fetchall()
        getPriceByIdCount = self.cur.rowcount
        for row in getPriceByIdResult:
            for key, value in row.items():
                print(value)
                try:
                    self.cur.execute(myQuery,(value[0:2]))
                    getPriceByIdResult = self.cur.fetchall()
                    getPriceByIdCount = self.cur.rowcount
                    print(getPriceByIdResult)
                except Exception as e:
                    print('error::stockerDBMODEL::getData::{}'.format(str(e)))
                    self.con.close
'''

'''
import dbutils
class STOCKCheck():
    def __init__(self):
        self.con = dbutils.getDBConnection(self)
        self.cur = self.con.cursor()
    def l(self):
        myQuery="SELECT * from cardsurls;"
        myQuery1="UPDATE usa_rtx3090 set price = '1000$' where id = %s"

        idn1= 1

        self.cur.execute(myQuery)
        getPriceByIdResult = self.cur.fetchall()
        getPriceByIdCount = self.cur.rowcount
        for row in getPriceByIdResult:
            for key, value in row.items():
                if key ==('rtx3090'):
                    self.cur.execute(myQuery1(idn1))
                    idn1 =idn1+1
                elif key ==('rtx3080'):
                    self.cur.execute(myQuery2)
                elif key ==('rtx3060'):
                    self.cur.execute(myQuery3)
                elif key ==('rtx3070'):
                    self.cur.execute(myQuery4)

'''


'''
import dbutils
import json
import firebase_admin
from firebase_admin import credentials, messaging, db


cred = credentials.Certificate('stocker-929ba-firebase-adminsdk-vewwh-49d6164e1d.json')

firebase_admin.initialize_app(cred, {

    'databaseURL' : 'https://stocker-929ba-default-rtdb.firebaseio.com/'
})

# The topic name can be optionally prefixed with "/topics/".
topic = 'all'                                    # See documentation on defining a message payload.
message = messaging.Message(
data={
    'cardname': 'rtx3090',
    'catchphrase': 'In Stock Hurry Now!',
                    },
    topic=topic,
    )
                                    # Send a message to the devices subscribed to the provided topic.
response = messaging.send(message)
                                    # Response is a message ID string.
print('Successfully sent message:', response)
'''

'''
from pyfcm import FCMNotification
push_service = FCMNotification(api_key="AAAAN1izv4E:APA91bGTJ-EYBQ2FwB74OuNlH2T69YR2mnDSZx6c2Z367oFCCl7BxdrVEWiGZnnMpoKSAxiIylwC0MZjx4-SFbdWxDC4GYAeNTPpDjXoiUt2u-d_z5LJXF3SVmfpov8fDUk2J6qiMlEz")

message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"

result = push_service.notify_topic_subscribers(topic_name="all", message_title=message_title, message_body=message_body)
'''

'''
import requests
from bs4 import BeautifulSoup

def so():
    url='https://www.amazon.com/dp/B08HR5SXPS/?coliid=IHXESHSBC60PX&colid=6GEW9TQ8VS1D&psc=0&ref_=lv_vv_lig_dp_it'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

    r = requests.get(url, headers=headers)
    print(r.status_code)
                
    soup = BeautifulSoup(r.content, 'lxml')
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
'''


cards=["rtx3090","rtx3080","rtx3070","rtx3060","rx6900","rx6800","rx6700"]

for card in cards:
    if card[0:3] == "rtx":
        print("nvidia card")
    else:
        print("amd card")

'''


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