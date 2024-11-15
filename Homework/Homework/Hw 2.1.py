# Задача номер 1
word = input()  # чтобы можно было вписать любое слово

wordLength = len(word)  # определяем длину слова
if wordLength % 2 == 0:  # проверка на четность\нечетность
    wordMidIndex = wordLength // 2
    result = word[wordMidIndex - 1:wordMidIndex + 1]  # условие при четности
else:
    wordMidIndex = wordLength // 2
    result = word[wordMidIndex]  # условие при нечетности
print(result)


# Задача номер 2
men = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
women = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(men) != len(women):  # проверяем, одинаковой ли длины списки
    print("Внимание, кто-то может остаться без пары!")
else:
    menSorted = sorted(men)  # Сортировка списков
    womenSorted = sorted(women)
    print("Идеальные пары:")
    # перебор и объединение списков в кортеж
    for men, women in zip(menSorted, womenSorted):
        print(f"{men} и {women}")  # вывод форматированной строки
