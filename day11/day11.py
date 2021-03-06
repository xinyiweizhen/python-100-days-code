import time
from math import sqrt


def read_file():
    """读取文件练习"""
    try:
        with open('致橡树.txt', 'r', encoding = 'utf-8') as f:
            # 一次性读取整个文件内容
            print(f.read())
        # 通过for-in循环逐行读取
        with open('致橡树.txt', mode='r') as f:
            for line in f:
                print(line, end='')
                time.sleep(0.5)
        print()

        # 读取文件按行读取到列表中
        with open('致橡树.txt') as f:
            lines = f.readlines()
        print(lines)

    except FileNotFoundError:
        print('文件未找到')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


def is_prime(number):
    """是否是素数"""
    assert number > 0
    for n in range(2, int(sqrt(number)) + 1):
        if number % n == 0:
            return False
        return True if number != 1 else False
def write_file():
    """写入文件"""
    filenames = ('1-99.txt', '100-999.txt', '1000-9999.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + ' ')
                elif number < 1000:
                    fs_list[1].write(str(number) + ' ')
                else:
                    fs_list[2].write(str(number) + ' ')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')


if __name__ == '__main__':
    # read_file()
    write_file()