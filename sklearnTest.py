from sklearn.linear_model import LinearRegression as lr
import sklearn
import matplotlib.pyplot as plt
import numpy as np

# Upper Confidence Interval for sample cancer data set, X axis (edited)
x = [144, 155, 165, 141, 134, 138, 138, 144, 130, 121, 124, 112, 119, 122, 120, 116, 141, 113, 110]
# Average Deaths Per Year in same data set, y axis (edited)
y = [43, 18, 5, 8, 19, 22, 16, 14, 9, 17, 33, 25, 21, 17, 17, 22, 6, 29, 39]
xRs = x.copy()
yRs = y.copy()
y_predicted = []

xRs = np.reshape(yRs, (-1, 1))
dataSet = lr()
model = dataSet.fit(xRs, yRs)
for i in range(len(x)):
    y_predicted.append(dataSet.predict(xRs))


plt.plot(x, y, "o")
plt.xlabel("Upper Confidence Interval")
plt.ylabel("Average Deaths")
plt.show()

print (y_predicted)