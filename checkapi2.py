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
        idn = 1
        myQuery= "SELECT price FROM usa_rtx3090;"
        myQuery2="SELECT last_price FROM usa_rtx3090 WHERE id = %s;"
        myQuery3="UPDATE usa_rtx3090 SET last_price = %s where id = %s;"
        try:
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
                                    ref = db.reference('USA/graphicCards/nvidia/rtx3090')
                                    ref.update( {'price' : value} )

                                    message_title = "Rtx 3090"
                                    message_body = "IN STOCK NOW!!, Hurry and get it."
                                    push_service.notify_topic_subscribers(topic_name="rtx3080notification", message_title=message_title, message_body=message_body)

                                    print('......... Something Have Changed :):) .........')#testing
                                    
                                    self.cur.execute(myQuery3,(value,idn))
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