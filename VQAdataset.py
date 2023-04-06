import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import xlrd
import seaborn as sns
from scipy.stats import norm

def main():
    data = xlrd.open_workbook("LIVE-Qualcomm_mos.xls")
    table1 = data.sheet_by_name('Sheet2')

    row1 = table1.row_values(0) #根据索引读取一行的数据，即表头
    for i in range(len(row1)):
        if row1[i] == 'flickr_id':
            oneindex1 = i
        elif row1[i] == 'mos':
            oneindex2 = i

#获取两列数据
    id = table1.col_values(oneindex1,1)
    mos = table1.col_values(oneindex2,1)

#计算mos的均值和方差
    mu = np.mean(mos)#均值
    sigma = np.std(mos) #方差
    mu,sigma

#横坐标
    Mos = list(sorted(mos))

    print("*********************开始绘图********************")
    #绘制数据集的正态分布曲线
    # x = np.arange(1,5,0.01)
    # y = mlab.normpdf(x, mu, sigma)
    # plt.plot(x, y, 'r--')  # 绘制y的曲线

    # #绘制数据集的直方图
    weights = np.ones_like(mos)/float(len(mos))
    sns.distplot(mos,fit=norm,bins=50,kde=True)#kide拟合的曲线不是正态分布的，而是更贴合数据的实际分布情况
    #添加fit=norm，即把正态分布的曲线也加到图中
    #plt.hist(mos,bins =100,density=1, facecolor='blue', alpha=0.5)
    plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'. \
               format(mu, sigma)], loc='best') #添加图例
    plt.xlabel('MOS')
    plt.ylabel('Number of scores')
    plt.title('LIVE-Qualcomm')
    plt.show()

if __name__ == '__main__':
    main()