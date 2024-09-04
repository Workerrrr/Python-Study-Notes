# Python 学习笔记
本笔记使用的Python版本为3.11

`更新时间:2024-09-04`

- `<>`必填项，必须在当前位置填写相应数据
- `{}`必选项，必须在当前位置选择一个给出的选项
- `[]`可选项，可以选择填写或忽略

*print("Hello World!")*

## Python 基础语法

**数据类型**

Python 中有6个数据类型，分别是:
- 数字(Number)
> 数字类型又可分为4种类型，即 整数(int), 浮点数(float), 
复数(complex), 布尔值(bool) <br>
> 
> - 整数(int), 例如 `10`, `-10`, `123`<br>
> - 浮点数(float), 例如 `13.4`, `-13.4`<br>
> - 复数(complex), 例如 `4+3j`, 以`j`结尾表示复数<br>
> - 布尔值(bool), 真(true), 假(false), 本质上是一个数字,
> `1`表示`true`, `0`表示`false`
- 字符串(String)
> 由任意数的字符组成, 必须用双引号`"`围起来, 例如 `"abc123"`, `"Python学习笔记"`
- 列表(List)
> 有序的可变序列, Python中使用最频繁数据类型
- 元组(Tuple)
> 有序的不可变序列, 可有序记录一堆不可变地Python数据集合
- 集合(Set)
> 无序不重复集合, 可无序记录一堆不重复地Python数据集合
- 字典(Dictionary)
> 无序Key-Value集合, 可无序记录一堆Key-Value型的Python数据集合

**注释**

*在所有编程语言中, 注释都是非常重要的工具*

在Python中, 注释与大多数编程语言一样, 分为两类<br>
- 行注释: 以井号`#`开头, 井号的右边所有文字作为注释
    ```python
    # 这是一条注释
    # 这是一条注释
    # 这是一条注释
    ```
- 段落注释: 用 一对三个双引号`"""` 括起来的内容作为段落注释
    ```python
    """
        这是一条注释
        这是一条注释
        这是一条注释 
    """
    ```
**变量**

Python是动态类型语言, 所以定义变量时无需声明变量类型

定义变量的格式: `<变量名>` = `<变量值>`
```python
# 定义一些变量
a = 1
b = 2.0
c = "Python"
# 输出这些变量
print(a, b, c)
```
![alt text](img/img-1.png)

Python从3.6开始也支持静态类型

静态类型变量的定义格式: `<变量名>` : `<变量类型>` = `<变量值>`
```python
# 定义一些静态变量
a : int = 1
b : float = 2.0
c : str = "Python"
# 输出这些变量
print(a, b, c)
```
![alt text](img/img-1.png)

Python本质上还是动态类型语言, 所以运行时还是以动态类型方式, 即使变量值与声明的类型不一致仍然能够运行
```python
# 定义一些与声明类型不一致的静态变量
a : str = 1
b : int = 2.0
c : bool = "Python"
# 输出这些变量
print(a, b, c)
```
![alt text](img/img-1.png)

**数据类型与转换**

上面我们已经学习了Python中常见的数据类型, 这里我们主要了解获取数据类型的方式与数据类型转换

Python提供一个专门的函数 `type()`用于获取字面量的数据类型
```python
# 定义几个变量
a = 1       # 变量 a 是 int 类型
b = 2.0     # 变量 b 是 float 类型
c = "Python" # 变量 C 是 string 类型
# 获取并输出这几个变量的数据类型
print(type(a))
print(type(b))
print(type(c))
```
![alt text](img/img-2.png)

需要注意的是, 字符串类型(string) 的类型标识符为`str`, 而不是`string`

也可以使用`type()`函数直接获取字面量的数据类型
```python
# 使用type()函数直接获取字面量的数据类型
print(type(123))
print(type(1.23))
print(type("1 2 3"))
```
![alt text](img/img-2.png)

使用`type()`函数获取静态类型变量的数据类型时, 结果是怎样的?
```python
# 定义静态类型变量
a : int = 1
# 输出变量的数据类型
print(type(a))
# 给静态类型变量赋予一个不同类型的数据
a = 2.0
# 输出变量的数据类型
print(type(a))
```
![alt text](img/img-3.png)

也就是说, 即使使用静态类型变量, 其数据类型仍然跟随所储存的字面量的数据类型