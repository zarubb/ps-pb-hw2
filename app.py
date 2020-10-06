# вводные данные по account
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

# вводные данные по user
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

# вводные данные по списку user
user_list = [user1, user2, user3, user4]

key_input = input('Введите ключ (name или account): ')  # запрашиваем имя ключа
key = key_input.lower()  # переводим в нижний регистр, чтобы исключить неверный ввод

# через try/except исключаем ошибку на ввод несуществующего ключа в словарях user*
# через цикл for проверяем все элементы списка user_list на налиие соответствующего ключа и выводим его значение
try:
    circle_i = 1
    for i in user_list:
        print(f'значение ключа для user{circle_i} = {i[key]}')
        circle_i +=1
except KeyError:
    print('Введенный ключ не найден')
    
print(' ') # пропускаю одну строку, чтобы в терминале смотрелось понятней

user_number = input('Введите порядковый номер: ') # запрашиваем номер пользователя

# через try/except исключаем ошибку на ввод несуществующего номера user*
# далее, опрашивая требуемые ключи, выводим их значение
try:
     user_list[(int(user_number)-1)] # проверка для try/except
     print(f'Данные по user{user_number}:')
     print(f'имя: {user_list[(int(user_number)-1)]["name"]}')
     print(f'возраст: {user_list[(int(user_number)-1)]["age"]}')
     print(f"логин: {user_list[(int(user_number)-1)]['account']['login']}")
     print(f"пароль: {user_list[(int(user_number)-1)]['account']['password']}")     
except IndexError:
    print('Пользователь с указанным номером не найден')

print(' ') # пропускаю одну строку, чтобы в терминале смотрелось понятней

# запрашиваем номер пользователя, для переноса в конец
user_move = input('Введите номер пользователя для переноса в конец списка: ') 

# через try/except исключаем ошибку на ввод несуществующего номера user*
try:
    user_list[(int(user_move)-1)] # проверка для try/except
    print('Список до изменения') # выводим список до изменения
    print(user_list)
    print(' ') # пропускаю одну строку, чтобы в терминале смотрелось понятней
    # указываем пользователя для перемещения
    print(f'Пользователь с именем {user_list[(int(user_move)-1)]["name"]} перемещен в конец списка')
    print(' ') # пропускаю одну строку, чтобы в терминале смотрелось понятней
    user_to_end = user_list.pop((int(user_move)-1)) # удаляем указанного пользователя из списка и записываем в переменную
    user_list.append(user_to_end) # добавляем удаленного пользователя в конец списка
    print('Список после изменения') # выводим список после изменения
    print(user_list)
    print(' ') # пропускаю одну строку, чтобы в терминале смотрелось понятней
except IndexError:
    print('Пользователь с указанным номером не найден')

# расчет среднего возраста
middle_age = 0 # вводим переменную "средний возраст", равную 0
for j in user_list: # через цикл for суммируем в данную переменную значения ключа "возраст" у всех user*
    middle_age += int(j['age'])
# выводим значение среднего возраста методом деления получившегося значения переменной "средний возраст" на длину списка
# длина списка user_list равна количеству пользователей
print(f'Средний взраст пользователей: {middle_age/len(user_list)}') 
