from config import Config
import MySQLdb

class Connection:
    def __init__(self):
        self.db=MySQLdb.connect(
            Config.DATABASE_CONFIG['server'],
            Config.DATABASE_CONFIG['user'],
            Config.DATABASE_CONFIG['password'],
            Config.DATABASE_CONFIG['name']
            )
        self.db.autocommit(True)
        self.db.set_character_set('utf8mb4')
        self.cur=self.db.cursor()

    #New Method EXAMPLE: row = Connection().select(query,[chat])
    def select(self,sql,args=None):
        self.cur.execute(sql,args)
        self.sel = self.cur.fetchone()
        self.cur.close()
        self.db.close()
        return self.sel

    def selectAll(self,sql,args=None):
        self.cur.execute(sql,args)
        self.sel = self.cur.fetchall()
        self.cur.close()
        self.db.close()
        return self.sel

    def getUserById(self,args=None):
        sql = "SELECT * FROM users WHERE user_id = %s"
        self.cur.execute(sql,args)
        self.sel = self.cur.fetchall()
        self.cur.close()
        self.db.close()
        return self.sel

    def getGroupsById(self,args=None):
        sql = "SELECT * FROM groups WHERE id_group = %s"
        self.cur.execute(sql,args)
        self.sel = self.cur.fetchall()
        self.cur.close()
        self.db.close()
        return self.sel