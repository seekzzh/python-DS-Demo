# 热图包含代表要绘制的每个值的相同颜色的各种阴影的值。 通常图表的较暗阴影表示比较浅的阴影更高的值。 对于非常不同的值，也可以使用完全不同的颜色。
# 以下示例是映射到图表的索引和列的值的二维图。

from pandas import DataFrame
import matplotlib.pyplot as plt

data = [{2, 3, 4, 1}, {6, 3, 5, 2}, {6, 3, 5, 4}, {3, 7, 5, 4}, {2, 8, 1, 5}]
Index = ['I1', 'I2', 'I3', 'I4', 'I5']
Cols = ['C1', 'C2', 'C3', 'C4']
df = DataFrame(data, index=Index, columns=Cols)

plt.pcolor(df)
plt.show()

# 执行上面示例代码，得到热图
