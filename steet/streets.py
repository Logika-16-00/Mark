filename = "file.txt"

def print_file_content(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.readlines()
        if content:
            for line in content:
                print(line)

def add_street(filename):
    new_entry = input("Введіть новий запис: ")
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(new_entry + '\n')
    print("Вулицю додано.")

def search_in_file(filename):
    keyword = input("Введіть ключове слово для пошуку: ").lower() 
    with open(filename, 'r', encoding='utf-8') as file:  
        found = False  
        for line in file:
            if keyword in line.lower(): 
                print(line)  
                found = True
            else:
                print("Ключове слово не знайдено.")
while True:
        command = input("\nВведіть команду (вийти, додати, друкувати, пошук): ").lower()
        
        if command == 'вийти':
            print("Програма завершила роботу.")
            break
        elif command == 'додати':
            add_street(filename)
        elif command == 'друкувати':
            print_file_content(filename)
        elif command == 'пошук':
            search_in_file(filename)
        else:
            print("Невідома команда. Спробуйте ще раз.")
