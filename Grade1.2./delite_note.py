def display_notes(notes):
    """Отображает текущий список заметок."""
    if not notes:
        print("Список заметок пуст.")
        return
    print("\nТекущие заметки:")
    for i, note in enumerate(notes, start=1):
        print(f"\nЗаметка {i}:")
        for key, value in note.items():
            print(f"  {key}: {value}")


def delete_note_by_criteria(notes, criteria, value):
    """Удаляет заметки, соответствующие критерию и значению."""
    initial_count = len(notes)
    notes[:] = [note for note in notes if note.get(criteria).lower() != value.lower()]
    deleted_count = initial_count - len(notes)
    if deleted_count > 0:
        print(f"Успешно удалено {deleted_count} заметок.")
    else:
        print(f"Заметок с таким {criteria} не найдено.")


def main():
    # Пример списка заметок
    notes = [
        {"Имя пользователя": "Алексей", "Заголовок": "Список покупок", "Описание": "Купить продукты на неделю"},
        {"Имя пользователя": "Мария", "Заголовок": "Учеба", "Описание": "Подготовиться к экзамену"},
    ]

    print("Добро пожаловать в 'Менеджер заметок'!")
    display_notes(notes)

    while True:
        if not notes:
            print("Список заметок пуст. Нечего удалять.")
            break

        # Запрашиваем критерий для удаления
        print("\nВы можете удалить заметку по имени пользователя или заголовку.")
        criteria = input("Введите критерий (имя пользователя/заголовок): ").strip().lower()

        if criteria in ["имя пользователя", "заголовок"]:
            value = input(f"Введите {criteria} для удаления заметки: ").strip()
            delete_note_by_criteria(notes, criteria.capitalize(), value)
            display_notes(notes)
        else:
            print("Ошибка: некорректный критерий. Попробуйте ещё раз.")

        # Проверяем, хочет ли пользователь продолжить
        while True:
            continue_choice = input("Хотите удалить ещё одну заметку? (да/нет): ").strip().lower()
            if continue_choice in ["да", "нет"]:
                break
            print("Ошибка ввода. Введите 'да' или 'нет'.")
        if continue_choice == "нет":
            break

    print("Работа с заметками завершена. Спасибо за использование программы!")


# Запуск программы
main()