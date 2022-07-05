import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(filename='sample.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # настройка
    n = int(input('Сколько директорий вы хотите мониторить?: '))
    print(f"Введите директории для мониторинга ({n} шт.): ")
    path = [input(f'{i + 1}). ') for i in range(n)]
    print(path)
    # 'path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    for i in range(n):
        observer.schedule(event_handler, path[i], recursive=True)
    print(type(event_handler))
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
