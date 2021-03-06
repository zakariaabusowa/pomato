import dbutils
import json
import firebase_admin
from firebase_admin import credentials, messaging, db
from pyfcm import FCMNotification


push_service = FCMNotification(api_key="AAAAN1izv4E:APA91bGTJ-EYBQ2FwB74OuNlH2T69YR2mnDSZx6c2Z367oFCCl7BxdrVEWiGZnnMpoKSAxiIylwC0MZjx4-SFbdWxDC4GYAeNTPpDjXoiUt2u-d_z5LJXF3SVmfpov8fDUk2J6qiMlEz")

cred = credentials.Certificate('stocker-929ba-firebase-adminsdk-vewwh-49d6164e1d.json')

firebase_admin.initialize_app(cred, {

    'databaseURL' : 'https://stocker-929ba-default-rtdb.firebaseio.com/'
})



class STOCKCheck():
    def __init__(self):
        self.con = dbutils.getDBConnection(self)
        self.cur = self.con.cursor()

    def usaRtx3090(self):
        #cardsNumber=["firstcard","secondcard","thirdcard","forthcard","fifthcard"]
        cards=["rtx3090","rtx3080","rtx3070","rtx3060","rx6900","rx6800","rx6700"]

        for card in cards:
            idn = 1
            myQuery="SELECT price FROM "+card+";"
            myQuery2="SELECT last_price FROM "+card+" WHERE id = %s;"
            myQuery3="UPDATE "+card+" SET last_price = %s where id = %s;"
            if card[0:3] == "rtx":
                cardType="nvidia"
            else:
                cardType="amd"
            try:
                print(idn)#testing
                self.cur.execute(myQuery)
                getPriceByIdResult = self.cur.fetchall()
                getPriceByIdCount = self.cur.rowcount
                if getPriceByIdCount > 0:
                    for row in getPriceByIdResult:
                        for key, value in row.items():
                                if key == 'price': 
                                        self.cur.execute(myQuery2,(idn))
                                        last_price=self.cur.fetchone()
                                        for key2, value2 in last_price.items():
                                            if value != value2 :
                                                if idn == 1 :
                                                    cardNumber = "firstcard"
                                                elif idn == 2:
                                                    cardNumber = "secondcard"
                                                elif idn == 3:
                                                    cardNumber = "thirdcard"
                                                elif idn == 4:
                                                    cardNumber = "forthcard"
                                                elif idn == 5:
                                                    cardNumber = "fifthcard"
                                                print(cardNumber)#testing
                                                   
                                                myQuery4="select country from "+card+" where id = %s;"
                                                self.cur.execute(myQuery4,(idn))
                                                getCountryByIdResult = self.cur.fetchone()
                                                for key, countryName in getCountryByIdResult.items():
                                                    country = countryName
                                                print (country)#testing 
                                                ref = db.reference(country+'/graphicCards/'+cardType+'/'+card+'/'+cardNumber)
                                                ref.update( {'price' : value} )
                                                
                                                
                                                message_title = card.strip('[]')
                                                print(message_title)
                                                message_body = "IN STOCK NOW!!, Hurry and get it."
                                                push_service.notify_topic_subscribers(topic_name=card+"notification", message_title=message_title, message_body=message_body)
                                                
                                                print('......... Something Have Changed :):) .........')#testing
                                                
                                                self.cur.execute(myQuery3,(value,idn))
                                                self.con.commit()
                                                self.con.close
                                                idn = idn+1
                                                print(idn)
                                            else:
                                                
                                                print('......... Nothing Have Changed :(:( .........')#testing
                                                idn = idn+1
                                                print(idn)#testing
                                                message_title = card.strip('[]')
                                                print(message_title)
                                else:
                                    return "value not exist"
                        continue            
                else:
                    self.con.close
                    return "", 0
            except Exception as e:
                print('error::stockerDBMODEL::getData::{}'.format(str(e)))
                self.con.close

            finally:
                print(card+" Done checking")
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