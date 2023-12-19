import matplotlib.pyplot as plt
import numpy as np

lang = ["Python", "C", "C++", "Java", "JavaScript"]
popularity_2022 = [76, 82, 85, 89, 86]
popularity_2023 = [92, 83, 87, 80, 84]
popularity_2024 = [60, 90, 95, 87, 80]

width = 0.3

p1 = np.arange(len(popularity_2023))
p2 = [j+width for j in p1]
p3 = [j+2*width for j in p1]

plt.xlabel("Language", fontsize=18)
plt.ylabel("Popularity", fontsize=18)
plt.title("Languages and their popularity", fontsize=20)

plt.bar(p1, popularity_2022, width, color="r", label="2022")
plt.bar(p2, popularity_2023, width, color="y", label="2023")
plt.bar(p3, popularity_2024, width, color="g", label="2024")

plt.xticks(p1+width, lang, rotation=90)
plt.legend()
plt.show()