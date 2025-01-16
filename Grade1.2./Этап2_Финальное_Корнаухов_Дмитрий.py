from datetime import datetime

# Хранилище заметок
notes = []

# Функция для добавления заголовков
def add_titles():
    print("Введите заголовки заметок. Для завершения нажмите Enter.")
    while True:
        title = input("Введите заголовок (или оставьте пустым для завершения): ")
        if not title:
            break
        if any(note['Заголовок'] == title for note in notes):
            print("Заголовок уже существует. Попробуйте другой.")
        else:
            notes.append({
                "Имя": None,
                "Заголовок": title,
                "Описание": None,
                "Статус": "новая",
                "Дата создания": datetime.now().strftime("%d-%m-%Y"),
                "Дедлайн": None,
            })
    print("\nЗаголовки добавлены.")

# Функция для обновления статуса заметки
def update_status():
    if not notes:
        print("Нет заметок для обновления статуса.")
        return
    print("Список заметок:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. Заголовок: {note['Заголовок']}, Статус: {note['Статус']}")
    try:
        index = int(input("Введите номер заметки для обновления статуса: ")) - 1
        if 0 <= index < len(notes):
            statuses = ["выполнено", "в процессе", "отложено"]
            print("Выберите новый статус:")
            for i, status in enumerate(statuses, 1):
                print(f"{i}. {status}")
            choice = int(input("Ваш выбор: "))
            if 1 <= choice <= len(statuses):
                notes[index]['Статус'] = statuses[choice - 1]
                print("Статус успешно обновлён.")
            else:
                print("Некорректный выбор.")
        else:
            print("Некорректный номер заметки.")
    except ValueError:
        print("Введите корректное число.")

# Функция для проверки дедлайна
def check_deadline():
    current_date = datetime.now().strftime("%d-%m-%Y")
    print(f"Текущая дата: {current_date}")
    try:
        deadline = input("Введите дату дедлайна (в формате день-месяц-год): ")
        deadline_date = datetime.strptime(deadline, "%d-%m-%Y")
        current_date_obj = datetime.strptime(current_date, "%d-%m-%Y")
        delta = (deadline_date - current_date_obj).days
        if delta < 0:
            print(f"Внимание! Дедлайн истёк {-delta} дней назад.")
        else:
            print(f"До дедлайна осталось {delta} дней.")
    except ValueError:
        print("Некорректный формат даты.")

# Функция для добавления заметок
def add_notes():
    while True:
        name = input("Введите имя пользователя: ")
        title = input("Введите заголовок заметки: ")
        description = input("Введите описание заметки: ")
        status = input("Введите статус заметки (новая, в процессе, выполнено): ")
        creation_date = datetime.now().strftime("%d-%m-%Y")
        deadline = input("Введите дедлайн (день-месяц-год, или оставьте пустым): ")
        notes.append({
            "Имя": name,
            "Заголовок": title,
            "Описание": description,
            "Статус": status,
            "Дата создания": creation_date,
            "Дедлайн": deadline if deadline else None,
        })
        cont = input("Хотите добавить ещё одну заметку? (да/нет): ").strip().lower()
        if cont != "да":
            break

# Функция для удаления заметок
def delete_note():
    global notes
    if not notes:
        print("Список заметок пуст.")
        return
    print("Список заметок:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. Имя: {note['Имя']}, Заголовок: {note['Заголовок']}")
    criteria = input("Введите имя пользователя или заголовок для удаления заметки: ")
    filtered_notes = [note for note in notes if note["Имя"] != criteria and note["Заголовок"] != criteria]
    if len(filtered_notes) == len(notes):
        print("Заметок с таким именем пользователя или заголовком не найдено.")
    else:
        notes = filtered_notes
        print("Заметка успешно удалена.")

# Главное меню
def main_menu():
    while True:
        print("\nМенеджер заметок:")
        print("1. Добавить заголовки")
        print("2. Обновить статус заметки")
        print("3. Проверить дедлайн")
        print("4. Добавить заметки")
        print("5. Удалить заметку")
        print("6. Показать все заметки")
        print("0. Выйти")
        try:
            choice = int(input("Выберите действие: "))
            if choice == 1:
                add_titles()
            elif choice == 2:
                update_status()
            elif choice == 3:
                check_deadline()
            elif choice == 4:
                add_notes()
            elif choice == 5:
                delete_note()
            elif choice == 6:
                if notes:
                    print("\nСписок всех заметок:")
                    for i, note in enumerate(notes, 1):
                        print(f"\n{i}. Имя: {note['Имя']}")
                        print(f"   Заголовок: {note['Заголовок']}")
                        print(f"   Описание: {note['Описание']}")
                        print(f"   Статус: {note['Статус']}")
                        print(f"   Дата создания: {note['Дата создания']}")
                        print(f"   Дедлайн: {note['Дедлайн']}")
                else:
                    print("Список заметок пуст.")
            elif choice == 0:
                print("Выход из программы. До свидания!")
                break
            else:
                print("Некорректный выбор.")
        except ValueError:
            print("Введите корректный номер действия.")

main_menu()