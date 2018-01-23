# Matplotlib

matplotlib可能是2D图形最常用的Python包。提供了一种非常快速的方式来以可视化方式从Python中获取数据，并以多种格式呈现出版质量数据。

pyplot

pyplot为matplotlib面向对象的绘图库提供了一个方便的接口。

matplotlib中的所有内容都按照层次结构进行组织。层次结构的顶部是由matplotlib.pyplot模块提供的matplotlib“状态机环境” 。在这个级别上，简单的函数用于在当前图中向当前轴添加绘图元素（线，图像，文本等）。

![图形的构成部分](https://matplotlib.org/_images/anatomy.png)

Matplotlib，pyplot和pylab：它们是如何相关的？
Matplotlib是整个包装; matplotlib.pyplot 是matplotlib中的一个模块; 并且pylab是一个安装在一起的模块matplotlib。

Pyplot为底层的面向对象的绘图库提供状态机界面。状态机隐式地自动创建数字和坐标轴以实现所需的绘图。

例子入手:
```python
from pylab import *

#定义numpy 数组，np.linspace()从 −π−π 到 +π+π 取值，等间隔的 256 个值
X = np.linspace(-np.pi, np.pi, 256,endpoint=True) 
C,S = np.cos(X), np.sin(X)  #C 和 S 则分别是这 256 个值对应的余弦和正弦函数值组成的 numpy 数组
plot(X,C)
plot(X,S)

show()
```
以上图形由默认设置输出，以下扩展查看默认设置的内容,可以修改其值查看效果

```python
from pylab import *

figure(figsize=(8,6), dpi=80)   #创建一个 8 * 6 点（point）的图，并设置分辨率为 80
subplot(1,1,1)      ## 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
plot(X, C, color="blue", linewidth=1.0, linestyle="-")  #

# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
plot(X, S, color="green", linewidth=1.0, linestyle="-")

xlim(-4.0,4.0)    # 设置横轴的上下限
ylim(-1.0,1.0)    # 设置纵轴的上下限

xticks(np.linspace(-4,4,9,endpoint=True))   # 设置横轴记号
yticks(np.linspace(-1,1,5,endpoint=True))   # 设置纵轴记号

# savefig("exercice_2.png",dpi=72)    # 以分辨率 72 来保存图片

show()    # 在屏幕上显示
```
### 设置图片边界:修改为:

```python
xlim(X.min()*1.1, X.max()*1.1)
ylim(C.min()*1.1, C.max()*1.1)
```
更好的方式例如以下:
```python
xmin ,xmax = X.min(), X.max()
ymin, ymax = Y.min(), Y.max()

dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2

xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, ymax + dy)
```
讨论正弦和余弦函数的时候，通常希望知道函数在 ±π 和 ±π/2 的值,
```python
xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
yticks([-1, 0, +1])
```

轴上是π和 π/2 的设置记好的标签,值的显示设置不转化为具体数字,这里使用了 **LaTeX**。
```python
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
```
### 移动脊柱Spines

坐标轴线和上面的记号连在一起就形成了脊柱（Spines，一条线段上有一系列的凸起，是不是很像脊柱骨啊~），它记录了数据区域的范围。它们可以放在任意位置，不过至今为止，我们都把它放在图的四边

实际上每幅图有四条脊柱（上下左右），为了将脊柱放在图的中间，我们必须将其中的两条（上和右）设置为无色，然后调整剩下的两条到合适的位置——数据空间的 0 点。
```python
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
```
### 添加图例Legend

我们在图的左上角添加一个图例。为此，我们只需要在 plot 函数里以「键 - 值」的形式增加一个参数。

```python
plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")

legend(loc='upper left')
```
### 特殊点做注释

希望在 2π/3 的位置给两条函数曲线加上一个注释。首先，我们在对应的函数图像位置上画一个点；然后，向横轴引一条垂线，以虚线标记；最后，写上标签。

```python
t = 2*np.pi/3
plot([t,t],[0,np.cos(t)], color ='blue', linewidth=2.5, linestyle="--")
scatter([t,],[np.cos(t),], 50, color ='blue')

annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
         xy=(t, np.sin(t)), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plot([t,t],[0,np.sin(t)], color ='red', linewidth=2.5, linestyle="--")
scatter([t,],[np.sin(t),], 50, color ='red')

annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
         xy=(t, np.cos(t)), xycoords='data',
         xytext=(-90, -50), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
```
![]() 插入图片

坐标轴上的记号标签被曲线挡住了，可以把它们放大，然后添加一个白色的半透明底色。这样可以保证标签和曲线同时可见。

```python
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))
```

到目前为止，我们都用隐式的方法来绘制图像和坐标轴。快速绘图中，这是很方便的。我们也可以显式地控制图像、子图、坐标轴。

### 图像

Matplotlib 中的「图像」指的是用户界面看到的整个窗口内容。图形界面中可以按下右上角的 X 来关闭窗口（OS X 系统是左上角）。Matplotlib 也提供了名为 close 的函数来关闭这个窗口。close 函数的具体行为取决于你提供的参数：

不传递参数：关闭当前窗口；
传递窗口编号或窗口实例（instance）作为参数：关闭指定的窗口；
all：关闭所有窗口。
和其他对象一样，你可以使用 setp 或者是 set_something 这样的方法来设置图像的属性。

### 子图

在图像里面有所谓「子图」。子图的位置是由坐标网格确定的.我们已经隐式地使用过图像和子图：当我们调用 plot 函数的时候，matplotlib 调用 gca() 函数以及 gcf() 函数来获取当前的坐标轴和图像；如果无法获取图像，则会调用 figure() 函数来创建一个——严格地说，是用 subplot(1,1,1) 创建一个只有一个子图的图像。
用 subplot 函数的时候，你需要指明网格的行列数量，以及你希望将图样放在哪一个网格区域中。此外，gridspec 的功能更强大，你也可以选择它来实现这个功能

使用子图只需要一个额外的步骤，就可以像前面的例子一样绘制数据集。即在调用 plot() 函数之前需要先调用 subplot() 函数。该函数的第一个参数代表子图的总行数，第二个参数代表子图的总列数，第三个参数代表活跃区域。

```python
x = np.linspace(0, 2 * np.pi, 50)
plt.subplot(2, 1, 1) # （行，列，活跃区）
plt.plot(x, np.sin(x), 'r')
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), 'g')
plt.show()
```
区别以下代码:
```python
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-o',
        x, np.cos(x), 'g--')
plt.show()
```

### 坐标轴

坐标轴和子图功能类似，但「坐标轴」不受坐标网格限制，可以放在图像的任意位置。因此，如果你希望在一副图中绘制一个小图，就可以用这个功能。

### 记号

良好的记号是图像的重要组成部分。Matplotlib 里的记号系统里的各个细节都是可以由用户个性化配置的。你可以用 Tick Locators 来指定在那些位置放置记号，用 Tick Formatters 来调整记号的样式。主要和次要的记号可以以不同的方式呈现。默认情况下，每一个次要的记号都是隐藏的，也就是说，默认情况下的次要记号列表是空的——NullLocator

Tick Locators

(NullLocator/IndexLocator/FixedLocator/LinearLocator/MultipleLocator/AutoLocator/LogLocator )都是 matplotlib.ticker.Locator 的子类，你可以据此定义自己的 Locator。

以日期为 ticks 特别复杂，因此 Matplotlib 提供了 matplotlib.dates 来实现这一功能




---------------------   

[参考网址:](https://www.labri.fr/perso/nrougier/teaching/matplotlib/)
