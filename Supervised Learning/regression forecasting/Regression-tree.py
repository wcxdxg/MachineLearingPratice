# coding=utf-8
#导入美国波士顿地区房价 模板包
from sklearn.datasets import load_boston
#读取房价的数据存储在boston之中
boston = load_boston()
#输出数据描述
#print(boston.DESCR)

#进行必要的数据分割
#实验数据分割器
from sklearn.model_selection import train_test_split
#导入numpy命名为np
import numpy as np
xx = boston.data
#导入数据data
yy = boston.target
#导入属性target

x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state = 33,test_size = 0.25)

#分析回归目标的差异
print("The max target value is ",np.max(boston.target))
print("The min target value is ",np.min(boston.target))
print("The average target value is ",np.mean(boston.target))
#numpy中mean为平均值

#导入数据标准化模块
from sklearn.preprocessing import StandardScaler
#分别初始化对特征和目标值的标准化器
ss_x = StandardScaler()
ss_y = StandardScaler()

x_train = ss_x.fit_transform(x_train)
x_test = ss_x.transform(x_test)
y_train = ss_y.fit_transform(y_train.reshape(-1, 1))
y_test = ss_y.transform(y_test.reshape(-1, 1))

from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor()
dtr.fit(x_train,y_train)
dtr_y_predict = dtr.predict(x_test)

from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
print('R2 value of linear SVR is', dtr.score(x_test,y_test))
print('The mean squared error of linear SVR is',
      mean_squared_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(dtr_y_predict)))
print('The mean absolute error of linear SVR is',
      mean_absolute_error(ss_y.inverse_transform(y_test),ss_y.inverse_transform(dtr_y_predict)))