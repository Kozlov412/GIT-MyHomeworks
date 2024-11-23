def шифр_символа(char, shift):
  """
  Шифрует один символ с помощью шифра Цезаря.
  """
  start = ord('а') if char.islower() else ord('А') if char.isupper() else ord('a') if char.islower() else ord('A')
  
  if start is not None:
    shifted_char_ord = ord(char) + shift

    end = ord('я') if start == ord('а') else ord('Я') if start == ord('А') else ord('z') if start == ord('a') else ord('Z')

    if shifted_char_ord > end:
      shifted_char_ord = start + (shifted_char_ord - end - 1)
    elif shifted_char_ord < start:
      shifted_char_ord = end - (start - shifted_char_ord - 1)

    return chr(shifted_char_ord)
  else:
    return char  # Добавляем символ без изменений, если это не буква

def caesar_cipher(text, shift):
  """
  Шифрует текст с использованием шифра Цезаря.
  """
  result = ''
  for char in text:
    if char.isspace():  # Проверка на пробел
      result += char
    elif char.isalpha():
      if 'а' <= char <= 'я' or 'А' <= char <= 'Я': # Русские буквы
        if char.islower():
          start = ord('а')
          shifted_char_ord = (ord(char) - start + shift) % 32 + start # 32 - размер русского алфавита
          shifted_char = chr(shifted_char_ord)
          result += shifted_char
        elif char.isupper():
          start = ord('А')
          shifted_char_ord = (ord(char) - start + shift) % 32 + start 
          shifted_char = chr(shifted_char_ord)
          result += shifted_char
      elif 'a' <= char <= 'z' or 'A' <= char <= 'Z': # Английские буквы
        if char.islower():
          start = ord('a')
          shifted_char_ord = (ord(char) - start + shift) % 26 + start
          shifted_char = chr(shifted_char_ord)
          result += shifted_char
        elif char.isupper():
          start = ord('A')
          shifted_char_ord = (ord(char) - start + shift) % 26 + start
          shifted_char = chr(shifted_char_ord)
          result += shifted_char
      else:
        result += шифр_символа(char, shift)
    else:
      result += char  # Добавляем символ без изменений, если это не буква
  return result

# Ввод данных
text = input("Введите текст: ")
try:
    shift = int(input("Введите сдвиг: "))
except ValueError:
    print("Ошибка: сдвиг должен быть числом.")
    exit()

# Шифрование и вывод результата
encrypted_text = caesar_cipher(text, shift)
print("Результат:", encrypted_text)