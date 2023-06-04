# 导入time模块
import time

# 设置专注时长（分钟）
focus_time = 25

# 设置休息时长（分钟）
break_time = 5

# 设置专注次数
focus_count = 4

# 定义一个函数，用于显示倒计时
def countdown(minutes):
    # 将分钟转换为秒
    seconds = minutes * 60
    # 循环直到秒数为零
    while seconds > 0:
        # 打印当前的分钟和秒数，格式为mm:ss
        print(f"{seconds // 60:02d}:{seconds % 60:02d}", end="\r")
        # 每隔一秒减一
        time.sleep(1)
        seconds -= 1
    # 打印换行符
    print()

# 开始专注时钟
print("开始专注时钟！")
# 循环专注次数
for i in range(focus_count):
    # 打印当前的专注次数
    print(f"第{i + 1}次专注")
    # 调用倒计时函数，传入专注时长
    countdown(focus_time)
    # 播放提示音或显示提示信息，表示专注时间结束
    print("哔哔哔，专注时间结束！")
    # 判断是否是最后一次专注
    if i == focus_count - 1:
        # 如果是最后一次专注，结束程序
        print("恭喜您，完成了所有的专注时钟！")
        break
    else:
        # 如果不是最后一次专注，继续休息时钟
        print("开始休息时钟！")
        # 调用倒计时函数，传入休息时长
        countdown(break_time)
        # 播放提示音或显示提示信息，表示休息时间结束
        print("哔哔哔，休息时间结束！")
