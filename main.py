'''
Создать класс Rectangle:
-конструктор принимает две стороны x,y
-описать арифметические методы:
  + сума площадей двух экземпляров класса
  - разница площадей
  == или площади равны
  != не равны
  >, < меньше или больше
  при вызове метода len() подсчитывать сумму сторон

'''

'''
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        a = self.x * self.y
        b = other.x * other.y
        return a + b

    def __sub__(self, other):
        a = self.x * self.y
        b = other.x * other.y
        return f'rectangle1 is big on {a - b}'

    def __eq__(self, other):
        a = self.x * self.y
        b = other.x * other.y
        if a == b:
            return 'regtangle1 == regtangle2'
        else:
            return 'regtangle1 != regtangle2'

    def __ne__(self, other):
        a = self.x * self.y
        b = other.x * other.y
        if a != b:
            return True
        else:
            return False

    def __gt__(self, other):
        a = self.x * self.y
        b = other.x * other.y
        if a > b:
            return 'regtangle1 > regtangle2'
        else:
            return 'regtangle1 <= regtangle2'

    def __len__(self):
        return (self.x + self.y)*2


rectangle1 = Rectangle(4, 8)
rectangle2 = Rectangle(3, 5)
print(rectangle1+rectangle2)
print(rectangle1-rectangle2)
print(rectangle1==rectangle2)
print(rectangle1!=rectangle2)
print(rectangle1>rectangle2)
print(len(rectangle2))
'''

'''
1) написати програму для запису відомостей про пасажирські перевезення
2) перевезення відбувається трьома способами, літаком, машиною, поїздом,
3) дані які треба буде зберігати:
  - вартість квитка(літак, поїзд)
  - кількість пасажирів(машина)
  - час в дорозі(всі)
  - час реєстрації(літак)
  - клас:перший,другий(літак)
  - вартість пального(машина)
  - км(машина)
  - місце: купе,св(поїзд)
4) методи:
  - розрахунок вартості доїзду(машина)
  - загальний час перельоту(літак)
  - порівняти час в дорозі між двома будь якими транспортними засобами(двома об'єктами) - наприклад"літак на 5 годин швидше за поїзд"
  - вивести всі дані про перевезення(поїзд)
'''

'''
class Plane:
    def __init__(self, price, time_road, time_register, type_place):
        self.price = price
        self.time_road = time_road
        self.time_register = time_register
        self.type_place = type_place

    def time(self):
        return f'{self.time_road + self.time_register} хв'

    def __sub__(self, other):
        time = self.time_road + self.time_register
        return f'літак на {other.time_road - time} хвилин швидше за поїзд'

class Car:
    def __init__(self, number, time_road, price_gas, km ):
        self.number = number
        self.time_road = time_road
        self.price_gas = price_gas
        self.km = km

    def price(self):
        return ((self.km / (self.time_road / 6)) * self.price_gas)/self.number

class Train:
    def __init__(self, price_ticket, time_road, type_place):
        self.price_ticket = price_ticket
        self.time_road = time_road
        self.type_place = type_place

    def information(self):
        return f'price ticket - {self.price_ticket}, time in road - {self.time_road}, type of place - {self.type_place}'


plane = Plane(100, 180, 60, 1)
car = Car(5, 720, 20, 2400)
train = Train(50, 1080, 'kupe')

print(plane.time())
print(car.price())
print(train.information())
print(plane-car)
'''

'''
1)Створити пустий list 
2)Створити клас Letter
3) створити змінну класу __count.
4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
5) при створені об'єкта __count має збільшуватися на 1
6) має бути метод(метод класу) для виводу __сount
7) має бути метод який записує в наш ліст текст з нашої змінної __text
'''
l = []

class Letter:
    __count = 0
    def __init__(self, text):
        self.__text = text
        Letter.__count +=1

    def get_text(self):
        return self.__text

    def set_text(self, new_text):
        self.__text = new_text

    @classmethod
    def get_count(cls):
        return cls.__count

    def write(self):
        l.append(self.__text)


letter = Letter('hello')
letter.write()
letter1 = Letter('hi everybody')
letter1.write()
letter.set_text('hello world')
letter.write()
print(letter.get_text())
print(letter1.get_count())
print(l)
