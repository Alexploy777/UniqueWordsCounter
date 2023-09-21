import re

w_list = ["слово-слово", "пример-слово", "-слово", "слово-", "слово--слово", "слово"]
pattern = re.compile(r'\b[А-Яа-яЁё]*(?:-[А-Яа-яЁё]+[А-Яа-яЁё]*)*\b')

r_list = [pattern.search(w)[0] for w in w_list if pattern.search(w)]

# for w in w_list:
#     if pattern.search(w):
#         r_list.append(pattern.search(w)[0])


print(r_list)

# import re
#
# w_list = ["слово-слово", "пример-слово", "-слово", "слово-", "слово--слово", "слово"]
#
# # Функция, которая проверяет, соответствует ли слово заданным критериям
# def is_valid_word(word):
#     # Паттерн для слова: начинается с буквы, может содержать дефис, заканчивается буквой
#     pattern = re.compile(r'\b[А-Яа-яЁё]*(?:-[А-Яа-яЁё]+[А-Яа-яЁё]*)*\b')
#     return bool(pattern.match(word))
#
# # Отфильтруем список
# res_list = [word for word in w_list if is_valid_word(word)]
#
# print(res_list)





