#六个字符串方法
s = "  Abc Def  ARe"
print(len(s))  # 计算字符串长度
print(s.upper())  # 转换为大写
print(s.lower())  # 转换为小写
print(s.capitalize())  # 首字母大写
print(s.title())  # 每个单词的首字母大写
print(s.strip())  # 去掉字符串两端的空格
print(s.replace("Abc","XYZ")) # 替换字符串中的内容
print(s.split())  # 将字符串分割为列表   
#变体
print(s.lstrip())  # 去掉字符串左端的空格
print(s.rstrip())  # 去掉字符串右端的空格
print(s.replace("A","x",1))  # 替换字符串中的内容，只替换一次
print(s.replace("A","x",2))  # 替换字符串中的内容，只替换两次
print("a:b".split(":"))  # 按冒号切割字符串为列表



#f-string  f是一个开关，打开它，{} 里的东西就会被换成“值”。
name = "王自强"
age = 19
print("{name}")
print(f"{name}")  #区别
print(f"{name}今年{age}岁")  #区别
print(f"我叫{name} 明年{age + 1}岁")  #age里面可以计算
print(f"{{name}}")  # 输出字面量 {name}
#格式化
pi = 3.141592653589793 
n = 42
print(f"{pi:.2f}")  # 输出 3.14，保留两位小数
print(f"{n:05d}")  # 输出 00042，整数前补零，宽度为5
print(f"{n:^8d}")  # 输出 '   42   '，整数居中，宽度为8
print(f"{n:<8d}")  # 输出 '42      '，整数左对齐，宽度为8
print(f"{n:>8d}")  # 输出 '      42'，整数右对齐，宽度为8
print(f"{12345678:,}")  # 输出 '12,345,678'，整数加上千位分隔符
print(f"{12345678:_}")  # 输出 '12_345_678'，整数加上下划线分隔符,只有整数和小数可以加分隔符
print(f"{12345678:e}")  # 输出 '1.234568e+07'，整数转换为科学计数法
print(f"{12345678:.2e}")  # 输出 '1.23e+07'，整数转换为科学计数法，保留两位小数
print(f"{12345678:E}")  # 输出 '1.234568E+07'，整数转换为科学计数法，使用大写E
print(f"{12345678:b}")  # 输出 '101111000110000101001110'，整数转换为二进制
print(f"{12345678:o}")  # 输出 '57060516'，整数转换为八进制
print(f"{12345678:d}")  # 输出 '12345678'，整数转换为十进制
print(f"{12345678:x}")  # 输出 'bc614e'，整数转换为十六进制



#切片
t = "abcdef"
print(t[0])  #输出第一个字符
print(t[1])  #输出第二个字符
print(t[-1])  #输出最后一个字符
print(t[1:4])  #输出索引1到3的字符
print(t[:3])  #输出前3个字符
print(t[3:6])  #输出索引3到5的字符
print(t[::2])  #输出每隔一个字符的子串
print(t[::-1])  #输出反转后的字符串
print(f"[{t[10:20]}]") #输出索引10到19的字符，超出范围不会报错，返回空字符串
#中文切片
cn = "你好世界"
print(cn[0]) #输出第一个字符
print(cn[1:3]) #输出索引1到2的字符（好世）
print(cn[::-1]) #输出反转后的字符串
rev = cn[::-1] #赋值反转字符串
print(rev)        # 界世好你
print(rev[0])     # 界       ← 取反转后的第一个
print(rev[:2])    # 界世     ← 取反转后的前两个
print(len(rev))   # 4



#链式调用
raw = "  Wang Zhi  "
print(f"[{raw.strip()}]") # 输出 "Wang Zhi"
print(f"[{raw.strip().lower()}]") # 输出 "wang zhi"
print(f"[{raw.strip().lower().replace(' ', '_')}]") # 输出 "wang_zhi"
print(f"[{raw.strip().lower().replace(' ', '_').upper()}]") # 输出 "WANG_ZHI"

#必须知道的两个
#u = "abc"
#u[0] = "X" 
#输出结果
#TypeError: 'str' object does not support item assignment
#字符串不能改
#u = "abc"
#print(u.replace("a", "X"))
#print("u 本身没变:", u)   只能生成新的

#s = "  abc  "
#s.strip()          # 返回 'abc'，但 s 没变
#s = s.strip()      # 要接住


#成品：名片生成器
#版本一
name = input("请输入姓名：").strip()
company = input("请输入公司：").strip()
place = input("请输入地址：").strip()
phone = input("请输入电话：").strip()

print("名片如下：")
print("=" * 30)
print("姓名：", name)
print("公司：", company)
print("地址：", place)
print("电话：", phone)
print("=" * 30)

#版本二（f-string居中）
#name = input("请输入姓名：")
#company = input("请输入公司：")
#place = input("请输入地址：")
#phone = input("请输入电话：")

print("名片如下：")
print("=" * 30)
print(f"{name:^24}")
print(f"{company:^24}")
print(f"{place:^24}")
print(f"{phone:^25}")
print("=" * 30)


#练习题三道
name = "王自强"
print(f"你的名字有{len(name)}个字")

skn = "zhang liang"
# 参考：硬编码写法，只对 zhang liang 有效，换名字就错
print(skn[0].upper() + skn[1:6] + skn[6].upper() + skn[7:])
# 正确：任何名字都对
print(skn.title())

print("你好世界"[::-1])