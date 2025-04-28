from abc import ABC, abstractmethod  # Імпортуємо базовий клас ABC та декоратор abstractmethod для створення абстрактних класів

# Абстрактний базовий клас
class Animal(ABC):  # Оголошення абстрактного базового класу Animal
    @abstractmethod
    def make_sound(self):  # Абстрактний метод, який потрібно реалізувати в похідних класах
        pass  # Порожня реалізація, оскільки метод абстрактний

    def sleep(self):  # Реалізований метод у базовому класі
        print(f"{self.__class__.__name__} спить...")  # Виводить повідомлення про сон тварини

# Похідний клас Dog
class Dog(Animal):  # Клас Dog успадковує базовий клас Animal
    def __init__(self, name):  # Конструктор класу Dog з параметром name
        self.__name = name  # Приватний атрибут ім'я

    def make_sound(self):  # Реалізація абстрактного методу make_sound для Dog
        print("Гав-гав!")  # Виводить звук собаки

    def get_name(self):  # Метод для отримання приватного атрибуту __name
        return self.__name

    def set_name(self, name):  # Метод для встановлення нового значення приватного атрибуту __name
        if isinstance(name, str):  # Перевіряємо, чи name є рядком
            self.__name = name

# Похідний клас Cat
class Cat(Animal):  # Клас Cat успадковує базовий клас Animal
    def __init__(self, color):  # Конструктор класу Cat з параметром color
        self.__color = color  # Приватний атрибут колір

    def make_sound(self):  # Реалізація абстрактного методу make_sound для Cat
        print("Мяу-мяу!")  # Виводить звук кота

    def get_color(self):  # Метод для отримання приватного атрибуту __color
        return self.__color

    def set_color(self, color):  # Метод для встановлення нового значення приватного атрибуту __color
        if isinstance(color, str):  # Перевіряємо, чи color є рядком
            self.__color = color

# Похідний клас Cow
class Cow(Animal):  # Клас Cow успадковує базовий клас Animal
    def __init__(self, age):  # Конструктор класу Cow з параметром age
        self.__age = age  # Приватний атрибут вік

    def make_sound(self):  # Реалізація абстрактного методу make_sound для Cow
        print("Муууу!")  # Виводить звук корови

    def get_age(self):  # Метод для отримання приватного атрибуту __age
        return self.__age

    def set_age(self, age):  # Метод для встановлення нового значення приватного атрибуту __age
        if isinstance(age, (int, float)) and age >= 0:  # Перевіряємо, що вік є числом і не від'ємний
            self.__age = age

# Приклад використання класів

dog = Dog("Бобік")  # Створення об'єкта класу Dog із ім'ям "Бобік"
cat = Cat("Рудий")  # Створення об'єкта класу Cat із кольором "Рудий"
cow = Cow(5)  # Створення об'єкта класу Cow із віком 5 років

for animal in (dog, cat, cow):  # Перебір усіх створених об'єктів у циклі
    animal.make_sound()  # Виклик методу make_sound для кожної тварини (відповідно до типу тварини)
    animal.sleep()  # Виклик методу sleep для кожної тварини (успадковано з базового класу)
