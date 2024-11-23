# Задание №1: Конвертация секунд
seconds = int(input("Введите количество секунд: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(
    f"В указанном количестве секунд ({seconds}):\nЧасов: {hours}\nМинут: {minutes}\nСекунд: {remaining_seconds}"
)

# Задание №2: Конвертация температуры
celsius = float(input("Введите температуру в градусах Цельсия: "))
kelvin = round(celsius + 273.15, 2)  # Округление с помощью round()
fahrenheit = celsius * 9 / 5 + 32
reaumur = celsius * 4 / 5
print(
    f"Температура {celsius}°C соответствует:\nКельвин: {kelvin} K\nФаренгейт: {fahrenheit:.2f}°F\nРеомюр: {reaumur:.2f}°Ré"
)
