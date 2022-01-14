import sqlite3
from Todo import Todo

class TodoDAO:

    def __init__(self,db_file) -> None:
        self._con = sqlite3.connect(db_file)

    def findAll(self):
        cur = self._con.cursor()
        sql= "SELECT * FROM todos_tbl"
        for id,userId,title,completed in cur.execute(sql):
            todo = Todo(id=id,completed=bool(completed),title=title,userId=userId)
            yield todo


    def findCompleted(self):
        cur = self._con.cursor()
        sql= "SELECT * FROM todos_tbl WHERE completed=1"
        for id,userId,title,completed in cur.execute(sql):
            todo = Todo(id=id,completed=bool(completed),title=title,userId=userId)
            yield todo


    def save(self,todo):
        cur = self._con.cursor()
        sql = f"INSERT INTO todos_tbl(user_id,title,completed) VALUES ({todo.userId},'{todo.title}',{todo.completed})"
        cur.execute(sql)
        self._con.commit()

    def __del__(self):
        self._con.close()
