import os
from os import path
import time
import shutil

if __name__ == "__main__":
    # setting
    print("存档文件会被放置在.\Documents\Paradox Interactive\Hearts of Iron IV\save games")
    print("为了便于区分，这些用于战报制作的存档会被放置在该目录下的一个新文件夹内")
    folder_name = input("请输入文件夹名称：")
    os.mkdir(folder_name)
    file_prefix = input("请输入战报存档的前缀：")
    print("下面的问题只接受整数作为答案，其他输入会导致游戏崩溃")
    print("")
    start_year = (int)(input("战报是从哪一年开始的（请输入数字，下同）："))
    start_month = (int)(input("战报是从哪一个月开始的："))
    start_day = (int)(input("战报是从几号开始的："))
    date_set = [start_year, start_month, start_day]
    print("你选择的自动存档选项是：")
    save_set = (int)(input("1 每周，2 每月，3 每年："))
    print("战报存档存储器开始运行，当您退出游戏后，请关闭该窗口以停止运行")
    while (True):
        time.sleep(1)
        if path.exists("autosave.hoi4"):
            temp_name = file_prefix + "_" + str(date_set[0]) + "_" + str(date_set[1]) + "_" + str(date_set[2]) + ".hoi4"
            os.rename("autosave.hoi4", temp_name)
            shutil.move(temp_name, folder_name)

            if save_set == 1:
                date_set[2] += 7
            if save_set == 2:
                date_set[1] += 1
            if save_set == 3:
                date_set[0] += 1

            if (date_set[1] in {1, 3, 5, 7, 8, 10, 12} and date_set[2] > 31):
                date_set[1] += 1
                date_set[2] = date_set[2] - 31
            if (date_set[1] in {2} and date_set[2] > 28):
                date_set[1] += 1
                date_set[2] = date_set[2] - 28
            if (date_set[1] in {4, 6, 9, 11} and date_set[2] > 30):
                date_set[1] += 1
                date_set[2] = date_set[2] - 30
            if (date_set[1] > 12):
                date_set[0] += 1
                date_set[1] = 1
