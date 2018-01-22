# 数学模块

模块名 math
注:
  linux下为内建模块    
  Mac OS 为标准库模块

## 变量:

math.e  自然常数
math.pi 圆周率

## 函数

math.ceil(x)   对x向上取整, 比如x=1.2,返回2
math.floor(x)  对x向下取整,比如x=1.2 ,返回1
math.sqrt(x)   返回x的平方根
math.factorial(x) 求x的阶乘
math.log(x[, base])  返回以base为底x的对数,如果不给出base,则以自然对数e为底
math.log10(x) 求以10为底x的对数
math.pow(x, y)  返回x**y
math.fabs(x)    返回浮点数x的绝对值

## 角度和弧度转换

math.degrees(x)  将弧度x转换为角度
math.radians(x)  将角度x转换为弧度

## 三角函数

math.sin(x)  返回x的正弦(x为弧度)
math.cos(x)  返回x的余弦
math.tan(x)  返回x的正切
...
math.asin(x)  返回x的反正弦(x为弧度)
math.acos(x)  返回x的反余弦
math.atan(x)  返回x的反正切