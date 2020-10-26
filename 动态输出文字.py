# 动态输出文字

import sys
import time
import random

# for i in range(10):
#     print("\r" + str(i), end="")
#     time.sleep(random.randint(1, 5))


def print_act(word):
    sys.stdout.write("\r")
    sys.stdout.flush()
    for item in word:
        sys.stdout.write(item)
        sys.stdout.flush()
        time.sleep(0.3)
    print("访澳旅客 " + chr(0x1f6a) + "     " + chr(0x2b50) + "访澳旅客")


while True:
    print_act("VISITANTES     VISTANTES")
