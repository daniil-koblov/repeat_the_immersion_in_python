# Данный репозиторий включает в себя повторение курса "Погружение в Python" по программе

# Обучения "Разработчик — Веб-разработка на Python. Технологическая специализация"

# образовательной платформы "GeekBrains".

## Урок 1. Основы Python.
 
## [Первая лекция](lectures/lecture_1)

### Создание виртуального окружения

* Подготовка к созданию окружения:
  - mkdir new_project
  - cd new_project

* Создание окружения
  - python -m venv venv — для Windows;
  - python3 -m venv venv — для Linux и MacOS.

* Активация окружения
  - venv\Scripts\activate — для Windows;
  - source venv/bin/activate — для Linux и MacOS.

* Выход из окружения
  - deactivate

### Работа с pip

Package Installer for Python — система управления
пакетами, которая используется для установки
и управления программными пакетами,
написанными на Python.

  - pip install requests
  - pip freeze
  - pip freeze > requirements.txt
  - more requirements.txt
  - pip install -r requirements.txt

*requirements.txt* - файл, в котором сохраняется
перечень всех необходимых дополнений для вашего
проекта.

### Работа с python в режиме интерпретатора.

  - Активация
    - *python* - для Windows
    - *python3* - для Linux, MacOC

  - Выход из режима
    - exit() 
  
### Арифметические операторы в Python.

![Таблица_арифметических_операторов_в_python](/images/images_from_lectures/lecture_1_1.png)

*_* - возврат результата последней операции.

### PEP-8

#### Переменные и требования к именам

- Что ещё нужно знать когда речь идёт о переменных и их именах:
  - Python использует кодировку utf-8. Поэтому в качестве имени переменной
  может выступать любой набор символов, даже смайлик. Однако правильные
  имена это имена на латинице, т.е. английские строчные буквы, слова.
  Например, *name*, *age*.
  - Если название переменной состоит из нескольких слов такие слова
  записываются строчными буквами и разделяются символом подчёркивания.
  Этот стиль называется *snake_case*.
  - В качестве первого символа в имени переменной запрещено использовать
  цифры и другие знаки пунктуации в этом случае Python выдаст ошибку. Имя
  начинается с буквы или символа подчёркивания.
  - Не используйте написание слов на транслите. Воспользуйтесь онлайн
  переводчиком на английский. Не *zdorove*, а *health*.

![Требования_к_именам_переменных](/images/images_from_lectures/lecture_1_2.png)

### Константы

Константа - переменная в программе, которая 

Примеры констант:

- MAX_COUNT = 1000
- ZERO = 0
- DATA_AFTER_DELETE = 'No data'
- DAY = 60 * 60 * 24

#### Встроенные константы *True* (Истина) *False* (Ложь) *None* (Ничего).

 - *True* и *False* это булевы значение (type boolean). 
    Являются результатом логических операций

 - *None* используется для объявления переменной при её необходимости, 
    но отсутствии каких либо данных о ней.

### [Функция id()](lectures/lecture_1/venv/task_1.py)

1) id() - возвращает адрес объекта в опер. памяти компьютера.

2) print() - выводит информацию в консоль.

В здании первая функция (id()) возвращает адрес о переменной в опер. памяти. 
И далее вторая функция (print()) выводит информацию в консоль.

### Зарезервированные слова, keyword.kwlist

База синтаксиса Python содержит около 40 зарезервированных слов:

False, None, True, and, as, assert, async, await, break, class,
continue, def, del, elif, else, except, finally, for, from,
global, if, import, in, is, lambda, nonlocal, not, or, pass,
raise, return, try, while, with, yield.

Также с версии 3.10 языка добавили:

case и match

### Ввод и вывод данных

- print() - функция, выводящая инфо в консоль.

- input() - функция, запрашивающая ввод данных. Ввод всегда преобразуется в
  строку (type str). 
  При необходимости можно перевести: 
  - В целочисленный тип -> int(input())
  - Или в вещественный тип, число с плавающей запятой -> float(input())
  
### Магические числа

Использование чисел вне переменных может усложнить чтение кода.

Пример с кодом на проверку возраста:

- [Неправильный вариант](lectures/lecture_1/venv/task_2.py), 
где число 18 может быть интуитивно понятно. 
При этом в крупных проектах, которые исчисляются сотнями или тысячами строк,
такое число может создать проблемы с решением задач.

- [Правильный вариант](lectures/lecture_1/venv/task_3.py), 
в котором удобно будет найти истоки вычислений.

### Ветвление

Такие операции полезны при необходимости выполнения определенных 
команд при соблюдении или не соблюдении некоторых условий.

Условие при этом возвращает булево значение истину или ложь.
Любое число это истина, кроме нуля. Ноль это ложь.
При этом явное преобразование лучше неявного.

#### Если, if

[Проверка условия](lectures/lecture_1/venv/task_4.py) происходит с помощью 
зарезервированного слова if.

В 3 строке с if используется оператор сравнения.

Список операторов сравнения:
- *==* - равно 
- *!=* - не равно
- *>* - больше
- *>=* - больше или равно
- *<* - меньше
- *<=* - меньше или равно

#### Отступы вместо фигурных скобок {}.

Python не требует заключать массивы кода в фигурные скобки {}, но при этом для
корректной работы необходимо соблюдать отступы для корректности работы программы.

Ветвления (if, else, match, case), циклы (while, for in), функции (def), классы (class) 
и другие сущности языка, требующие вложения кода, должны быть написаны с отступами
в 4 пробела* (нажатие на кнопку *Tab* по умолчанию создает такую возможность).

[Соблюдение отступов](lectures/lecture_1/venv/task_4.py) повышает вероятность 
корректной отработки программы и читабельность написанного кода.

Строки 3 это условие. 
4 и 5 строки с отступами для выполнения кода строго при соблюдении 
условия 3 строки.
6 строка работает вне зависимости от выполнения условия 3 строки.

_*PEP-8 требует 4 пробела для отступа, но синтаксис языка 
для корректной работы программы позволяет отступы в 2 и 8 пробелов. При этом 
программа проверки на соблюдение PEP-8 будет выдавать предупреждение о не соблюдении
условий._

Для обозначения логического выражения в условии ветвления синтаксис Python не требует 
заключения его в скобки по сравнению с другими языками. Например, Java.

#### Иначе, Else

Для ложности выполнения условия if используется 
[зарезервированное слово else](lectures/lecture_1/venv/task_5.py).

[Else относится к тому if](lectures/lecture_1/venv/task_6.py), 
который с ним на одном уровне.

#### Если еще, elif (в Java, например, используется else if)

При наличии дополнительного/-ых равнозначного/-ых условия/-ий (или одно, 
или другое) используется 
[зарезервированное слово elif](lectures/lecture_1/venv/task_7.py).

Проверка условий проходит до первого совпадения. Остальные проверки 
равнозначных условия после первого истинного результата пропускаются.
При отсутствии истинных результатов в каждом условии выполняется код
после else*, при его наличии.

_*Ветвления if elif else допускают отсутствие использования else если оно не нужно._

#### Выбор вариантов match case

С версии Python 3.10 появились множественные сравнения. Это конструкция match case.
После match указывается переменная для сравнения.

[Пример](lectures/lecture_1/venv/task_8.py)

В данном коде альтернативный вариант примера elif. Отличие заключается 
в множественном условии для каждого логического условия. К красному цвету добавлен
оранжевый, вывод результата в консоль идентичен. При этом не дополнительных строк
кода как это было бы с вариантом if elif. В примере match case 
вертикальная черта *|* играет роль оператора *или*. Пользователь при этом
водит также один цвет.

В конструкции case играет роль как if/elif, так и else. 
При этом если case с условием, то он схож больше с if или elif. 
А при отсутствии условия после надо прописывать сочетание case _ и в таком
случае он играет роль else.

#### Логические конcтрукции or, and, not.

Синтаксис языка предполагает 3 логических оператора:
- and - логическое умножение *И*
- or - логическое сложение *ИЛИ*
- not - логическое отрицание *НЕ*

#### Логика их работы:

- first *True* second *True*
  - first and second -> *True*
  - first or second -> *True*
  

- first *False* second *True*
  - first and second -> *False*
  - first or second -> *True*


- first *True* second *False*
  - first and second -> *False*
  - first or second -> *True*


- first *False* second *False*
  - first and second -> *False*
  - first or second -> *False*

[Пример кода](lectures/lecture_1/venv/task_9.py) 
без использования логических операторов.

[Пример кода](lectures/lecture_1/venv/task_10.py)
с использованием логических операторов, благодаря которым уменьшается код.

#### Ленивый if 

[В примере прошлого кода](lectures/lecture_1/venv/task_10.py) во второй строке
использовался ленивый *if*. 

Он по порядку слева на право проверяет все условия.
При наличии оператора *or* если первое выражение (оно находится слева от *or*) 
выдает значение *True*, то проверка условия *if* 
останавливается и возвращается *True*.
При наличии оператора *and* если первое выражение выдает значение *False*, то
проверка условия *if* останавливается и возвращается *False*.

В данном условии ленивого if, для получения результата в виде 
високосного года нужно:
1) Получить значение *False* в первом выражении (year % 4 != 0) т.к. из-за 
оператора *or* программа продолжит проверять следующие за первым выражения.
2) Получить значение *True* во втором выражении (year % 100 == 0) т.к. из-за
оператора *and* программа также продолжит проверять следующие 
уже за вторым выражения.
3) В последнем выражении (year % 400 != 0) также нужно получить значение *True*
и тогда получится, что if выдает *False* по причине результата 
*False* or *True* and *True* и тогда результат if не будет выводится и тогда 
программа сразу перейдет к результату else.

#### Проверка вхождения in.

Оператор in проверяет вхождение эл-та в последовательность.

[Пример](lectures/lecture_1/venv/task_11.py) проверки вхождения оператором *in*.

[Пример](lectures/lecture_1/venv/task_12.py) проверки отсутствия вхождения 
оператором *not in*.  

#### Тернарный оператор

Тернарный оператор позволяет записать несколько логических строк в одну.

[Пример](lectures/lecture_1/venv/task_13.py) обычного ветвления.

[Пример](lectures/lecture_1/venv/task_14.py) ветвления с тернарным оператором.

Второй пример значительно короче первого за счет этого проще.
В нем один раз используется функция print(), так как в первом два раза.
Сначала прописывается результата истины, потом *if* и условие, далее else 
и результат для лжи условия if.

*В тернарном операторе не допускается отсутствие else. 
А также слишком длинные строки тернарного оператора теряют удобство в чтении кода.*

### Циклы

#### Цикл While

Цикл выполняется пока результат логического выражения условия этого цикла *True*. 
При получении *False* цикл завершается.

[Пример](lectures/lecture_1/venv/task_15.py), 
перебора четных чисел до введенного пользователем.

*При прибавлении к счетчику вместо: __count = count + 2__  
можно использовать: __count += 2__. Также можно 
и с прибавлением к переменной других чисел.*

#### Возврат в начало цикла, continue

Оператор *continue* необходимо для досрочного перехода в начало цикла. 
В [данном примере](lectures/lecture_1/venv/task_16.py) цикл возвращается 
в начало при кратности числа двенадцати 
и вывод этого числа в консоль не происходит.

Добавили константу *STEP* (count += STEP), которая увеличивает *count*, 
вместо магического числа (count += 2).

Ввели переменную limit. Чтобы цикл не выводил лишние числа, больше
введенного num, на каждой проверке цикла while надо вычитать значение
шага. Но шаг — константа. Для экономии ресурсов ПК и ускорения работы
кода логично сделать вычитание один раз перед циклом и сравнивать
значения быстрее, без вычитания в строке while



#### Досрочное завершение цикла, break

Ещё один способ управления циклом — команда break для его досрочного
завершения. Она отлично подходит для создания циклов с постусловием,
бесконечных циклов с возможностью выхода.
[Пример программы](lectures/lecture_1/venv/task_17.py), 
которая просит ввести число внутри заданного диапазона.

Конструкция *while True* создает бесконечный цикл. Добавлено для примера.

#### Действие после цикла, else

В цикле *while* можно также использовать *else* относительно цикла.

*else* должен быть на уровне с необходимым *while*.

Теперь, в измененном [примере](lectures/lecture_1/venv/task_18.py):
- Добавили счётчик *count*. Он в цикле ограничивает кол-во попыток ввода числа.
- Добавили *else* внутрь цикла *while*. Если *if*, проверяющий 
неверность введенного числа, выдает *False*, то программа переходит к *else* 
и завершает цикл.
- После *else* выводится сообщение об исчерпании попыток и для
завершения работы с файлом вводится функция *quit()*.

#### Цикл итератор for in

Этот цикл отличается от *while* ограничением кол-ва итераций цикла.
Цикл *while* работает пока его условие не станет ложным,
а *for in* заканчивает работу как только закончится отсчет кол-ва итераций.

Например, [перебор значений из массива](lectures/lecture_1/venv/task_19.py).
Цикл последовательно перебирает значения массива *data* и поочередно помещает
их в переменную *item*.

Т.е. при написании условия цикла указывается сначала *for*. 
Далее переменная, которая будет изменяться после каждой итерации цикла.
После *in*.
Затем указывается итерируемый объект, например, range() 
или как в примере массив.

*Нельзя изменять массив, который является итерируемым объектом условия 
во время итерации цикла. Это может привести к ошибкам.*

#### Функция арифметического цикла, range()

Вместо отдельного объявления массива из некоторого кол-ва целых чисел
для итерации цикла, проще указать в условии цикла функцию range().

В [примере](lectures/lecture_1/venv/task_20.py) указаны два цикла, которые
выводят четные числа. 
Первый вариант статичен из-за неизменяемости массива. Для изменения результата
надо или менять код переменной, или вводить отдельный цикл для изменения массива,
или изменять основной цикл.

Второй вариант по кол-ву строк не отличается от первого, 
но при этом он динамичен благодаря функции range(). Наличие массива не нужно.
Перебор начинается с первого четного числа *2*, заканчивается на втором *num*. 
Третье число указывает на шаг перебора значений. 
В данном случае 2 т.к. нужны числа кратные двум т.е. четные. 
За счет этого результат изменяем без коррекции кода.

Также если шаг будет отрицательным, то перебор будет на уменьшение чисел. Т.о.
можно произвести обратный отсчет.
Если стартовое число больше финишного при положительном шаге или наоборот,
стартовое число меньше финишного при отрицательном шаге, то цикл не запустится
т.к. условие уже выполнено.

#### Имена переменных в цикле.

Принято брать имена переменных в цикле в порядке *i*, *j*, *k*.
Т.е. цикл будет иметь вложенный цикл, то сначала берется *i*, потом *j*, а
затем *k*. [Пример](lectures/lecture_1/venv/task_21.py) тройного 
вложенного цикла.

На равнозначные циклы это не распространяется.

Также при переборе данных из массива лучше дать имя перменной как имя массива
в единственном числе. [Пример](lectures/lecture_1/venv/task_22.py) перебора имен
животных в массиве.

#### Функция с нумерацией элементов, enumerate()

Данная функция позволяет добавить порядковый номер к элементам итерируемой 
последовательности.

[Измененный пример](lectures/lecture_1/venv/task_23.py) перебора имен животных 
в массиве.

Список изменений:
1) В условии цикла теперь две переменных вместо одной. 
   - В переменную *i* сохраняется порядковый номер.
   - В переменную *animal* сохраняется очередное значение из массива *animals*.
2) Добавили в качестве итерируемого объекта функцию enumerate()
   - В аргументе *animals* список животных.
   - Во второй поставили стартовую переменную в виде *start = 1*, чтобы 
   порядковые номера значений не начинались с нуля. Это бы произошло 
   при отсутствии второй переменной в функции.

*Функция enumerate() может перебирать только целые (int) числа 
и только с шагом в единицу.* 

## [Первый семинар](seminars\seminar_1)

### [Задание 4](seminars/seminar_1/task_4.py):

  - [x] Работа в консоли в режиме интерпретатора Python.
  - [x] Решите квадратное уравнение:
      - 5x<sup>2</sup>-10x-400=0
      - Надо также последовательно сохранять переменные a, b, c, d, x1 и x2.
  - [x] *Попробуйте решить уравнения с другими значениями a, b, c.


### [Задание 5](seminars/seminar_1/task_5.py):

  - [x] Работа в консоли в режиме интерпретатора Python.
  - [x] Посчитайте сумму чётных элементов от 1 до *n*, исключая кратные *e*.
  - [x] Используйте *while* и *if*.
  - [x] Попробуйте разные значения *e* и *n*.

### [Задание 6](seminars/seminar_1/task_6.py):

  - [x] Напишите программу, которая запрашивает год и проверяет его 
        на високосность.
  - [x] Распишите все возможные проверки в цепочке *elif*
  - [x] Откажитесь от магических чисел
  - [x] Обязательно учтите год ввода Григорианского календаря
  - [x] В коде должны быть один *input* и один *print*.

#### [Задание 7](seminars/seminar_1/task_7.py):

  - [x] Пользователь вводит число от 1 до 999. Используя операции с числами
  сообщите что введено: цифра, двузначное число или трёхзначное число.
  - [x] Для цифры верните её квадрат, например 5 - 25
  - [x] Для двузначного числа произведение цифр, например 30 - 0
  - [x] Для трёхзначного числа его зеркальное отображение, например 520 - 25
  - [x] Если число не из диапазона, запросите новое число.
        Откажитесь от магических чисел
  - [x] В коде должны быть один *input* и один *print*

#### [Задание 8](seminars/seminar_1/task_8.py):

  - [x] Нарисовать в консоли ёлку спросив
  у пользователя количество рядов.

  - Пример результата:

    Сколько рядов у ёлки? Ответ: 5.

  ![Семинар_1_задание_8](/images/images_from_seminars/seminar_1_task_8.png)

#### [Задание 9](seminars/seminar_1/task_9.py):

  - [x] Выведите в консоль таблицу умножения от 2х2 до 9х10 
  как на школьной тетрадке.

  ![Семинар_1_задание_9](/images/images_from_seminars/seminar_1_task_9.png)

## [Первое практическое задание](homeworks\homework_1)

### [Задание 1](homeworks/homework_1/task_1.py):
  Напишите программу, которая рисует прямоугольную рамку с помощью
  символьной графики. 
  - Для вертикальных линий используйте символ
    вертикального штриха '|', а для горизонтальных — дефис '-'. 
  - Пусть ширину и высоту рамки определяет пользователь.
    
  Пример: 
  
  ![Домашняя_Работа_1_задание_1](/images/images_from_homework/homework_1_task_1.png)

### [Задание 2](homeworks/homework_1/task_2.py):
  Треугольник существует только тогда, когда сумма любых двух его сторон
  больше третьей. 
  - Дано a, b, c - стороны предполагаемого треугольника.
  - Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
  - Если хотя бы в одном случае отрезок окажется больше суммы двух других, то
  треугольника с такими сторонами не существует. 
  - Отдельно сообщить является ли треугольник разносторонним, равнобедренным 
  или равносторонним.

### [Задание 3](homeworks/homework_1/task_3.py):
  Напишите программу, которая считает количество простых чисел в заданной
  последовательности и выводит ответ на экран.

*! Простое число делится только на себя и на единицу.*

  *! Простое числа только натуральные. Т.е. они не могут быть отрицательными.*

  *! Последовательность задаётся при помощи вызова ввода (input) 
  на каждой итерации цикла.* 

  *! Одна итерация — одно число.*
  
  Пример:

  - Введите количество чисел: 6.
  - Введите число: 4. 
  - Введите число: 7. 
  - Введите число: 20. 
  - Введите число: 3. 
  - Введите число: 11. 
  - Введите число: 37.


  - Количество простых чисел в последовательности: 4.

### [Задание 4](homeworks/homework_1/task_4.py):
  - Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. 
  - Вам поручили создать генератор ландшафта. 
  - Напишите программу, которая получает на вход число N и 
  выводит на экран числа в виде ямы:

  ![Домашняя_Работа_1_задание_4](/images/images_from_homework/homework_1_task_4.png)  

### [Задание 5](homeworks/homework_1/task_5.py):
  - Мальчик загадывает число между 1 и 100 (включительно). 
  - Компьютер может спросить у мальчика:

  «Твоё число равно, меньше или больше, чем число N?»,
  - N — число, которое хочет проверить компьютер. 
  - Мальчик отвечает одним из трёх чисел: 1 — равно, 2 — больше, 3 — меньше. 
  - Напишите программу, которая с помощью цепочки таких вопросов и ответов
  мальчика угадывает число. 
  - Дополнительно: сделайте так, чтобы можно было гарантированно угадать
  число за семь попыток.

## Урок 2.

### [Вторая лекция](lectures\lecture_2)

### [Второй семинар](seminars\seminar_2)

### [Второе практическое задание](homeworks\homework_2)

## Урок 3.

### [Третья лекция](lectures\lecture_3)*

### [Третий семинар](seminars\seminar_3)*

### [Третье практическое задание](homeworks\homework_3)*

## Урок 4.

### [Четвертая лекция](lectures\lecture_4)

### [Четвертый семинар](seminars\seminar_4)
 
### [Четвертое практическое задание](homeworks\homework_4)

## Урок 5.

### [Пятая лекция](lectures\lecture_5)

### [Пятый семинар](seminars\seminar_5)

### [Пятое практическое задание](homeworks\homework_5)

## Урок 6.

### [Шестая лекция](lectures\lecture_6)

### [Шестой семинар](seminars\seminar_6)

### [Шестое практическое задание](homeworks\homework_6)

## Урок 7.

### [Седьмая лекция](lectures\lecture_7)

### [Седьмой семинар](seminars\seminar_7)

### [Седьмое практическое задание](homeworks\homework_7)

## Урок 8.
 
### [Восьмая лекция](lectures\lecture_8)
 
### [Восьмой семинар](seminars\seminar_8)

### [Восьмое практическое задание](homeworks\homework_8)

## Урок 9.

### [Девятая лекция](lectures\lecture_9)

### [Девятый семинар](seminars\seminar_9)

### [Девятое практическое задание](homeworks\homework_9)

## Урок 10.

### [Десятая лекция](lectures\lecture_10)

### [Десятый семинар](seminars\seminar_10)

### [Десятое практическое задание](homeworks\homework_10)

## Урок 11.

### [Одиннадцатая лекция](lectures\lecture_11)

### [Одиннадцатый семинар](seminars\seminar_11)

### [Одиннадцатое практическое задание](homeworks\homework_11)

## Урок 12.

### [Двенадцатая лекция](lectures\lecture_12)

### [Двенадцатый семинар](seminars\seminar_12)

### [Двенадцатое практическое задание](homeworks\homework_12)

## Урок 13.

### [Тринадцатая лекция](lectures\lecture_13)

### [Тринадцатый семинар](seminars\seminar_13)

### [Тринадцатое практическое задание](homeworks\homework_13)

## Урок 14.

### [Четырнадцатая лекция](lectures\lecture_14)

### [Четырнадцатый семинар](seminars\seminar_14)

### [Четырнадцатое практическое задание](homeworks\homework_14)

## Урок 15.

### [Пятнадцатая лекция](lectures\lecture_14)

### [Пятнадцатый семинар](seminars\seminar_14)

### [Пятнадцатое практическое задание](homeworks\homework_14)
