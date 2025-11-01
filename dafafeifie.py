import math

pi = 3.14  # 设置常量π

#已知半径，计算周长和面积
r=5
C=2*pi*r
S=pi*r**2
print(f"半径为{r}的圆形,周长为{C},面积为{S}.")

#已知周长，计算半径和面积
C1=62.8
r1=C1/(2*pi)
S1=pi*r1**2
print("周长为%f的圆形，半径为%f，面积为%f."%(C1,r1,S1))


#已知面积，计算周长和面积
S2=50.24
r2=math.sqrt(S2/pi)
C2=2*pi*r2
string=("面积为%f的圆形,半径为{},周长为{}."%S2)
print(string.format(r2,C2))
