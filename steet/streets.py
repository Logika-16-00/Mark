streets = "file.txt"

def print_streets(streets):
    with open(streets, 'r', encoding='utf-8') as file:
        content = file.readlines()
        if content:
            for line in content:
                print(line)
print_streets(streets)

def add_street(streets):
    new_entry = input("Введіть новий запис: ")
    with open(streets, 'a', encoding='utf-8') as file:
        file.write(new_entry + '\n')
    print("Вулицю додано.")

def search_street(streets):
    keyword = input("Введіть ключове слово для пошуку: ").lower() 
    with open(streets, 'r', encoding='utf-8') as file:  
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
            add_street(streets)
        elif command == 'друкувати':
            print_streets(streets)
        elif command == 'пошук':
            search_street(streets)
        else:
            print("Невідома команда. Спробуйте ще раз.")
