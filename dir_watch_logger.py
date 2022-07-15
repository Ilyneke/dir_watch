import sys
import datetime
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        operation = event.event_type
        Filing(NamePath, path, operation, event.src_path)

    def on_created(self, event):
        operation = 'on_created'
        Filing(NamePath, path, operation, event.src_path)

    def on_deleted(self, event):
        operation = 'on_deleted'
        Filing(NamePath, path, operation, event.src_path)

    def on_modified(self, event):
        operation = 'on_modified'
        Filing(NamePath, path, operation, event.src_path)

    def on_moved(self, event):
        operation = 'on_moved'
        Filing(NamePath, path, operation, event.src_path)


def Filing(mass_name_path, mass_path, operation, path):
    for i in range(len(mass_path)):
        if mass_path[i] == path[:len(mass_path[i])]:
            my_file = open(mass_name_path[i] + ".log", "a")
            my_file.write(operation + now.strftime("%Y-%m-%d %H:%M:%S") + ' ' + path + '\n')
            my_file.close()


if __name__ == "__main__":

    now = datetime.datetime.now()

    n = int(input('Сколько директорий вы хотите мониторить?: '))
    print(f"Введите директории для мониторинга ({n} шт.): ")
    path = [input(f'{i + 1}). ') for i in range(n)]

    NamePath = path.copy()

    for i in range(n):
        NamePath[i] = NamePath[i].replace("\\", "_")
        my_file = open(NamePath[i] + '.log', "a")
        my_file.close()

    # 'path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MyHandler()
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