# Список возможных статусов
valid_statuses = ["выполнено", "в процессе", "отложено"]

# Текущий статус заметки
current_status = "в процессе"

# Показываем текущий статус
print(f"Текущий статус заметки: \"{current_status}\"\n")

while True:
    # Показываем пользователю варианты статусов
    print("Выберите новый статус заметки:")
    print("1. выполнено")
    print("2. в процессе")
    print("3. отложено")
    print("\n*Вы можете ввести номер статуса или его название.")

    # Считываем ввод пользователя
    user_input = input("\nВведите номер или название статуса: ").strip().lower()

    # Если пользователь ввёл номер
    if user_input == "1":
        current_status = "выполнено"
        break
    elif user_input == "2":
        current_status = "в процессе"
        break
    elif user_input == "3":
        current_status = "отложено"
        break
    # Если пользователь ввёл текст
    elif user_input in valid_statuses:
        current_status = user_input
        break
    else:
        print("Ошибка: Введённый статус некорректен. Попробуйте снова.\n")

# Показываем обновлённый статус
print(f"\nСтатус заметки успешно обновлён на: \"{current_status}\"")
