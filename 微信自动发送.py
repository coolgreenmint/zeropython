import win32api
import win32gui
import win32con
import win32clipboard as clipboard
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import random


def send_msg(win):
    win32api.keybd_event(17, 0, 0, 0)  # 按下ctrl
    time.sleep(1)
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, 86, 0)  # 按键v
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开ctrl
    time.sleep(1)
    win32gui.SendMessage(win, win32con.WM_KEYDOWN,
                         win32con.VK_RETURN, 0)  # 回车发送
    return


def txt_ctrl_v(txt_str):
    # 定义文本信息,将信息缓存入剪贴板
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardData(win32con.CF_UNICODETEXT, txt_str)
    clipboard.CloseClipboard()
    return

def get_window(className, titleName):
    title_name = className  # 单独打开，好友名称
    win = win32gui.FindWindow(className, titleName)
    # 窗体前端显示
    # win32gui.SetForegroundWindow(win)
    # 使窗体最大化
    # win32gui.ShowWindow(win, win32con.SW_MAXIMIZE)
    win = win32gui.FindWindow(className, titleName)
    print("找到句柄：%x" % win)
    if win != 0:
        left, top, right, bottom = win32gui.GetWindowRect(win)
        print(left, top, right, bottom)  # 最小化为负数
        win32gui.SetForegroundWindow(win)  # 获取控制
        time.sleep(0.5)
    else:
        print('请注意：找不到【%s】这个人（或群），请激活窗口！' % title_name)
    return win
# 发送过程=================


def sendTaskLog():
    # 查找微信小窗口
    # win = get_window('ChatWnd', '文件传输助手')
    # win = get_window('ChatWnd', '李盛大哥')
    win = get_window('TXGuiFoundation', '马媛')
    names = []
    for i in range(10):
        names.append(i)
    fileName = 'F:\sendmsg\%s.txt' % random.choice(names)
    # 读取文本
    file = open(fileName, mode='r', encoding='UTF-8')
    str = file.read()
    print(str)
    txt_ctrl_v('测试程序发送qq消息！')
    send_msg(win)


scheduler = BlockingScheduler()
scheduler.add_job(sendTaskLog, 'interval', seconds=1)
# scheduler.add_job(sendTaskLog, 'cron',day_of_week='mon-fri', hour=7,minute=31,second='10',misfire_grace_time=30)
#scheduler.add_job(sendTaskLog, 'cron', day_of_week='mon-fri',hour=6, minute=55, second='10', misfire_grace_time=30)
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass
