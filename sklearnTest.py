from sklearn.linear_model import LinearRegression
import sklearn.linear_model
import matplotlib.pyplot as plt
import numpy as np

# Upper Confidence Interval for sample cancer data set, X axis (edited)
x = [144, 155, 165, 141, 134, 138, 138, 144, 130, 121, 124, 112, 119, 122, 120, 116, 141, 113, 110]
# Average Deaths Per Year in same data set, y axis (edited)
y = [43, 18, 5, 8, 19, 22, 16, 14, 9, 17, 33, 25, 21, 17, 17, 22, 6, 29, 39]
xRs = x.copy()
yRs = y.copy()

xRs = np.reshape(xRs, (-1, 1))
yRs = np.reshape(yRs, (-1, 1))
line_fitter = LinearRegression()
line_fitter.fit(xRs, yRs)
best_fit = line_fitter.predict(xRs)

print (line_fitter.intercept_)

plt.plot(x, y, "o")
plt.plot(x, best_fit, "-")
plt.xlabel("Upper Confidence Interval")
plt.ylabel("Average Deaths")
plt.show()