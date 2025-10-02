import csv

library = {
    "Война и мир": {"Автор": "Л. Толстой", "Год": 1869, "Рейтинг": [5, 4, 5]},
    "Преступление и наказание": {"Автор": "Ф. Достоевский", "Год": 1866, "Рейтинг": [5, 5, 4]}
}

def menu():
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Найти книгу по названию")
        print("4. Удалить книгу")
        print("5. Добавить новую оценку книге")
        print("6. Книги, выпущенные после определённого года")
        print("7. Книги с рейтингом выше порога")
        print("8. Экспорт в CSV")
        print("9. Импорт из CSV")
        print("0. Выход")

        choice = input("Введите номер действия: ").strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            show_books()
        elif choice == '3':
            find_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            add_rating()
        elif choice == '6':
            books_after_year()
        elif choice == '7':
            books_above_rating()
        elif choice == '8':
            export_to_csv()
        elif choice == '9':
            import_from_csv()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

def add_book():
    title = input("Введите название книги: ").strip()
    if title in library:
        print("Книга уже есть в библиотеке.")
        return

    author = input("Введите автора: ").strip()
    
    try:
        year = int(input("Введите год издания: ").strip())
    except ValueError:
        print("Год должен быть числом.")
        return

    library[title] = {"Автор": author, "Год": year, "Рейтинг": []}
    print(f"Книга '{title}' добавлена.")

def show_books():
    if not library:
        print("Библиотека пустая.")
        return

    for title, data in library.items():
        ratings = data["Рейтинг"]
        avg_rating = round(sum(ratings) / len(ratings), 2) if ratings else "нет оценок"
        print(f"{title} — {data['Автор']} ({data['Год']}) | Оценки: {ratings} | Средняя оценка: {avg_rating}")

def find_book():
    search = input("Введите название книги: ").strip()
    for title, data in library.items():
        if title.lower() == search.lower():
            ratings = data["Рейтинг"]
            avg_rating = round(sum(ratings)/len(ratings),2) if ratings else "нет оценок"
            print(f"Найдена: {title} — {data['Автор']} ({data['Год']}) | Оценки: {ratings} | Средняя оценка: {avg_rating}")
            return
    print("Книга не найдена.")

def delete_book():
    title = input("Введите название книги для удаления: ").strip()
    if title in library:
        del library[title]
        print(f"Книга '{title}' удалена.")
    else:
        print("Книга не найдена.")

def add_rating():
    title = input("Введите название книги для оценки: ").strip()
    if title not in library:
        print("Книга не найдена.")
        return

    try:
        rating = int(input("Введите оценку 1-5: ").strip())
        if rating < 1 or rating > 5:
            raise ValueError
    except ValueError:
        print("Оценка должна быть числом от 1 до 5.")
        return

    library[title]["Рейтинг"].append(rating)
    print(f"Оценка {rating} добавлена к книге '{title}'.")

def books_after_year():
    try:
        year = int(input("Введите год: ").strip())
    except ValueError:
        print("Год должен быть числом.")
        return

    found = False
    for title, data in library.items():
        if data["Год"] > year:
            print(f"{title} — {data['Автор']} ({data['Год']})")
            found = True
    if not found:
        print(f"Нет книг, выпущенных после {year}.")

def books_above_rating():
    try:
        threshold = float(input("Введите порог рейтинга: ").strip())
    except ValueError:
        print("Порог должен быть числом.")
        return

    found = False
    for title, data in library.items():
        ratings = data["Рейтинг"]
        if ratings:
            avg_rating = sum(ratings)/len(ratings)
            if avg_rating > threshold:
                print(f"{title} — {data['Автор']} ({data['Год']}) | Средняя оценка: {round(avg_rating,2)}")
                found = True
    if not found:
        print(f"Нет книг с рейтингом выше {threshold}.")

def export_to_csv():
    filename = input("Введите имя файла для экспорта: ").strip()
    try:
        file = open(filename, mode='w', newline='', encoding='utf-8')
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")
        return
    else:
        try:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(["Название", "Автор", "Год", "Оценки"])
            for title, data in library.items():
                ratings = ','.join(map(str, data["Рейтинг"]))
                writer.writerow([title, data["Автор"], data["Год"], ratings])
        except Exception as e:
            print(f"Ошибка при записи: {e}")
        else:
            print(f"Библиотека экспортирована в {filename}.")
        finally:
            file.close()

def import_from_csv():
    filename = input("Введите имя файла для импорта: ").strip()
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                if len(row) != 4:
                    print(f"Неверный формат строки: {row}")
                    continue
                title, author, year, ratings_str = row
                try:
                    year = int(year)
                    ratings = list(map(int, ratings_str.split(','))) if ratings_str else []
                except ValueError:
                    print(f"Ошибка в данных книги: {row}")
                    continue
                library[title] = {"Автор": author, "Год": year, "Рейтинг": ratings}
        print(f"Библиотека импортирована из {filename}.")
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Ошибка при импорте: {e}")


if __name__ == "__main__":
    menu()
