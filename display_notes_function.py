# display_notes_function.py

def display_notes(notes):
    """
    Функция отображает список заметок в структурированном формате.
    """
    if not notes:
        print("У вас нет сохранённых заметок.")
        return

    print("Список заметок:")
    print("------------------------------")

    for i, note in enumerate(notes, start=1):
        print(f"Заметка №{i}:")
        print(f"Имя пользователя: {note.get('username', 'Не указано')}")
        print(f"Заголовок: {note.get('title', 'Без заголовка')}")
        print(f"Описание: {note.get('content', 'Без описания')}")
        print(f"Статус: {note.get('status', 'Не указан')}")
        print(f"Дата создания: {note.get('created_date', 'Не указана')}")
        print(f"Дедлайн: {note.get('issue_date', 'Не указан')}")
        print("------------------------------")


# Пример вызова функции с тестовыми данными:
if __name__ == "__main__":
    # Тестовый список заметок
    test_notes = [
        {
            "username": "Алексей",
            "title": "Список покупок",
            "content": "Купить продукты на неделю",
            "status": "новая",
            "created_date": "27-11-2024",
            "issue_date": "30-11-2024",
        },
        {
            "username": "Мария",
            "title": "Учеба",
            "content": "Подготовиться к экзамену",
            "status": "в процессе",
            "created_date": "25-11-2024",
            "issue_date": "01-12-2024",
        },
    ]

    # Вызов функции отображения заметок
    display_notes(test_notes)
