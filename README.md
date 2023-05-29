# Easy-airPlus
本代码修改自airPLS项目（https://github.com/zmzhang/airPLS） ，用于处理拉曼光谱数据并输出相应图片。

鉴于原项目对科研小白不够友好，所以有了这个项目。

如果用于其他光谱，注意修改图片坐标标题 `plt.xlabel、plt.ylabel` ，支持latex语法。

图片可通过修改 `plt.savefig` 修改输出格式。

可根据处理结果通过调节 `airPLS` 中的 `lambda_` 、 `porder=1` 、 `itermax` 参数优化结果。

提供简陋的平滑功能，使用 `Savitzky_Golay`算法滤波。  
`window_length`即窗口长度取值为奇数且不能超过len(x)。它越大，则平滑效果越明显；越小，则更贴近原始曲线。  
`polyorder`为多项式拟合的阶数。它越小，则平滑效果越明显；越大，则更贴近原始曲线。

使用前请先在'元数据'文件夹中放置数据，支持csv和txt格式。具体请参考示例数据格式。
