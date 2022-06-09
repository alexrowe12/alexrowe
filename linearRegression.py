# Upper Confidence Interval for sample cancer data set, X axis
upperConfidenceInterval = [144.2, 155.1, 194.7, 165.5, 141.4, 134.9, 138.5, 138.3, 144.4, 130.4, 121, 124.1, 112.6, 119.9, 122.3, 120.6, 116.9, 141.6, 113.7, 110.3]
# Average Deaths Per Year in same data set, y axis
averageDeaths = [43, 18, 5, 8, 19, 22, 16, 14, 9, 17, 33, 25, 47, 21, 17, 17, 22, 6, 29, 39]

import matplotlib as plt

plt.plot(upperConfidenceInterval, averageDeaths)
plt.xlabel("Upper Confidence Interval")
plt.ylabel("Lower Confidence Interval")
plt.show()
