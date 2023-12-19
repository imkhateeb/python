import matplotlib.pyplot as plt

dna = [ 12, 34, 30, 80, 32 ]
constituents = [40, 50, 60, 70, 56]
patients = [16, 43, 54, 23, 5]

color = ['r', 'g', 'b', 'y', 'r']
size = [100, 400, 300, 200, 100]
# plt.scatter(dna, constituents, c=color, s=size, alpha=0.5, marker="*", edgecolor='g', cmap="BrBG")
plt.scatter(dna, constituents, s=size, cmap="viridis")
plt.scatter(dna, patients, s=size, cmap="viridis")

color_bar = plt.colorbar()
color_bar.set_label("ColorBar", fontsize=15)

# We can add xlabel, ylabel and title here also
plt.show()