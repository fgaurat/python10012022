import json

def main():
    with open('todos.json') as f:
        data = json.load(f)
        todo = data[0] 
        print(todo['title'])

def main_write_json():
    data = [{
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    },
        {
        "userId": 1,
        "id": 2,
        "title": "quis ut nam facilis et officia qui",
        "completed": False
    },
        {
        "userId": 1,
        "id": 3,
        "title": "fugiat veniam minus",
        "completed": False
    },
        {
        "userId": 1,
        "id": 4,
        "title": "et porro tempora",
        "completed": True
    }]

    with open('todos.json','w') as f:
        # s= json.dumps(data)
        # print(type(data))
        # print(type(s))
        json.dump(data,f)
        # print(data,file=f)


# Lecture csv
def main_read_csv():

    with open('todos.csv') as f:
        lines = [l.strip() for l in f.readlines()]
        out = []
        header = lines[0]
        data = lines[1:]
        for d in data:
            h = header.split(";")
            v = d.split(";")
            todo = dict(zip(h, v))
            out.append(todo)

        print(out)

# Ecriture csv


def main_write_csv():
    # http://jsonplaceholder.typicode.com/todos
    data = [{
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    },
        {
        "userId": 1,
        "id": 2,
        "title": "quis ut nam facilis et officia qui",
        "completed": False
    },
        {
        "userId": 1,
        "id": 3,
        "title": "fugiat veniam minus",
        "completed": False
    },
        {
        "userId": 1,
        "id": 4,
        "title": "et porro tempora",
        "completed": True
    }]

    with open('todos.csv', 'w') as f:
        headers = data[0].keys()
        print(*headers, sep=";", file=f)
        for todo in data:
            v = todo.values()
            print(*v, sep=";", file=f)


def main_1():
    with open(r"lefichier.txt", "w") as f:
        # f.write("Toto\n")
        # f.write("Titi\n")
        print("Toto", file=f)
        print("Titi", file=f)
        print("Toto", file=f)
        print("Titi", file=f)

    with open(r"lefichier.txt", "r") as f:
        # Lit la totalité dans une chaîne
        # data = f.read()
        # print(data)
        data = f.readlines()
        print(data)
        for n, line in enumerate(data):
            s = f"ligne {n+1} {line.strip()}"
            print(s)

        # ligne 1 : Toto
        # ligne 2 : Titi


if __name__ == '__main__':
    main()
