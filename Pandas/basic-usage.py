import pandas as pd
import numpy as np


def basic():
    """生成对象"""

    # 用值列表生成 Series (opens new window)时，Pandas 默认自动生成整数索引：
    series = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(series)
    # 用含日期时间索引与标签的 NumPy 数组生成 DataFrame
    dates = pd.date_range('20130101', periods=6)
    print(dates)

    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    # 用 Series 字典对象生成 DataFrame
    df2 = pd.DataFrame({
        'A': 1,
        'B': pd.Timestamp('20210306'),
        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'),
        'E': pd.Categorical(['james', 'wide', 'tomas', 'kobe'])
    })
    print(df2)
    # DataFrame 的列有不同数据类型
    print(df2.dtypes)

    """查看数据"""

    # 查看 DataFrame 头部和尾部数据
    print(df.head())

    print(df.last())

    print(df.tail(2))

    # 显示索引与列名
    print(df.index)

    print(df.columns)

    # 输出底层数据的 NumPy 对象。
    """
        注意，DataFrame (opens new window)的列由多种数据类型组成时，该操作耗费系统资源较大，这也是 Pandas 和 NumPy 的本质区别：
        NumPy 数组只有一种数据类型，DataFrame 每列的数据类型各不相同。
        调用 DataFrame.to_numpy() (opens new window)时，Pandas 查找支持 DataFrame 里所有数据类型的 NumPy 数据类型。
        还有一种数据类型是 object，可以把 DataFrame 列里的值强制转换为 Python 对象。
    """
    print(df.to_numpy())

if __name__ == '__main__':
    basic()
