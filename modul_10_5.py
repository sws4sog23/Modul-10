import multiprocessing
from multiprocessing import Pool
import time
from datetime import datetime
def read_info(name):
    all_data = []
    file = open(name, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        all_data.append(line)
    file.close()

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# time_start = datetime.now()
# res_=list(map(read_info, filenames))
# time_end = datetime.now()
# res_time = time_end - time_start
# print(f'Линейный вызов {res_time}')

if __name__ == '__main__':
    time_start = datetime.now()
    with Pool(processes=4) as pool:
        res_p = pool.map(read_info, filenames)
        time_end = datetime.now()
        res_time = time_end - time_start
        print(f'Многопроцессный вызов {res_time}')


