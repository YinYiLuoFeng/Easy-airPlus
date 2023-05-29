# Easy-airPlus
## 说明
本代码修改自airPLS项目（https://github.com/zmzhang/airPLS） ，用于处理拉曼光谱数据并输出相应图片。

鉴于原项目对科研小白不够友好，所以有了这个项目。

如果用于其他光谱，注意修改图片坐标标题 `plt.xlabel、plt.ylabel` ，支持Latex语法。

图片可通过修改 `plt.savefig` 修改输出格式，如`.svg` `.png` `.jpeg`。

核心函数为`airPLS`,可根据处理结果通过调节以下参数：  
`lambda_` 、 `porder=1` 、 `itermax` 

提供简陋的平滑功能，使用 `Savitzky_Golay`算法滤波，以下为参数：    
`window_length`即窗口长度取值为奇数且不能超过`len(x)`。越大，则平滑效果越明显；越小，则更贴近原始曲线。  
`polyorder`为多项式拟合的阶数。越小，则平滑效果越明显；越大，则更贴近原始曲线。

使用前请先在`元数据`文件夹中放置数据，支持csv和txt格式，请参照示例安排数据。  
具体请参考示例数据格式。为了确保数据安全，`处理后数据`文件夹只能为空，请及时迁移数据。

## 示例
示例1  
![Image text](https://github.com/YinYiLuoFeng/Easy-airPlus/blob/master/%E7%A4%BA%E4%BE%8B%E6%95%B0%E6%8D%AE/%E7%A4%BA%E4%BE%8B1.svg)  

示例2  
![Image text](https://github.com/YinYiLuoFeng/Easy-airPlus/blob/master/%E7%A4%BA%E4%BE%8B%E6%95%B0%E6%8D%AE/%E7%A4%BA%E4%BE%8B2.svg)  


