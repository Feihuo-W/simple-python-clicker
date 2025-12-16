import pyautogui
import keyboard
import time
import threading

# 这是一个标志位，控制是否正在点击
is_clicking = False
pyautogui.PAUSE = 0
def clicker():
    """这是专门负责点击的函数"""
    global is_clicking
    print("点击器已就绪...")
    print("按 [F8] 开始/暂停")
    print("按 [Esc] 退出程序")
    
    while True:
        if is_clicking:
            # 双击或者单击，这里演示左键单击
            pyautogui.click() 
            # 0.1秒点一次，也就是一秒10下
            time.sleep(0.1) 
        else:
            # 如果没开启，就休息一下，免得占用CPU
            time.sleep(0.1)

def toggle_clicking():
    """切换开关状态"""
    global is_clicking
    is_clicking = not is_clicking
    if is_clicking:
        print(">>> 开始疯狂点击！")
    else:
        print(">>> 已暂停。")

# 开启一个单独的线程来跑点击循环，这样不会卡死主程序
t = threading.Thread(target=clicker)
t.daemon = True
t.start()

# 监听键盘
keyboard.add_hotkey('f8', toggle_clicking)  # 按 F8 切换开关
keyboard.wait('esc')  # 按 Esc 退出整个程序
print("程序已退出")
