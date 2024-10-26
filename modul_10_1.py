import threading
import time
from datetime import datetime


def write_words(word_count, file_name):
    file_ = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count + 1):
        time.sleep(0.1)
        ii = 'Какое-то слово № ' + str(i) + '\n'
        file_.write(ii)
    file_.close()
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
res_time = time_end - time_start
print(f'Работа потоков {res_time}')

time_start = datetime.now()
thread_1 = threading.Thread(target = write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target = write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target = write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target = write_words, args=(100, 'example8.txt'))

thread_4.start()
thread_3.start()
thread_2.start()
thread_1.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

time_end = datetime.now()
res_time = time_end - time_start
print(f'Работа потоков {res_time}')
