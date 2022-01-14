import json

def main():
    with open('todos.json') as f:
        data = json.load(f)
        todo = data[0] 
        print(todo['title'])

if __name__ == '__main__':
    main()