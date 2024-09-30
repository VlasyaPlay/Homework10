from time import sleep
from threading import Thread
from datetime import datetime

time_start = datetime.now()

def write_words(word_count, file_name):
    with open (file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            time.sleap(0.1)
        print(f'Завершить запись файла {file_name}')


thr_first = Thread(target=write_words, args=(10, example1.txt))
thr_second = Thread(target=write_words, args=(30, example2.txt))
thr_third = Thread(target=write_words, args=(200, example3.txt))
thr_fourth = Thread(target=write_words, args=(100, example.txt))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end = datetie(now)
time_res = time_end - time_start
print(time_res)
print('Работа потоков завершена')

