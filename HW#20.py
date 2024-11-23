small_dict = {
    'Человек-муравей и Оса: Квантомания': 2023,
    'Стражи Галактики. Часть 3': 2023,
    'Капитан Марвел 2': 2023,
    'Дэдпул 3': 2024,
    'Капитан Америка: Дивный новый мир': 2024,
    'Громовержцы': 2024,
    'Блэйд': 2025,
    'Фантастическая четвёрка': 2025,
    'Мстители: Династия Канга': 2026,
    'Мстители: Секретные войны': 2027,
    'Безымянный фильм о Человеке-пауке': None,
    'Безымянный фильм о Шан-Чи': None,
    'Безымянный фильм о Вечных': None,
    'Безымянный фильм о мутантах': None
}

def search_movies_by_name(movies_dict):
    """
    Ищет фильмы в словаре по заданному названию или части названия.

    Args:
        movies_dict: Словарь с фильмами, где ключ - название фильма, 
                     а значение - год выхода.

    Returns:
        None
    """
    search_term = input("Введите название фильма или его часть: ")
    found_movies = []
    for movie_name in movies_dict:
        if search_term.lower() in movie_name.lower():
            found_movies.append(movie_name)
    
    if found_movies:
        print("Найденные фильмы:")
        for movie in found_movies:
            print(movie)
    else:
        print("Фильмов с таким названием не найдено.")


def filter_movies_by_year(movies_dict):
    """
    Фильтрация фильмов по году выхода, исключая фильмы с неизвестным годом.

    Args:
        movies_dict: Словарь с фильмами, где ключ - название фильма, 
                     а значение - год выхода.

    Returns:
        None
    """
    filtered_movies = {}
    for movie_name, year in movies_dict.items():
        if year is None:
            continue 
        if year > 2024:
            filtered_movies[movie_name] = year

    if filtered_movies:
        print("Фильмы, вышедшие после 2024 года:")
        print(filtered_movies)

    print("\nФильмы, вышедшие после 2024 года (список):")
    for movie_name, year in filtered_movies.items():
        print(movie_name)

    print("\nФильмы, вышедшие после 2024 года (список словарей):")
    filtered_list = [{'Название': movie_name, 'Год': year} for movie_name, year in filtered_movies.items()]
    print(filtered_list)

if __name__ == "__main__":
    search_movies_by_name(small_dict)
    print("-" * 40)
    filter_movies_by_year(small_dict)