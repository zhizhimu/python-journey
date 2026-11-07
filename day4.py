#if 条件判断
#形态1  只有if
age = int(input("请输入年龄："))
if age >= 18:
    print("你已经成年了")

#形态2  if + else
age2 = int(input("请输入年龄："))
if age2 >= 18:
    print("你已经成年了")
else:
    print("你还未成年")

#形态3  if + elif + else
score = int(input("请输入成绩："))
if score >= 90:
    print("A")
elif score >=80:
    print("B")
elif score >=60:
    print("C")
else:
    print("不及格")

#比较运算符
a = 5
b = 3
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#逻辑运算符
age = 25
print(age >= 18 and age <= 60)
print(age < 18 or age > 60)
print(not (age >= 18))

#年龄判断器
age = int(input("请输入你的年龄："))
if age < 18:
    print("你是未成年")
elif age <= 60:
    print("你已成年")
else:
    print("你已老年")

#练习 1：两数较大值
a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
if a > b:
    print(f"{a}比{b}大")
elif a < b:
    print(f"{a}比{b}小")
else:
    print(f"{a}与{b}相等")

#练习 2：分数等级
score = int(input("请输入你的成绩："))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >=60:
    print("C")
else:
    print("成绩不合格")

#练习 3：闰年判断
c = int(input("请输入年份："))
if c % 4 ==0 and c % 100 != 0:
    print(f"{c}是闰年")
elif c % 400 ==0:
    print(f"{c}是闰年")
else:
    print(f"{c}是平年")

#练习 4：三数最大值
a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
c = int(input("请输入第三个数："))
if a >= b and a >=c:
    print(f"最大的数是{a}")
elif b >= c:
    print(f"最大的数是{b}")
else:
    print(f"最大的数是{c}")

#练习 5：能否投票
a = int(input("请输入你的年龄："))
b = str(input("你是否是中国公民(是/否）："))
if a >=18 and b == str("是"):
    print("可以投票")
else:
    print("你不能参加投票")

#练习 6：英文姓名格式化
name = str(input("请输入你的英文名字："))
print(f"{name.title().strip()}")

#练习 7：密码长度检查
pwd = input("输入密码：")
if len(pwd) >= 8:
    print("密码合格")
else:
    print(f"密码太短，(当前密码{len(pwd)}位,至少需要8位)")

#练习 8：姓名长度检查
name = input("请输入你的名字：")
if len(name) >=2 and len(name) <= 10:
    print("名字合格")
else:
    print(f"名字长度不合格（{len(name )}个字，要求2-10字）")

#练习 9：三角形判定
A = int(input("请输入第一条边的长度；"))
B = int(input("请输入第二条边的长度："))
C = int(input("请输入第三条边的长度："))
if A + B > C and A + C > B and B + C > A:
    print("能构成三角形")
else:
    print("不能构成三角形")

#练习 10：月份天数
year = int(input("请输入年份："))
month = int(input("请输入月份"))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    day = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    day = 30
else:
    if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
        day = 29
    else:
        day = 28
print(f"{year}年{month}月有{day}天")

#练习 11：成绩转等级（五档）
L = int(input("请输入你的成绩："))
if L >=90:
    print("优秀")
elif L >=80:
    print("良好")
elif L >= 70:
    print("中等")
elif L >= 60:
    print("及格")
else:
    print("不及格")

#练习 12：回文判断
ch = input("输入一句话：")
if ch == ch[::-1]:
    print("是回文")
else:
    print("不是回文")