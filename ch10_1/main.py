import json
import argparse


def main():

    parser = argparse.ArgumentParser(description = 'Convertir un fichier json en csv')
    parser.add_argument('json_file')
    args = parser.parse_args()

    with open('./ch10_1/todos.json') as f:
        data = json.load(f)
        # todo = data[0] 
        # print(todo['title'])
        for todo in data:
            print(todo)

if __name__ == '__main__':
    main()