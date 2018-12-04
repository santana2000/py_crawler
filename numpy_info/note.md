Python数值计算
NumPy本身并没有提供多么高级的数据分析功能，理解NumPy数组以及面向数组的计算将有助于你更加高效地使用诸如pandas之类的工具
可以高效处理大数组的数据
ndarry   N维数组  dimension 维度   
其中的所有元素必须是相同类型的/shape/dtype(数组数据类型)

my_data1 = [2,4,4,5,6,7]
my_data2 = [[2,4,4,5,6,7],[2,4,4,5,6,7]]

1.新建数组：多个函数

my_arr1 = np.array(my_data, dtype = np.int32)  
c_arr1 = my_arr.astype(np.float64)
 
my_arr2 = np.array(my_data2)    列表转数组
 
>>>array([[2,4,4,5,6,7],
          [2,4,4,5,6,7]])  
          
my_arr2.shape          
my_arr2.ndim  维度的判断  

([[[1, 1, 1, 1],
   [1, 1, 1, 1],
   [1, 1, 1, 1]],
  
  [[1, 1, 1, 1],
   [1, 1, 1, 1],
   [1, 1, 1, 1]]])  
   
np.zeros(10) 
np.zeros((3,5))   注意括号
np.ones(10)
np.aranges(10).reshape((3,3))
np.full(10)
np.eye(10)   单位矩阵

2.数组运算：不用编写循环即可对数据执行批量运算
不同大小的数组之间的运算叫做广播（broadcasting）

四则运算 / 切片
跟列表最重要的区别在于，数组切片是原始数组的视图。
这意味着数据不会被复制，视图上的任何修改都会直接反映到源数组上。

注意不同维度数组的切片索引  arr2d[:2, 1:]

布尔型索引

花式索引 (fancy indexing)
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
    
数组转置和轴对换：
arr.T
np.dot(arr,arr.T) 矩阵内积

通用函数：- 
np.sqrt(arr)  平方根      
np.exp(arr)   e的x次方
np.maximum(arr1, arr2)

remainder, whole_part = np.modf(arr)
divmod(py内置函数,返回整除和余数)

3.使用数组处理数据
用数组表达式代替循环的做法，通常被称为矢量化




数组是以未压缩的原始二进制格式保存在扩展名为.npy的文件中
np.save和np.load是读写磁盘数组数据的两个主要函数


x.dot(y)等价于np.dot(x, y)