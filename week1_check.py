name = "王自强"
age = 19
print("1) 变量+类型：",name, age, type(name), type(age))
print("2) input 返回：", type("19").__name__, "加int后：", type(int("19")).__name__)
print("3) 运算符 // % **：", 7 // 2, 7 % 2, 2**10)
print("4) round:",round(3.14159,2))
print("5) 字符串方法：","   abc   ".strip().upper())
print("6) f-string:",f"{name}今年{age}岁")
print("7) 切片：","abcdef"[1:4],"abcdef"[::-1])