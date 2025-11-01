#year=2022
#print("年份:%d"%year)
#Science='科技成果登记数'
#quantity=84324
#print("%d年,中国%s为%d项."%(year,Science,quantity))
"""
year=2022
product='主要农产品产量'
quantity=68652.8
string="{}年,中国{}为{}万吨."
print(string.format(year,product,quantity))

print(f"{year}年，中国{product}为{quantity}万吨.")#花括号代指变量


print(2/1);print(type(2/1))#正斜线除法
print(2//1);print(type(2//1))#双正斜线除法

print(1+2,'and',1.0+2);print(1*2,'and',1.0*2)#加法和乘法
print('23除以10,商为',23//10,',余数为',23%10)#商和余数
print(3*'Python ')#字符串的若干次重复

print(1==2);print(1!=2)#数值的比较
print('a'=='b','a'!='b');print('a'<'b','a'>'b')#字符的比较
print(ord('a'),ord('b'),ord('c'),ord('d'))#查看字符对应的ASCII值
print(chr(97),chr(98),chr(99))#查看ASCII值对应的字符
print('#'<'%')#符号的比较

a=1+2;print(a)#简单赋值运算
print('a:',a);a+=4;print('a+=4特殊赋值运算后，a:',a)#特殊赋值运算
f+=4，print(f)#未定义变量不能进行特殊赋值运算

a=60;b=13;print('a=60,b=13')#初始赋值
#按位与,按位或，按位异或运算
print('a&b=',a&b)
print('a|b=',a|b)
print('a^b=',a^b)
#按位取反和位移运算
print('~a=',~a)
print('a<<2=',a<<2)
print('a>>2=',a>>2)
print(bin(60))#看十进制的二进制
print(int('100110',2))#看二进制的十进制  字符串  int('str',2)

a=11;b=22;print('a=11,b=22')#初始赋值
#and，or，not运算
print('a and b =',a and b)
print('a or b =',a or b)
print('not(a and b)=',not(a and b))

a=0;b=22;print('a=0,b=22')#重新赋值
#and，or，not运算
print('a and b =',a and b)
print('a or b =',a or b)
print('not(a and b)=',not(a and b))

List=[1,2,3,0,[4,5],'Python3']#初始化列表List
print(1 in List)#判断1是否属于List
print([1] in List)#判断[1]是否属于List
...

a=11;b=11;print('a=11,b=11')#初始化a，b
print(a is b);print(a is not b)#身份运算
print(id(a));print(id(b))#查看id地址

a=11;b=22;print('a=11,b=22')#重新给b赋值
print(a is b);print(a is not b)#身份运算
print(id(a));print(id(b))#查看id地址

print(24+12/6**2*18) # 24+12/36*18 → 24+(1/3)*18 → 24+6
print(24 + 12 / ( 6 ** 2 ) * 18)  # 24+12/36*18 → 24+(1/3)*18 → 24+6
print(24 + ( 12 / ( 6 ** 2 ) ) * 18)  # 24+(12/36)*18 → 24+(1/3)*18 → 24+6
print(24 + ( 12 / 6 ) ** 2 * 18)  # 24+2**2*18 → 24+4*18 → 24+72
print((24 + 12 ) / 6 ** 2 * 18)  # 36/6**2*18 → 36/36*18 → 1*18
print(-4 * 5 + 3)  # -20+3
print(4 * -5 + 3)  # -20+3

# -*- coding: utf-8 -*-

根据输入计算圆形的其他参数
圆形的相关计算公式参考正文

pi = 3.14  # 设置常量

# 输入半径，求周长、面积
r = 3  # 输入圆形的半径
C = 2 * pi * r  # 计算圆形的周长
S = pi * r ** 2  # 计算圆形的面积
print(f"半径为{r}的圆形,其周长等于{C};面积等于{S};")

# 输入周长，求半径、面积
C = 15.7  # 输入圆形的周长
r = C / ( 2 * pi )  # 计算圆形的半径
S = pi * r ** 2  # 计算圆形的面积
print(f"周长为{str(C)}的圆形,其半径为{str(r)};面积等于{str(S)};")

# 输入面积，求半径、周长
S = 5  # 输入圆形的面积
pi=3.14
r = round(( S / pi ) ** 0.5 , 2)  # 计算圆形的半径，并保留两位小数
C = round( 2 * pi * r , 2)  # 计算圆形的周长，并保留两位小数
print(f"面积为{str(S)}的圆形,其半径为{str(r)};周长等于{str(C)};")
# -*- coding: utf-8 -*-

word='Python'
print(word[1])
print(word[0])
print(word[-1])
print(word[0:3])
print(word[:3])
print(word[4:])
print(word[3:52])#第二个索引越界
print(word[52:])#第一个索引大于字符串长度
print(word[-1:3])#第一个为-1,第二个索引正常
print(word[5:3])#第一个索引值大于第二个索引值
"""