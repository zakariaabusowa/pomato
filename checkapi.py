import dbutils


class STOCKCheck():
    def __init__(self):
        self.con = dbutils.getDBConnection(self)
        self.cur = self.con.cursor()


    def getData(self, id):
        myQuery= "SELECT price FROM rtx_3080 where id = %s;"
        try:
            self.cur.execute(myQuery,id)
            getCardByIdResult = self.cur.fetchone()
            getCardByIdCount = self.cur.rowcount
            if getCardByIdCount > 0:
                print(getCardByIdResult)
                #return getCardByIdResult, getCardByIdCount
                for key, value in getCardByIdResult.items():
                    if key == 'price':
                        if len(value) != 22 :
                            print('.........IN STOCK!!!!.........')#testing
                        else:
                            print('')#testings
                    else:
                        return "value not exist"
            else:
                self.con.close
                return "", 0
        except Exception as e:
            print('error::stockerDBMODEL::getData::{}'.format(str(e)))
            self.con.close
         
      
'''
    print(get_value('price'))
    
    def get_value(self,_key='price'):
        for key, value in getUserByIdResult.items():
            if _key == key:
                return value
        return "value not exist"

    print(get_value('price'))  
    '''