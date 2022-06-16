from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

x = [86.06, 66.40, 88.61, 83.24, 65.87]
y = [42559000, 54243000, 35174000, 35255000, 38079000]

xRs = x.copy()
yRs = y.copy()
xRs = np.reshape(x, (-1, 1))
yRs = np.reshape(y, (-1, 1))

line_fitter = LinearRegression()
line_fitter.fit(xRs, yRs)
best_fit = line_fitter.predict(xRs)

plt.plot(x, y, "o")
plt.plot(x, best_fit, "--")
plt.xlabel("Enterprise Value/EBITDA")
plt.ylabel("Gross Profit")
plt.title("EV/EBITDA compared to Gross Profit in $AAPL")
plt.show()