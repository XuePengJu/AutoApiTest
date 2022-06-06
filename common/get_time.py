import time


def get_now_time():
    print(time.strftime('%H:%M:%S', time.localtime()))


def return_timeout():
    time_out = time.strftime('%Y_%m_%d_%H', time.localtime())
    print(time_out)
    return time_out


def timetamp_format_standard_time(timestamp):
    """
    时间戳格式化为标准时间
    :param timestamp:
    :return:
    """
    time_local = time.localtime(timestamp)
    standard_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    print(standard_time)
    return standard_time


if __name__ == '__main__':
    get_now_time()
    return_timeout()
    timetamp_format_standard_time(time.time())
