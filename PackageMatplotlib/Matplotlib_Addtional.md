## pyplot快速绘图

matplotlib实际上是一套面向对象的绘图库，它所绘制的图表中的每个绘图元素，例如线条Line2D、文字Text、刻度等在内存中都有一个对象与之对应。

为了方便快速绘图matplotlib通过pyplot模块提供了一套和MATLAB类似的绘图API，将众多绘图对象所构成的复杂结构隐藏在这套API内部。我们只需要调用pyplot模块所提供的函数就可以实现快速绘图以及设置图表的各种细节。pyplot模块虽然用法简单，但不适合在较大的应用程序中使用。

为了将面向对象的绘图库包装成只使用函数的调用接口，pyplot模块的内部保存了当前图表以及当前子图等信息。当前的图表和子图可以使用plt.gcf()和plt.gca()获得，分别表示"Get Current Figure"和"Get Current Axes"。

在pyplot模块中，许多函数都是对当前的Figure或Axes对象进行处理，比如说：

plt.plot()实际上会通过plt.gca()获得当前的Axes对象ax，然后再调用ax.plot()方法实现真正的绘图。

可以在Ipython中输入类似"plt.plot??"的命令查看pyplot模块的函数是如何对各种绘图对象进行包装的。

### 面向对象画图

matplotlib API包含有三层，Artist层处理所有的高层结构，例如处理图表、文字和曲线等的绘制和布局。通常我们只和Artist打交道，而不需要关心底层的绘制细节。

直接使用Artists创建图表的标准流程如下：

- 创建Figure对象
- 用Figure对象创建一个或者多个Axes或者Subplot对象
- 调用Axies等对象的方法创建各种简单类型的Artists

翻译成 Python 
```python
import matplotlib.pyplot as Plt
import mpmath as Mp

X = ...
Y = ...
#Y = [Mp.sqrt(num) for num in X]     # y = x^(1/2)

Fig = Plt.figure()                      # Create a `figure' instance
Ax = Fig.add_subplot(111)               # Create a `axes' instance in the figure
Ax.plot(X, Y)                           # Plot in the axes
Fig.savefig("test.pdf")
```

### 配置属性

matplotlib所绘制的图表的每个组成部分都和一个对象对应，我们可以通过调用这些对象的属性设置方法set_*()或者pyplot模块的属性设置函数setp()设置它们的属性值。

### 在一张图上绘制两个数据集

大多数时候可能更想在一张图上绘制多个数据集。用 Matplotlib 也可以轻松实现这一点.

```python

x = np.linspace(0, 2 * np.pi, 50)

#绘制表示函数 sin(x) 和 sin(2x) 的图形
plt.plot(x, np.sin(x),
        x, np.sin(2 * x))
plt.show()
```
区分以下代码,不同在于这段代码在调用 plt.plot() 的时候多传入了一个数据集，并用逗号与第一个数据集分隔开。

```python
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x)) # 如果没有第一个参数 x，图形的 x 坐标默认为数组的索引
plt.show() # 显示图形
```

## matplotlib.markers

class matplotlib.markers.MarkerStyle(marker=None, fillstyle=None)

- filled_markers = ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')
- fillstyles = ('full', 'left', 'right', 'bottom', 'top', 'none')
- markers = {'.': 'point', ',': 'pixel', 'o': 'circle', 'v': 'triangle_down', '^': 'triangle_up', '<': 'triangle_left', '>': 'triangle_right', '1': 'tri_down', '2': 'tri_up', '3': 'tri_left', '4': 'tri_right', '8': 'octagon', 's': 'square', 'p': 'pentagon', '*': 'star', 'h': 'hexagon1', 'H': 'hexagon2', '+': 'plus', 'x': 'x', 'D': 'diamond', 'd': 'thin_diamond', '|': 'vline', '_': 'hline', 'P': 'plus_filled', 'X': 'x_filled', 0: 'tickleft', 1: 'tickright', 2: 'tickup', 3: 'tickdown', 4: 'caretleft', 5: 'caretright', 6: 'caretup', 7: 'caretdown', 8: 'caretleftbase', 9: 'caretrightbase', 10: 'caretupbase', 11: 'caretdownbase', 'None': 'nothing', None: 'nothing', ' ': 'nothing', '': 'nothing'}¶

|**marker**|**description**|
|----------|---------------|
|"."	|point|
|","	|pixel|
|"o"	|circle|
|"v"	|triangle_down|
|"^"	|triangle_up|
|"<"	|triangle_left|
|">"	|triangle_right|
|"1"	|tri_down|
|"2"	|tri_up|
|"3"	|tri_left|
|"4"	|tri_right|
|"8"	|octagon|
|"s"	|square|
|"p"	|pentagon|
|"P"	|plus (filled)|
|"*"	|star|
|"h"	|hexagon1|
|"H"	|hexagon2|
|"+"	|plus|
|"x"	|x|
|"X"	|x (filled)|
|"D"	|diamond|
|"d"	|thin_diamond|
|"|"	|vline|
|"_"	|hline|


## Matplotlib.pylab快速绘图

matplotlib还提供了一个名为pylab的模块，其中包括了许多NumPy和pyplot模块中常用的函数，方便用户快速进行计算和绘图，十分适合在IPython交互式环境中使用


一个《用Python做科学计算》中的简单例子，下面的两行程序通过调用plot函数在当前的绘图对象中进行绘图：

plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")

plot函数的调用方式很灵活，第一句将x,y数组传递给plot之后，用关键字参数指定各种属性：

label : 给所绘制的曲线一个名字，此名字在图示(legend)中显示。只要在字符串前后添加"$"符号，matplotlib就会使用其内嵌的latex引擎绘制的数学公式。
color : 指定曲线的颜色
linewidth : 指定曲线的宽度


Double Map
Python 内建了一个很有用的 map 函数，用来把一个函数作用在一 个列表的每一个元素上。List comprehension 基本上就是这个函数的一个语法糖。 但是 map 只对一元函数和一维列表有用。如果我们要画一个二元 函数，我们肯定希望有 map 的二维版本。这个可以简单地用两个 map 嵌套实现：

```python
def maap(f, a, b):
    return map(lambda x: map(lambda y: f(x, y), b), a)
```
这样如果 a=(a0,a1,...,an−1)a=(a0,a1,...,an-1), b=(b0,b1,...,bm−1)b=(b0,b1,...,bm-1)，maap(func a, b) 返回一个矩阵 A,

Aij=f(ai,bj)Aij=f(ai,bj).





---------
[参考页面:](https://matplotlib.org)

[相关](https://liam0205.me/2014/09/11/matplotlib-tutorial-zh-cn/)

[待学习页面:](https://liam0205.me/2014/09/08/latex-introduction/)
