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

if __name__ == '__main__':
    basic()
