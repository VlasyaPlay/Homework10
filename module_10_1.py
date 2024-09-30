from time import sleep
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    with open (file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f'Какое-то слово № {i}\n'
            file.write(word)
            sleep(0.1)
    print(f'Завершить запись файла {file_name}')


time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(f'Выполнение последовательных функций {time_res}')

time_start_2 = datetime.now()

thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end_2 = datetime.now()
time_res_2 = time_end_2 - time_start_2
print(f'Работа потоков {time_res_2}')
