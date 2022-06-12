# Upper Confidence Interval for sample cancer data set, X axis
upperConfidenceInterval = [144, 155, 194, 165, 141, 134, 138, 138, 144, 130, 121, 124, 112, 119, 122, 120, 116, 141, 113, 110]
# Average Deaths Per Year in same data set, y axis
averageDeaths = [43, 18, 5, 8, 19, 22, 16, 14, 9, 17, 33, 25, 47, 21, 17, 17, 22, 6, 29, 39]

import matplotlib.pyplot as plt
import numpy as np
import sklearn

def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')

def get_gradient_at_b(x, y, b, m):
  N = len(upperConfidenceInterval)
  diff = 0
  for i in range(N):
    x_val = upperConfidenceInterval[i]
    y_val = averageDeaths[i]
    diff += (y_val - ((m[i] * x_val) + b[i]))
  b_gradient = -(2/N) * diff  
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(upperConfidenceInterval)
  diff = 0
  for i in range(N):
      x_val = upperConfidenceInterval[i]
      y_val = averageDeaths[i]
      diff += x_val * (y_val - ((m[i] * x_val) + b[i]))
  m_gradient = -(2/N) * diff  
  return m_gradient

def step_gradient(x, y, b_current, m_current, learning_rate):
  b_gradient = get_gradient_at_b(x, y, b_current, m_current)
  m_gradient = get_gradient_at_m(x, y, b_current, m_current)
  b = b_current - (learning_rate * b_gradient)
  m = m_current - (learning_rate * m_gradient)
  return (b, m)

def gradient_descent(x, y, learning_rate, num_iterations):
  b = 0
  m = 0
  for i in range(num_iterations):
    b,m = step_gradient(b, m, x, y, learning_rate)
  return [b, m]

# current intercept guess:
b = 0
# current slope guess:
m = 0

# Call your function here to update b and m
b, m = gradient_descent(upperConfidenceInterval, averageDeaths, 0.01, 1000)
print(b, m)

plt.plot(upperConfidenceInterval, averageDeaths, "o")
plt.xlabel("Upper Confidence Interval")
plt.ylabel("Average Deaths per Year")
abline(b, m)
plt.show()
