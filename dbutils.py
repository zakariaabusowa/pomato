import pymysql

def getDBConnection(self):
    host = "localhost"
    user = "root"
    password = "itAdm!n19"
    db = "stockerdb"
    self.stockerdbcon = pymysql.connect(host=host, user=user, password=password,db=db, cursorclass=pymysql.cursors.DictCursor, charset='utf8', use_unicode=True)
    return self.stockerdbcon