> NumPy是代表“**Numerical Python**”的Python包。 它是一个由多维数组对象和一组处理数组的例程组成的库。
## Numpy操作
使用NumPy，开发人员可以执行以下操作

- 数组的数学和逻辑运算。
- 傅立叶变换和形状操作的例程。
- 与线性代数有关的操作，NumPy具有用于线性代数和随机数生成的内置函数。

## NumPy - MatLab的替代品
NumPy通常与`SciPy(Scientific Python)`和`Mat-plotlib(绘图库)`等软件包一起使用。 这种组合广泛用于替代技术计算的流行平台MatLab。 然而，MatLab的Python替代品现在被视为更现代和完整的编程语言。

### ndarray对象
NumPy中定义的最重要的对象是名为`ndarray`的N维数组类型。 它描述了相同类型的项目的集合。 可以使用从零开始的索引来访问集合中的项目。 `ndarray`中的每个项目在内存中占用相同的块大小。`ndarray`中的每个元素都是数据类型对象(称为`dtype`)的对象。 从`ndarray`对象中提取的任何项目(通过切片)由数组标量类型之一的Python对象表示。