from cities import cities_list

def get_city_key(cities_list):
    """Определяет ключ для названия города."""
    if cities_list:
        first_city = cities_list[0]
        if 'city' in first_city:
            return 'city'
        elif 'name' in first_city:
            return 'name'
    return None

def prepare_cities(cities_list):
    """Подготавливает города для игры, удаляя "плохие буквы"."""
    city_key = get_city_key(cities_list)
    if not city_key:
        raise ValueError("Не найден ключ для названия города в cities.py")

    cities_set = set()
    for city_data in cities_list:
        cities_set.add(city_data[city_key].upper())

    bad_letters = set()
    good_first_letters = set()
    first_letter_counts = {}

    for city in cities_set:
        good_first_letters.add(city[0])
        first_letter_counts[city[0]] = first_letter_counts.get(city[0], 0) + 1

    for city in cities_set:
        if city[-1] not in good_first_letters and first_letter_counts[city[0]] > 1:
            bad_letters.add(city[-1])

    filtered_cities = set()
    for city in cities_set:
        if city[-1] not in bad_letters:
            filtered_cities.add(city)

    return filtered_cities, bad_letters

def get_next_city(last_letter, cities):
    """Находит следующий город, начинающийся на заданную букву."""
    for city in sorted(list(cities)): # Сортируем, чтобы выбор был детерминированным.
      if city.startswith(last_letter):
          cities.remove(city)
          return city
    return None


def is_valid_city(city_name, cities):
    """Проверяет, есть ли город в множестве городов."""
    return city_name.upper() in cities


def play_cities(cities_set, bad_letters):
    """Основная функция игры с учетом "плохих букв"."""

    used_cities = set()
    last_letter = None
    current_player = "user"

    while True:
        print(f"Ход игрока: {current_player}")

        if current_player == "user":
            city_name = input("Введите название города (или 'стоп'): ").strip()

            if city_name.lower() == "стоп":
                print("Вы проиграли! Компьютер победил!")
                return

            if not is_valid_city(city_name, cities_set) or city_name.upper() in used_cities:
                print("Такой город не существует или уже был использован. Вы проиграли! Компьютер победил!")
                return

            used_cities.add(city_name.upper())
            last_letter = city_name[-1].upper()

            if last_letter in bad_letters:
                print(f"Буква '{last_letter}' является 'плохой'. Город не подходит. Попробуйте другой город.")
                current_player = "user" # Ход остается у пользователя
                continue


        else: # Ход компьютера
            computer_city = get_next_city(last_letter, cities_set)

            if computer_city is None:
                print(f"Компьютер не смог найти город на букву '{last_letter}'. Вы победили!")
                return

            print(f"Компьютер выбрал город: {computer_city}")
            used_cities.add(computer_city)
            last_letter = computer_city[-1].upper()

        current_player = "computer" if current_player == "user" else "user"



if __name__ == "__main__":
    cities_set, bad_letters = prepare_cities(cities_list)

    if not cities_set:
        print("Ошибка: после удаления городов с 'плохими буквами' не осталось городов для игры.")
    else:
        play_cities(cities_set, bad_letters)
