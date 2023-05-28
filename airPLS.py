import numpy as np
from matplotlib import pyplot as plt
from scipy.sparse import csc_matrix, eye, diags
from scipy.sparse.linalg import spsolve
from pandas import read_csv
import os
import matplotlib.pyplot as pl


def WhittakerSmooth(x, w, lambda_, differences=1):
    X = np.matrix(x)
    m = X.size
    E = eye(m, format='csc')
    for i in range(differences):
        E = E[1:] - E[:-1]
    W = diags(w, 0, shape=(m, m))
    A = csc_matrix(W + (lambda_ * E.T * E))
    B = csc_matrix(W * X.T)
    background = spsolve(A, B)
    return np.array(background)


def airPLS(x, lambda_=100, porder=1, itermax=15):
    m = x.shape[0]
    w = np.ones(m)
    for i in range(1, itermax + 1):
        z = WhittakerSmooth(x, w, lambda_, porder)
        d = x - z
        dssn = np.abs(d[d < 0].sum())
        if dssn < 0.001 * (abs(x)).sum() or i == itermax:
            if i == itermax: print('WARING max iteration reached!')
            break
        w[d >= 0] = 0  # d>0 means that this point is part of a peak, so its weight is set to 0 in order to ignore it
        w[d < 0] = np.exp(i * np.abs(d[d < 0]) / dssn)
        w[0] = np.exp(i * (d[d < 0]).max() / dssn)
        w[-1] = w[0]
    return z


if __name__ == '__main__':

    print("本代码修改自airPLS项目（https://github.com/zmzhang/airPLS），用于处理拉曼光谱数据并输出相应图片。\n"
          "如果用于其他光谱，注意修改图片坐标标题<plt.xlabel、plt.xlabel>，支持latex语法。\n"
          "图片可通过修改<plt.savefig>修改格式。\n"
          "可根据处理结果通过调节<airPLS>中的lambda_、porder=1、itermax参数优化结果.\n"
          "使用前请先在'元数据'文件夹中放置数据，支持csv和txt格式。\n")

    i = 0
    path1 = "元数据"  # 可自行修改
    isExists = os.path.exists(path1)
    if not isExists:
        os.makedirs(path1)
        print(path1 + ' 不存在，现已创建成功，请放入数据后重新打开程序')
        quit()
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path1 + ' 目录已存在')
        size1 = 0
        for root, dirs, files in os.walk(path1):
            for filename in files:
                # 获取文件大小用 os.path.getsize
                size1 += os.path.getsize(os.path.join(root, filename))
            if size1 == 0:
                print("目录为空，请放入数据")
                quit()

    path2 = "处理后数据"  # 可自行修改
    isExists = os.path.exists(path2)
    # 判断结果
    if not isExists:
        os.makedirs(path2)
        print(path2 + ' 不存在，已创建')
    else:
        # 如果目录存在则不创建，并判断目录是否为空
        size = 0
        for root, dirs, files in os.walk(path2):
            for filename in files:
                # 获取文件大小用 os.path.getsize
                size += os.path.getsize(os.path.join(root, filename))
            if size == 0:
                print(path2 + ' 目录已存在')
            else:
                print(path2 + " 目录不为空，为防止已数据丢失，请清空目录！\n")
                quit()

    for filename in os.listdir(path1):
        if filename.endswith(".CSV") or filename.endswith(".csv") or filename.endswith(".txt") or filename.endswith(
                ".TXT"):  # 判断文件格式，其余文本文件亦可加入
            X1 = read_csv(path1 + "/" + filename, usecols=[0])  # 读取x坐标
            Y1 = read_csv(path1 + "/" + filename, usecols=[1])  # 读取y坐标
            x = X1.values.T  # 将DataFrame转换为 numpy() 数组，并将列向量转化为行向量
            y = Y1.values.T
            x1 = x[0, :]  # 将二位数组转化为一维数组
            y1 = y[0, :]
            x = x1
            c1 = y1 - airPLS(y1)  # 减去基线
            print("Plotting " + filename)
            font_dict = {'family': 'Times New Roman',
                         'weight': 'normal',
                         'size': 18}
            # plt.xlabel(filename[0:len(filename) - 4], fontdict=font_dict) #标题，可自行修改
            fig = plt.figure()  # 生成画布
            ax = plt.axes()
            ax.plot(x, y1, '-k')  # 原数据
            ax.plot(x, c1, '-r')  # 处理后数据
            plt.savefig(path2 + "/" + "处理后-" + filename[0:len(filename) - 4] + ".svg",
                        dpi=300, bbox_inches='tight',
                        transparent=True,
                        )  # 输出图片，transparent为背景透明
            plt.xlabel(r"Raman shift" + "$(cm^{-1} )$")  # x轴标题
            plt.ylabel("Raman intensity")  # y轴标题
            pl.show()  # 展示图片，此命令需要在所以plt函数最后
            print(filename + ' Done!\n')
            stack_xy = np.column_stack((x, y1))  # 合并处理后数据
            np.savetxt(path2 + "/" + "处理后-" + filename, stack_xy, delimiter=",")  # 输出处理后数据，格式为csv
            i = i + 1
    print("共 " + str(i) + " 组数据处理完成")
