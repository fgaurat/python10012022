import sqlite3
from Todo import Todo

class TodoDAO:

    def __init__(self,db_file) -> None:
        self._con = sqlite3.connect(db_file)

    def findAll(self):
        cur = self._con.cursor()
        sql= "SELECT * FROM todos_tbl"
        for data in cur.execute(sql):
            todo = Todo(*data)
            yield todo


    def findCompleted(self):
        pass

    def save(self):
        pass
    

    def __del__(self):
        self._con.close()
