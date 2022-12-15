import sqlite3
from todoitem import Todoitem
connection = sqlite3.connect('mydatabase.db')
""" cursor = connection.cursor()
cursor.execute("DROP TABLE todolist") """
class DataService:
    def __init__(self):
        self.connection = sqlite3.connect('mydatabase.db')
        self.cursor = self.connection.cursor()
        if (not self._checkTableExists('todolist')):
            self.cursor.execute("""CREATE TABLE todolist (id INTEGER PRIMARY KEY, date text,_from text,_to text,task text,tag text)""")
            self.connection.commit()

    def _checkTableExists(self, tablename):
        self.cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name= :tablename ''',{'tablename':tablename})
        if self.cursor.fetchone()[0]==1 : 
            return True
        else:
            return False
        


    def _toToDoArray(self, dbarray):
        result = []
        for todo in dbarray:
            result.append(Todoitem(todo[1],todo[2],todo[3],todo[4],todo[5],todo[0]))
        return result

    def _getToDoItem(self,id):
        self.cursor.execute("SELECT * FROM todolist where id = :id",{'id':id})
        return self._toToDoArray(self.cursor.fetchall())

   
    
    def addToDoItem(self, item):
        self.cursor.execute("INSERT INTO todolist VALUES (NULL, ?,?,?,?,?)",(item.DATE,item.FROM,item.TO,item.TASK,item.TAG))
        self.connection.commit()
        
    def deleteToDoItem(self, id):
        if(len(self._getToDoItem(id))==0):
            return False
        else: 
            self.cursor.execute("DELETE FROM todolist WHERE id = :id",{'id':id})
            self.connection.commit()
            return True
        
    def getPrioTask(self):
        self.cursor.execute("select * FROM todolist GROUP BY task,tag ORDER BY COUNT(*) DESC")
        return self._toToDoArray(self.cursor.fetchall())
    
    def getByDate(self,value):
        self.cursor.execute("SELECT * FROM todolist where date = :value",{'value':value})
        return self._toToDoArray(self.cursor.fetchall())

    def getByTask(self,value):
        self.cursor.execute("SELECT * FROM todolist where task = :value",{'value':value})
        return self._toToDoArray(self.cursor.fetchall())
    
    def getByTag(self,value):
        self.cursor.execute("SELECT * FROM todolist where tag = :value",{'value':value})
        return self._toToDoArray(self.cursor.fetchall())

    def getByDateFromTo(self, start, end):
        self.cursor.execute("SELECT * FROM todolist where date BETWEEN :start AND :end",{'start':start,'end':end})
        return self._toToDoArray(self.cursor.fetchall())


   
    def getAllItems(self):
        self.cursor.execute("SELECT * FROM todolist")
        return self._toToDoArray(self.cursor.fetchall())

    def drop(self):
        self.cursor.execute("DROP TABLE todolist")
        connection.commit()
    def __del__(self):
        self.connection.close()

#testDataService = DataService()
#print(testDataService._checkTableExists("asdf"))
#print(testDataService._checkTableExists("todolist"))
