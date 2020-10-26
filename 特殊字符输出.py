# 输出特殊字符
'''
  windows系统中， 使用 win + R ，然后输入charmap 即可查看系统字符映射表
  linux系统中， 可以打开字符程序查看
  此程序根据字符的十六进制输出系统中的特殊字符
'''


def nextLine():
    print("")
    print("-" * 20)


# 输出猫脸
for i in range(0x1f638, 0x1f641):
    print("--".join(chr(i)), end=" ")

nextLine()

# 输出植物
for i in range(0x1f331, 0x1f344):
    print("--".join(chr(i)), end=" ")

nextLine()

# 输出动物(十二生肖)
for i in range(0x1f400, 0x1f417):
    print("--".join(chr(i)), end=" ")

nextLine()

# 输出箭头
print([chr(i) for i in range(8592, 8704)])

nextLine()
