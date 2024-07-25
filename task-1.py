import queue
import random
import time

# Створення черги заявок
application_queue = queue.Queue()


def generate_request():
    # Створення нової заявки з унікальним номером
    request_id = random.randint(1, 1000)
    print(f"Створено заявку: {request_id}")
    # Додавання заявки до черги
    application_queue.put(request_id)


def process_request():
    # Якщо черга не порожня
    if not application_queue.empty():
        # Видалення заявки з черги
        request_id = application_queue.get()
        # Обробка заявки
        print(f"Обробка заявки: {request_id}")
    else:
        # Виведення повідомлення про порожню чергу
        print("Черга порожня")


# Основний цикл програми
try:
    while True:
        # Виклик функції для створення нових заявок
        generate_request()
        # Виклик функції для обробки заявок
        process_request()
        # Імітація затримки між операціями
        time.sleep(1)

except KeyboardInterrupt:
    print("Вихід з програми.")  # Для виходу натисніть Ctrl + C
