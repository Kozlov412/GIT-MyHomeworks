name = input("Введите имя студента: ")
grade_input = input("Введите оценку студента: ")

if grade_input.isdigit():
    grade = int(grade_input)
    if 1 <= grade <= 3:
        level = "Начальный"
    elif 4 <= grade <= 6:
        level = "Средний"
    elif 7 <= grade <= 9:
        level = "Достаточный"
    elif 10 <= grade <= 12:
        level = "Высокий"
    else:
        level = "Некорректная оценка" 
else:
    level = "Некорректная оценка" # Вывод сообщения об ошибке

print(f"Имя студента: {name}. Уровень: {level}")