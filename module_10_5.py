import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            all_data.append(line.strip())


if __name__ == '__main__':
    names = [f'./file {i}.txt' for i in range(1, 4)]

    start = datetime.datetime.now()
    results = []
    for name in names:
        results.append(read_info(name))
    end = datetime.datetime.now()
    print(end - start)

    start2 = datetime.datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, names)
    end2 = datetime.datetime.now()
    print(end2 - start2)