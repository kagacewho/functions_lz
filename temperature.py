def temperature(a): #Задаем фунцию для перевода градусов Цельсия в температуру по Фаренгейту
    return (a * 1.8) + 32
t = float(input('Введите температуру в градусах Цельсия: ')) #Вводим температуру с клавиатуры
otv1 = temperature(t)
print ('По Фаренгейту будет:', otv1) #Выводим ответ