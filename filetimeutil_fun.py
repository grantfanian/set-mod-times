import datetime
import os
import time
try:
    import win32file
    import win32con
    from pywintypes import Time as wintime
    __use_win_32 = True
except:
    __use_win_32 = False


def do_ttime(datetime_obj):
    return time.mktime(datetime_obj.timetuple())


def set_file_dates(filename, dates):
    # вроде должно принимать как
    # создано, произошёл доступ, изменено
    dates = [do_ttime(i) for i in dates]
    if __use_win_32:
        filehandle = win32file.CreateFile(
            filename, win32file.GENERIC_WRITE, 0, None, win32con.OPEN_EXISTING, 0, None)
        win32file.SetFileTime(filehandle, *[wintime(int(i)) for i in dates])
        filehandle.close()
    else:
        os.utime(filename, tuple(dates[1:]))


def string_to_time(s):
    return datetime.datetime.strptime(s, "%d.%m.%Y %H:%M:%S")


if __name__ == "__main__":
    print(r"Ввод производится в формате: %d.%m.%Y %H:%M:%S")
    file = input("Введите нужное имя файла: ")
    ctime = string_to_time(input("Введите нужное время создания: "))
    atime = string_to_time(input("Введите нужное время доступа: "))
    mtime = string_to_time(input("Введите нужное время изменения: "))
    set_file_dates(file, [ctime, atime, mtime])