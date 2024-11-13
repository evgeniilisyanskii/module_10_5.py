import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':

    file_list = [f'file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for file_name in file_list:
        read_info(file_name)
    end_time = time.time()
    print(f'Линейное выполнение заняло {end_time - start_time} секунд')

    start_time2 = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_list)
    end_time2 = time.time()
    print(f'Многопроцессорное выполнение заняло {end_time2 - start_time2} секунд')