import matplotlib.pyplot as plt
import numpy as np

pie_perc = [20, 20, 20, 40]
pie_lang = ["Python", "C", "C++", "JavaScript"]

explode = [0.1, 0.0, 0.0, 0.0]


plt.pie(pie_perc, labels = pie_lang, explode=explode, autopct="%0.2f%%", shadow=True, radius=1.3)

plt.show()