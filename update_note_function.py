import datetime

def validate_date(date_str):

    # Проверка корректности формата даты.
    for date_format in ("%d-%m-%Y", "%d/%m/%Y"):
        try:
            datetime.datetime.strptime(date_str, date_format)
            return True
        except ValueError:
            continue
    return False

def update_note(note):

    # Обновляет выбранное поле заметки на новое значение, введённое пользователем.
    print("_______________________")
    print("Текущие данные заметки:")
    for key, value in note.items():
        print(f"{key}: {value}")

    # Список доступных для обновления полей
    fields = ["username", "title", "content", "status", "issue_date"]

    while True:
        field = input(f"\nВведите название поля для обновления ({', '.join(fields)}): ")

        if field in fields:
            if field == "issue_date":
                while True:
                    new_value = input("Введите новую дату дедлайна (в формате день-месяц-год): ")
                    if validate_date(new_value):
                        note[field] = new_value
                        break
                    else:
                        print("Некорректный формат даты. Попробуйте снова.")
            else:
                new_value = input(f"Введите новое значение для {field}: ")
                note[field] = new_value

            print("__________________")
            print("Заметка обновлена:")
            for key, value in note.items():
                print(f"{key}: {value}")
            return note
        else:
            print("Некорректное поле. Попробуйте снова.")

# Пример работы функции
if __name__ == "__main__":
    sample_note = {
        "username": "Алексей",
        "title": "Список покупок",
        "content": "Купить продукты на неделю",
        "status": "новая",
        "created_date": "27-11-2024",
        "issue_date": "30-11-2024"
    }

    update_note(sample_note)