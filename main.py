#Спросить у пользователя строку с овощами через запятую (например:
# "carrot, potato, onion, tomato, carrot, cucumber") и превратить её в список.
all_vegetables = input("Введите список овощей через запятую: ").split(",")
#Привести все овощи к нижнему регистру.
all_vegetables = [veg.lower() for veg in all_vegetables]
print("Список овощей в нижнем регистре:", all_vegetables)
#Посчитать, сколько всего уникальных букв встречается во всех названиях овощей (например, "carrot" даёт буквы c, a, r, o, t).
uniq_letters = set("".join(all_vegetables))
print("Количество уникальных букв во всех названиях овощей:", len(uniq_letters))
#Найти овощ с самым большим количеством букв «о» в названии.
max_o = 0
for i in all_vegetables:
    if i.count("o") > max_o:
        max_o = i.count("o")
        max_vegetables_o = i
print("Овощ с самым большим количеством букв 'o':", max_vegetables_o)
#Сделать словарь, где:
#ключ = название овоща,
#значение = количество гласных в нём.
vowels = "aeiou"
veg_dict = {}
for veg in all_vegetables:
    count = 0
    for letter in veg:
        if letter in vowels:
            count += 1
    veg_dict[veg] = count
print("Словарь, где ключ - овощ, а значение - количество гласных букв в названии овоща:", veg_dict)
#Найти овощ, в котором гласных больше всего.
max_vowels = 0
for veg, count in veg_dict.items():
    if count > max_vowels:
        max_vowels = count
        max_vowel_veg = veg
print("Овощ с наибольшим количеством гласных букв:", max_vowel_veg)
#Сформировать список овощей, длина которых больше средней длины по всем введённым овощам.
average_length = 0
full_length = 0
for i in all_vegetables:
    full_length += len(i)
average_length = full_length / len(all_vegetables)
for i in all_vegetables:
    if len(i) > average_length:
        longer_than_average = []
        longer_than_average.append(i)
print("Список овощей, длина которых больше средней длины по всем введённым овощам:", longer_than_average)
#Создать кортеж, в котором будут овощи в обратном порядке ввода.
revers_veg = tuple(reversed(all_vegetables))
print("Кортеж с овощами в обратном порядке ввода:", revers_veg)
#Проверить, встречаются ли овощи, начинающиеся на букву c или k (carrot, cucumber и т.п.). Если есть — вывести их список,
#  если нет — сообщение «Нет таких овощей».
c_k_veg = []
for i in all_vegetables:
    if i.startswith("c") or i.startswith("k"):
        c_k_veg.append(i)
if c_k_veg:
    print("Овощи, начинающиеся на букву 'c' или 'k':", c_k_veg)
else:
    print("Нет таких овощей.")
#Спросить у пользователя число N и вывести все овощи, у которых количество букв больше N.
N = int(input())
longer_N = []
for i in all_vegetables:
    if len(i) > N:
        longer_N.append(i)
print("Овощи, у которых количество букв больше", N, ":", longer_N)
 
