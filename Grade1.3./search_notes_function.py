def search_notes(notes, keyword=None, status=None):
    """
    Функция для поиска заметок по ключевому слову и/или статусу.

    """
    # Проверка на пустой список заметок
    if not notes:
        print("Список заметок пуст.")
        return

    # Фильтрация заметок по заданным условиям
    filtered_notes = []
    for note in notes:
        # Проверка условия поиска по ключевому слову
        keyword_match = (
            keyword is None or
            keyword.lower() in note['title'].lower() or
            keyword.lower() in note['content'].lower() or
            keyword.lower() in note['username'].lower()
        )
        # Проверка условия поиска по статусу
        status_match = status is None or note['status'] == status

        # Если обе проверки пройдены, добавляем заметку в результаты
        if keyword_match and status_match:
            filtered_notes.append(note)

    # Вывод результатов
    if filtered_notes:
        print("Найдены заметки:")
        for i, note in enumerate(filtered_notes, start=1):
            print(f"\nЗаметка №{i}:")
            print(f"Имя пользователя: {note['username']}")
            print(f"Заголовок: {note['title']}")
            print(f"Описание: {note['content']}")
            print(f"Статус: {note['status']}")
    else:
        print("Заметки, соответствующие запросу, не найдены.")


# Пример использования
if __name__ == "__main__":
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
    ]

    print("1. Поиск по ключевому слову:")
    search_notes(notes, keyword='покупок')

    print("\n2. Поиск по статусу:")
    search_notes(notes, status='в процессе')

    print("\n3. Поиск по ключевому слову и статусу:")
    search_notes(notes, keyword='работы', status='выполнено')

    print("\n4. Проверка на пустой список заметок:")
    search_notes([])
