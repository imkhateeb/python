import matplotlib.pyplot as plt
import numpy as np

month = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
high = [32, 32, 33, 33, 32, 30, 30, 30, 30, 30, 31, 31]
low = [23, 23, 24, 25, 25, 24, 24, 24, 24, 24, 23, 22]

width = 0.4
p1 = np.arange(len(month))
p2 = [(int(i)+width) for i in range(len(month))]


plt.bar(p1, high, width, label="high")
plt.bar(p2, low, width, label="low")
plt.xticks(p1 + width/2, month, rotation=90)
plt.legend()
plt.show()