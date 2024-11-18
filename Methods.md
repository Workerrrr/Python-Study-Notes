# Python 方法表
本笔记使用的Python版本为3.11

`更新时间:2024-10-18`
## 变量与简单数据类型

### 数据容器

#### 字符串str.

`replace(ori, str)`: 将原字符串内的子串`ori`替换为`str`, 并返回整个字符串<br>
`split(str)`: 分割以`str`为分隔的子串, 并返回一个列表<br>
`title()`: 使字符串首字母大写<br>
`lower()`: 使字符串全小写<br>
`upper()`: 使字符串全大写<br>
`rstrip(str)`: 如果存在参数`str`, 删除字符串右侧的子串`str`, 否则删除字符串右侧的空白<br>
`lstrip(str)`: 如果存在参数`str`, 删除字符串左侧的子串`str`, 否则删除字符串左侧的空白<br>
`strip(str)`: 如果存在参数`str`, 删除字符串左右的子串`str`, 否则删除字符串左右的空白<br>

#### 列表list.

`index(value)`: 查询列表中元素`value`的下标<br>
`insert(sub, value)`: 在下标`sub`的位置插入元素`value`<br>
`append(value)`: 为列表追加元素`value`<br>
`extend(con)`: 为列表追加另一个数据容器`con`<br>
`pop(sub)`: 弹出列表中指定下标`sub`的元素<br>
`remove(value)`: 删除列表中指定元素`value`<br>
`clear()`: 清空列表<br>
`count(value)`: 统计列表中元素`value`的数量<br>
`sort(reverse)`: 为列表永久排序, 使用参数`reverse`设置排序方式<br>
`reverse()`: 为列表永久倒序<br>

#### 元组tuple.

`index(value)`: 查询元组中元素`value`的下标<br>
`count(value)`: 统计元组中元素`value`的数量<br>

#### 集合set.

## 文件

### 文件读取

`read(num)`: 按指定字节数`num`读取文件, 不指定则默认读取文件全部内容, 返回一个字符串<br>
`readline()`: 读取文件一行内容, 返回一个字符串<br>
`readlines()`: 读取文件全部内容, 以每一行一个元素返回一个列表, 包含转义字符<br>
