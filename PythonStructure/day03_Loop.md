

      循环语句：
      - while
      - for
      - break
      - continue
      - 死循环

==============================================

# 循环语句:

- 作用：根据一定的条件，重复的执行一个或多个语句
- 两种循环语句:
  - while语句
  - for 语句

## while语句

- 语法:其中，else子句可以省略
```python
while 真值表达式:
	    语句1
	    ...
else:
  	  语句2
	    ...
```
- 执行顺序：
   1. 先判断真值表达式是否为True<br>
   2. 如果第1步为True,则执行语句1后跳到第1步，否则跳到第3步<br>
   3. 执行else子句<br>
   4. 结束while 语句的执行<br>

- 示例：打印1~10的整数
```python
n = 1
while n <= 10:
	print(n)
	n += 1
```
- while语句嵌套:
```python
while  a > b:
	  while b > c:
      	    ....
	  else:
            ....
```
## for循环语句

for语句可以用来遍历序列或可迭代对象的每一个元素

- 可迭代对象包括:

```python
字符串——str
列表——list
元组 ——tuple
字典 ——dict
集合 ——set
固定集合  ——frozenset
迭代器——
int float bool complex
2 3.14
"ABCD"
```
- for 语句的语法:
```python
for 变量列表 in 可迭代对象:
    语句1
    ...
else:
    语句2
    ...
```
——说明：
    - else子句部分可以省略<br>
    - 语句1的执行次数与可迭代对象的元素个数有关

- for 语句嵌套：
  示意：
```python
for x in "abc":
	  for y in "123":
    	  print(x + y)
#输出结果如下：
a1
a2
a3
b1
b2
b3
c1
c2
c3
```

## break 语句

- 作用：用于循环语句(while, for）中，用来终止当前循环语句的执行

- 说明:
1. break语句通常和if语句组合使用<br>
2. 当break语句执行后，此循环语句break之后的语句将不再执行<br>
3. break语句终止循环时，循环语句的else子句将不会执行<br>
4. break语句只能终止当前循环语句的执行，如有循环嵌套时，不会跳出外重循环<br>

## continue 语句

- 作用：用于循环语句(while,for)中，不再执行本次循环内continue之后的语句，重新开始一次新的循环。

- 示例：打印10以内的偶数
```python
 # 用for 语句实现:见continue.py <br>
 #用while语句实现:
n = 0
while n <= 10:
	print(n)
	n += 2
```
说明：
1. 在while语句中执行continue语句,将会直接跳转到while语句真值表达式处重新判断循环条件.
2. 在for 语句中执行continue语句,将会从可迭代对象中移向下一个元素再次进行循环

## 死循环:

- 死循环是指循环条件一直成立的循环
- 死循环通常用break语句来终止循环
- 死循环的else子句永远不会执行