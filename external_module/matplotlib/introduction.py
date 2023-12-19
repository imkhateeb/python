import matplotlib.pyplot as plt
import numpy as np

years = [2006 + x for x in range(16)]
weights = [24, 23, 26, 30, 34, 32, 35, 40, 38, 39, 45, 32, 43, 42, 45, 46]
# plt.plot(years, weights, c='red', lw=3, linestyle='--' )


lang = ["C++", "C#", "Python", "JavaScript", "Java", "Go"]
votes = [23, 34, 89, 101, 43, 21]
# plt.bar(lang, votes, color='red', width=0.5, edgecolor='yellow', lw=2)


ages = np.random.normal(20, 1.5, 1000)
# plt.hist(ages, bins=20, color='red', cumulative=True)


plt.pie(votes, labels=lang, autopct="%.f%%", pctdistance=0.8)
plt.show()