with open("quotes.txt", "r",encoding="utf-8") as file:
    for line in file:
        print(line)

a = input("Хто написав?")
with open("quotes.txt", "a", encoding="utf-8") as file:
    file.write("\n "+a+" \n")

while 1:
    b = input("чи хочеш додати").lower()
    if b =="ні":
        break
    else:
        q = input("цитата:")
        with open("quotes.txt", "q", encoding="utf-8") as file: 
            file.write("\n "+a+" \n")
        a = input("Хто написав?")
        with open("quotes.txt", "q", encoding="utf-8") as file:
            file.write("\n "+a+" \n")