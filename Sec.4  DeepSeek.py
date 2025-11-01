#学习目标
#（1）掌握if、else和elif语句的基本结构与用法。
#（2）掌握for循环和while循环的基本结构与用法。
#（3）掌握循环语句中常用的range函数、break语句、continue语句和pass语句的用法
#（4）掌握嵌套循环以及组合选择结构与循环结构。
#（5）了解变量迭代。
#（6）掌握列表解析的创建方法。
#（7）了解异常的基本概念和类型。
#（8）掌握try、except、else、finally语句的基本结构与用法。
#（9）掌握raise语句和assert语句的基本结构与用法   分别用例子让我掌握

#（1）掌握if、else和elif语句的基本结构与用法

# 判断一个数字是正数、负数还是零
"""
num=int(input("请输入一个数字:"))

if num>0:
    print("正数")

elif num<0:
    print("负数")

else:
    print("零")

#（2）掌握for循环和while循环的基本结构与用法。

#for循环用于遍历序列（如列表、字符串等）中的每个元素。

# while循环则在条件为真时重复执行代码块。

#for循环例子：

fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

#while循环例子：

count=1
while count<=5:
    print(count)
    count+=1

#（3）掌握循环语句中常用的range函数、break语句、
# continue语句和pass语句的用法

#range函数：生成一个整数序列，常用于for循环中指定循环次数。

#break：跳出整个循环。

#continue：跳过当前循环的剩余语句，然后继续下一轮循环。

#pass：空语句，用于占位，不执行任何操作。

# 使用range函数
for i in range(5):
    print(i)
print(40*'=')

for i in range(5):
    if i==3:
        break
    print(i)# break例子：当遇到3时跳出循环
print(40*'=')

for i in range(5):
    if i==3:
        continue
    print(i)# continue例子：跳过3
print(40*'=')

# pass例子：如果i等于3，什么也不做，但不会中断循环
for i in range(5):
    if i==3:
        pass
    print(i)

#（4）掌握嵌套循环以及组合选择结构与循环结构。

#嵌套循环：循环内部还有循环。
#组合选择结构与循环结构：在循环中使用if等条件判断。

# 嵌套循环：打印乘法表
for i in range(1,4):
    for j in range(1,4):
        print(f"{i}*{j}={i*j}")

# 组合选择结构与循环：打印1到10之间的偶数
for i in range(1,11):
    if i%2==0:
        print(i)

#（5）了解变量迭代。
#变量迭代指的是在循环中，变量依次取序列中的每个值。

# 变量迭代：在for循环中，变量item依次取列表中的每个值
items = [1,2,3,4,5]
for item in items:
    print(item)

#（6）掌握列表解析的创建方法。
#列表解析是一种快速创建列表的方法，通常用于根据已有列表生成新列表。

# 创建一个列表，包含0到9每个数字的平方
squares=[x**2 for x in range(10)]
print(squares)

# 带条件的列表解析：只包含偶数的平方
even_squares=[x**2 for x in range(10) if x%2==0]
print(even_squares)

#（7）了解异常的基本概念和类型。
#异常是程序执行过程中出现的错误，比如除以零、索引越界等。
# Python有很多内置的异常类型，如ZeroDivisionError、IndexError等。

# 常见的异常类型

ValueError - 值错误
TypeError - 类型错误
IndexError - 索引错误
KeyError - 键错误
ZeroDivisionError - 除零错误
FileNotFoundError - 文件未找到错误

# 查看异常信息
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"发生异常: {type(e).__name__}: {e}")

#（8）掌握try、except、else、finally语句的基本结构与用法。
#try块包含可能抛出异常的代码，except块用于捕获并处理异常，else块在没有异常时执行，
# finally块无论是否发生异常都会执行。

try:
    num = int(input("请输入一个整数: "))
    result = 10 / num
except ZeroDivisionError:
    print("不能除以零！")
except ValueError:
    print("请输入一个有效的整数！")
else:
    print(f"结果是：{result}")
finally:
    print("执行完毕。")

#（9）掌握raise语句和assert语句的基本结构与用法。
#raise语句用于主动抛出异常。assert语句用于断言，如果条件为假则抛出AssertionError异常，常用于调试。
# raise例子：当年龄小于0时抛出异常
age = -1
if age < 0:
    raise ValueError("年龄不能为负数！")

# assert例子：断言x是正数
x = 10
assert x > 0, "x必须是正数"

# 如果x为负数，则断言失败，程序会抛出AssertionError并显示消息

#https://chat.deepseek.com/share/osow0jgw1i6h2fq2vc
"""
# 综合应用：学生成绩管理系统

def process_student_grades(grades):
    """
    处理学生成绩，演示各种控制结构和异常处理
    """
    processed_grades = []

    for grade in grades:
        try:
            # 输入验证
            if not isinstance(grade, (int, float)):
                raise TypeError("成绩必须是数字")

            if grade < 0 or grade > 100:
                raise ValueError("成绩必须在0-100之间")

            # 成绩等级判断
            if grade >= 90:
                level = "优秀"
            elif grade >= 80:
                level = "良好"
            elif grade >= 70:
                level = "中等"
            elif grade >= 60:
                level = "及格"
            else:
                level = "不及格"

            # 使用列表解析创建处理后的数据
            student_data = {
                'original_grade': grade,
                'level': level,
                'passed': grade >= 60
            }

            processed_grades.append(student_data)

        except (TypeError, ValueError) as e:
            print(f"无效成绩 {grade}: {e}")
            continue  # 继续处理下一个成绩

    # 使用列表解析统计通过人数
    passed_count = len([data for data in processed_grades if data['passed']])

    return processed_grades, passed_count


# 测试数据
test_grades = [85, 92, 57, 105, "abc", 78, 63, -5, 88]

# 处理成绩
results, passed = process_student_grades(test_grades)

print("\n处理结果:")
for result in results:
    print(f"成绩{result['original_grade']}: {result['level']}")

print(f"\n总人数: {len(results)}")
print(f"通过人数: {passed}")