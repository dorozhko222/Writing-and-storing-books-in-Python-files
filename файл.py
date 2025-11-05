with open("books.txt","w", encoding='utf-8') as file:
    file.write('')
print("Файл записан")
while True:
    print('Что вы хотите сделать? а-удалить книгу, б-добавить книгу, в -найти книгу, г-очистить список,д- перезаписать книгу')
    option = input()
    if option == 'б':
        num = input('Напишите номер книги:')
        name = input('Напишите название книги:')
        data = input('Напишите год издания книги:')
        with open("books.txt", "a", encoding='utf-8') as file:
            file.write(num+') '+name+'-'+data+'г'+".\n")
        print('Книга записана')
    elif option == 'а':

        print('Удалить по: 1-номеру, 2-названию')
        choice = input()
        with open("books.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()
        if choice == '1':
            num_1 = input('Введите номер книги для удаления:')
            new_lines = [line for line in lines if not line.startswith(num_1 + ")")]
        else:
            name_1 = input('Введите название книги для удаления:')
            new_lines = [line for line in lines if name_1 not in  line]
        with open("books.txt", "w", encoding='utf-8') as file:
            file.writelines(new_lines)
        print('Книга удалена')

    elif option == 'в':
        print('Найти по: 1-номеру, 2-названию, 3-году')
        choice = input()
        search = input('Введите значение для поиска:')
        with open("books.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()
        found = False
        for line in lines:
            if choice == '1' and line.startswith(search + ")"):
                print("Найдена:", line.strip())
                found = True
            elif choice == '2' and search in line:
                print("Найдена:", line.strip())
                found = True
            elif choice == '3' and search in line:
                print("Найдена:", line.strip())
                found = True
        if not found:
            print('Книга не найдена')

    elif option == 'г':
        with open("books.txt", "w", encoding='utf-8') as file:
            file.write('')
        print('Книги удалены')

    elif option == 'д':
        book_num = input('Номер книги для изменения: ')
        with open("books.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()
        new_lines = []
        for line in lines:
            if line.startswith(book_num + ")"):
                new_name = input('Новое название: ')
                new_data= input('Новый год: ')
                new_line = book_num+') '+new_name+'-'+new_data+'г'+".\n"
                new_lines.append(new_line)
                print('Книга изменена')
            else:
                new_lines.append(line)
        with open("books.txt",  "w",  encoding='utf-8') as file:
            file.writelines(new_lines)