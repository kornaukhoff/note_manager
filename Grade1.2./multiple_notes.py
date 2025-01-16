from datetime import datetime

def get_valid_date(prompt):
    """
    Функция запрашивает дату у пользователя и проверяет её корректность.
    Возвращает объект datetime.date.
    """
    while True:
        date_input = input(prompt).strip()
        try:
            return datetime.strptime(date_input, '%d-%m-%Y').date()
        except ValueError:
            print("Ошибка: некорректный формат даты. Используйте формат день-месяц-год (например, 27-11-2024).")

def add_note():
    """
    Функция запрашивает данные заметки у пользователя и возвращает её в виде словаря.
    """
    name = input("Введите имя пользователя: ").strip()
    title = input("Введите заголовок заметки: ").strip()
    description = input("Введите описание заметки: ").strip()
    status = input("Введите статус заметки (новая, в процессе, выполнено): ").strip().lower()
    creation_date = get_valid_date("Введите дату создания (день-месяц-год): ")
    deadline = get_valid_date("Введите дедлайн (день-месяц-год): ")

    return {
        "Имя": name,
        "Заголовок": title,
        "Описание": description,
        "Статус": status,
        "Дата создания": creation_date.strftime('%d-%m-%Y'),
        "Дедлайн": deadline.strftime('%d-%m-%Y'),
    }

def display_notes(notes):
    """
    Функция выводит список всех заметок в формате, удобном для чтения.
    """
    if not notes:
        print("\nСписок заметок пуст.")
        return

    print("\nСписок заметок:")
    for idx, note in enumerate(notes, 1):
        print(f"\n{idx}.")
        for key, value in note.items():
            print(f"{key}: {value}")

def main():
    """
    Основная функция программы.
    """
    print("Добро пожаловать в 'Менеджер заметок'!")
    notes = []  # Список для хранения всех заметок

    while True:
        print("\nДобавьте новую заметку.")
        note = add_note()  # Создаём новую заметку
        notes.append(note)  # Сохраняем её в список

        # Предлагаем добавить ещё одну заметку или завершить
        while True:
            more_notes = input("Хотите добавить ещё одну заметку? (да/нет): ").strip().lower()
            if more_notes in ['да', 'нет']:
                break
            print("Ошибка: введите 'да' или 'нет'.")

        if more_notes == 'нет':
            break

    # Выводим все заметки
    display_notes(notes)
    print("\nСпасибо за использование 'Менеджера заметок'!")

main()