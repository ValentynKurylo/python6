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

class Transport:
    def __init__(self, name, price, time_road, type_in):
        self.name = name
        self.price = price
        self.time_road = time_road
        self.type_in = type_in

    def __sub__(self, other):
        return f'{self.name} is faster on {other.time_road - self.time_road} minutes than {other.name}'


class Plane(Transport):
    def __init__(self, name, price, time_road, type_in, time_register):
        Transport.__init__(self, name, price, time_road, type_in)
        self.time_register = time_register

    def time(self):
        return self.time_road + self.time_register

    def __sub__(self, other):
        time = self.time_road + self.time_register
        return f'{self.name} is faster on {other.time_road - time} minutes than {other.name}'


class Car(Transport):
    def __init__(self, name, price, time_road, type_in, km):
        Transport.__init__(self, name, price, time_road, type_in)
        self.km = km

    def price_road(self):
        return (self.km * self.price) / self.type_in

class Train(Transport):
    def information(self):
        return f'This {self.name} tickets cost - {self.price}$ type - {self.type_in} and time in road - {self.time_road} minutes'

plane = Plane('plane', 300, 300, 1, 30)
car = Car('car', 20, 360, 8, 800)
train = Train('train', 200, 1080, 'kupe')
print(plane.time())
print(car.price_road())
print(train.information())
print(plane.__sub__(train))
print(car.__sub__(train))

'''
1)Створити пустий list 
2)Створити клас Letter
3) створити змінну класу __count.
4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
5) при створені об'єкта __count має збільшуватися на 1
6) має бути метод(метод класу) для виводу __сount
7) має бути метод який записує в наш ліст текст з нашої змінної __text
'''

'''
l = []

class Letter:
    __count = 0
    def __init__(self, text):
        self.__text = text
        Letter.__count +=1

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        self.__text = new_text

    my_text = property(fget=__get_text, fset=__set_text)

    @classmethod
    def get_count(cls):
        return cls.__count

    def write(self):
        l.append(self.__text)


letter = Letter('hello')
letter.write()
letter1 = Letter('hi everybody')
letter1.write()
letter.my_text = 'hello world'
letter.write()
print(letter.my_text)
print(letter1.get_count())
print(l)
'''