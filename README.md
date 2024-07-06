# Домашнє завдання до теми “Основні структури даних”

- Вітаємо! Як настрiй? Сподiваємося, що ви з нетерпiнням очікуєте на новий челендж 😉

- Сьогодні ви відпрацюєте навички правильного застосування структур даних для конкретних завдань, що є вкрай важливим для розробки ефективних алгоритмів та програм.

Які саме ключові структури даних потрібно використати?

- чергу (клас Queue з модуля queue ), що дозволить зімітувати систему обробки заявок у сервісному центрі;
- двосторонню чергу (deque з модуля collections), щоб створити програму, яка перевіряє, чи є заданий рядок паліндромом.

Таким чином, домашнє завдання буде складатися з двох незалежних завдань.

> [!IMPORTANT]
>
> 💡 Крім того, вам пропонується третє, необов’язкове завдання на використання стеку, якщо ви бажаєте поглибитись у тему 😉

## Опис домашнього завдання

### Завдання 1

Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги для "обробки", імітуючи таким чином роботу сервісного центру.

Ось псевдокод для завдання з використанням черги (Queue з модуля queue в Python) для системи обробки заявок:

```Python
import Queue

Створити чергу заявок
queue = Queue()

Функція generate_request():
Створити нову заявку
Додати заявку до черги

Функція process_request():
Якщо черга не пуста:
Видалити заявку з черги
Обробити заявку
Інакше:
Вивести повідомлення, що черга пуста

Головний цикл програми:
Поки користувач не вийде з програми:
Виконати generate_request() для створення нових заявок
Виконати process_request() для обробки заявок
```

У цьому псевдокоді використовуються дві основні функції: generate_request(), яка генерує нові заявки та додає їх до черги, та process_request(), яка обробляє заявки, видаляючи їх із черги. Головний цикл програми виконує ці функції, імітуючи постійний потік нових заявок та їх обробку.

### Завдання 2

Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.

### Завдання 3 (необов'язкове завдання)

У багатьох мовах програмування ми маємо справу з виразами, виділеними символами-розділювачами, такими як круглі ( ), квадратні [ ] або фігурні дужки { }.

Напишіть програму, яка читає рядок з послідовністю символів-розділювачів, наприклад, ( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, коли розділювачі симетричні, несиметричні, наприклад ( ( ( ) , або коли розділювачі різних видів стоять у парі, як-от ( }.

> [!IMPORTANT]
>
> 💡 Використовуйте стек, щоб запам'ятати відкриті в даний момент символи-розділювачі.

Приклад очікуваного результату:

```Python
( ){[ 1 ]( 1 + 3 )( ){ }}: Симетрично
( 23 ( 2 - 3);: Несиметрично
( 11 }: Несиметрично
```

## Підготовка та завантаження домашнього завдання

1. Створіть публічний репозиторій `goit-algo-hw-02`.

2. Виконайте завдання та відправте його у свій репозиторій.

3. Завантажте робочі файли на свій комп’ютер та прикріпіть їх у LMS у форматі `zip`. Назва архіву повинна бути у форматі ДЗ2_ПІБ.

4. Прикріпіть посилання на репозиторій `goit-algo-hw-02` та відправте на перевірку.

> [!IMPORTANT]
>
> 💡 ВАЖЛИВО Перегляньте Інструкцію щодо завантаження робочого файлу з репозиторію на Github

## Формат здачі

- Прикріплені файли репозиторію у форматі `zip` з назвою ДЗ2_ПІБ.
- Посилання на репозиторій.

Критерії прийняття ДЗ

Прикріплені посилання на репозиторій `goit-algo-hw-02` та безпосередньо самі файли репозиторію у форматі `zip`.

### Завдання 1:

Код виконується, використано клас Queue з модуля queue в Python.

Програма автоматично генерує нові заявки, додає їх до черги, а потім послідовно видаляє з черги.

Структура коду відповідає наданому псевдокоду.

### Завдання 2:

Код виконується, використано deque з модуля collections у Python.

Програма правильно перевіряє, чи є заданий рядок паліндромом, враховуючи рядки з парною та непарною кількістю символів, та є нечутливою до регістру та пробілів.

### Завдання 3 (необов'язкове завдання):

Завдання є додатковим, тому не оцінюється, проте, за бажанням, ви можете отримати конструктивний зворотний зв'язок від ментора.

## Формат оцінювання

Залік/незалік
