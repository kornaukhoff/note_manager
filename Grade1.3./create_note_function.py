import datetime


def create_note():
    """
    Функция для создания новой заметки.
    Возвращает словарь с данными заметки.
    """
    # Запрашиваем данные у пользователя
    username = input("Введите имя пользователя: ").strip()
    title = input("Введите заголовок заметки: ").strip()
    content = input("Введите описание заметки: ").strip()

    # Запрос и проверка статуса
    status = input("Введите статус заметки (новая, в процессе, выполнено): ").strip().lower()
    while status not in {"новая", "в процессе", "выполнено"}:
        print("Некорректный статус. Введите 'новая', 'в процессе' или 'выполнено'.")
        status = input("Введите статус заметки (новая, в процессе, выполнено): ").strip().lower()

    # Автоматическое добавление текущей даты
    created_date = datetime.date.today().strftime("%d-%m-%Y")

    # Запрос и проверка даты дедлайна
    while True:
        issue_date = input("Введите дату дедлайна (в формате день-месяц-год): ").strip()
        try:
            datetime.datetime.strptime(issue_date, "%d-%m-%Y")
            break
        except ValueError:
            try:
                datetime.datetime.strptime(issue_date, "%d/%m/%Y")
                break
            except ValueError:
                print("Некорректный формат даты. Попробуйте снова.")

    # Формирование словаря заметки
    note = {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date,
    }
    return note

# Демонстрация работы функции

new_note = create_note()
print("\nЗаметка создана:")
print(new_note)