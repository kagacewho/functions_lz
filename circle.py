def pl(a): #Задаем функцию для нахождения площади круга
    return a * a * 3.14
def dl(a): #Задаем функцию для нахождения длины окрыжности
    return  2 * a * 3.14
R = float(input('Введите радиус круга: ')) #Вводим радиус с клавиатуры
otv1 = pl(R)
otv2 = dl(R)
print('Площадь круга равна:', otv1) #Выводим ответ в консоль
print('Длина окружности равна:', otv2)