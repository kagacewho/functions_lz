def chas(a): #Задаем функцию для перевода в секунды
    return (int(a[0])*60*60 + int(a[1])*60 + int(a[2]))
vremya = input('Введите время в формате x-x-x ')
vremya = vremya.split('-') #Разделяем при помощи команды split и -
print('Всего секунд:', chas(vremya) ) #Выводим в консоль