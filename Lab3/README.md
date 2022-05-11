ООП в Питоне

Л/Р 3 - __.03.22
Техническое задание на л/р:

Автоматизация работы деканата

Взять за основу файл с лекции students.csv и программу для работы с ним и класс Student.
Добавить в класс поля, всего будут там такие поля:

id|name|group|age|gender|inf|eng|math
id - id студента
name - Фамилия Имя Отчество
group - учебная группа
age - возраст
gender - пол
inf - оценка по информатике
eng - оценка по английскому
math - оценка по математике

Задачи:

        выбрать функцией filter студентов мужского пола и вывести на печать
        выбрать функцией filter студентов мужского пола призывного возаста и вывести на печать
        отсортировать всех студентов по убыванию по оценке за Информатику и вывести на печать 3-х лучших по рейтингу
        отсортировать всех студентов по среднему баллу за три дисциплины по убыванию и вывести на печать

ТЕОРИЯ

Класс - это тип данных, описывающий сложную сущность и задающий её функционал.
Класс, как и функцию, сначала нужно продекларировать - описать - и только потом использовать в программе.
На основе класса создаются объекты, которые наследуют все структурные элементы класса.
На основе одного класса в программе можно создать множество объектов и все они будут обладать сходным функционалом и могут отличаться только в хранимых значениях.
Класс структурно может состоять из конструктора класса (нужен для инициализации значений), атрибутов (это переменные) и свойств (это методы доступа к атрибутам) класса, методов класса (это функции для работы с переменными класса).

Важные понятия для ООП:

    инкапсуляция
    наследование
    полиморфизм

В Питоне реализована автоматическая сборка мусора.

В Питоне классы неявно наследую базовый класс object

В Питоне реализовано множественное наследование:

class ClassChild(ClassParent1, ClassParent2):
    def __init__(self):
        pass