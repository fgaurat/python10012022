import json
import csv
import argparse
import sqlite3
from Todo import Todo
from TodoDAO import TodoDAO

def main():
    dao = TodoDAO('todos.db')

    todos = dao.findAll()

    for todo in todos:
        print(todo)

    completed_todos = dao.findCompleted()
    for todo in completed_todos:
        print(todo)


    todo = Todo(title="Formation Python",completed=True)
    dao.save(todo)


def main_select_todos():
    with sqlite3.connect('todos.db') as con:
        cur = con.cursor()
        sql= "SELECT * FROM todos_tbl"
        for id,userId,title,completed in cur.execute(sql):
            print(title)


def main_insert_todos():
    con = sqlite3.connect('todos.db')
    cur = con.cursor()
    with open("todos.json") as f:
        data = json.load(f)
        for todo in data:
            sql = f"INSERT INTO todos_tbl(user_id,title,completed) VALUES ({todo['userId']},'{todo['title']}',{todo['completed']})"
            cur.execute(sql)
    
    con.commit()
    con.close()

def main_read_csv():
    parser = argparse.ArgumentParser(description = 'Convertir un fichier csv en liste de dictionnaire')
    parser.add_argument('csv_file',help="nom du fichier csv")
    args = parser.parse_args()

    with open(args.csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)


def main_write_csv():

    parser = argparse.ArgumentParser(description = 'Convertir un fichier JSON en csv')
    parser.add_argument('json_file',help="nom du fichier JSON")
    args = parser.parse_args()
    with open(args.json_file) as f:
        data = json.load(f)
        with open('./todos.csv', 'w', newline='') as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)




if __name__ == '__main__':
    main()