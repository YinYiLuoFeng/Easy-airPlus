# Easy-airPlus
本代码修改自airPLS项目（https://github.com/zmzhang/airPLS） ，用于处理拉曼光谱数据并输出相应图片。

如果用于其他光谱，注意修改图片坐标标题 `plt.xlabel、plt.xlabel` ，支持latex语法。

图片可通过修改 `plt.savefig` 修改格式。

可根据处理结果通过调节 `airPLS` 中的 `lambda_` 、 `porder=1` 、 `itermax` 参数优化结果。

提供简陋的平滑功能，使用 `Savitzky_Golay`算法滤波，强度可通过 `y1 = scipy.signal.savgol_filter(y1, 21, 3)`中的数值进行调节。

使用前请先在'元数据'文件夹中放置数据，支持csv和txt格式。具体请参考示例数据格式。
