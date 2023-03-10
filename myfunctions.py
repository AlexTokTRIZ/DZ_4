"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""
def simple_separator():
    # Функция создает красивый резделитель из 10-и звездочек (**********)
    print('*'*10)

print(simple_separator())  # True

def long_separator(count):
 #   Функция создает разделитель из звездочек число которых можно регулировать параметром count
    print('*' * count)
    return

print(long_separator(3))
print(long_separator(4))

def separator(simbol, count):
    #Функция создает разделитель из любых символов любого количества
    print(simbol * count)
    return

print(separator('-', 10))
print(separator('#', 5))

def hello_world():
#   Функция печатает Hello World в формате:
    separator('*', 10)
    print('Hello World!')
    separator('#', 10)
    return

hello_world()

def hello_who(who='World'):
    #Функция печатает приветствие в красивом формате
    separator('*', 10)
    print('Hello '+ who + '!')
    separator('#', 10)
    return

hello_who('Max')
hello_who('Kate')


def pow_many(power, *args):
    #Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    summ=0
    for i in args:
        summ+=i
    return summ**power

print(pow_many(1, 1, 2) == 3)  # True
print(pow_many(1, 2, 3) == 5)  # True
print(pow_many(2, 1, 1) == 4)  # True
print(pow_many(3, 2) == 8)  # True
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


def print_key_val(**kwargs):
    #Функция выводит переданные параметры в фиде key --> value
    for k, v in kwargs.items():
        print(str(k)+' --> '+str(v))

print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)


def my_filter(iterable, function):
    """
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    :param iterable: входаня последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    spis=[]
    for i in iterable:
        if function(i)==True:
            spis.append(i)
    return spis

# print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
# print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
# print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
# print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
