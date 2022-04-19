import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [0, 1, 4, 9, 16, 25, 36, 49]
y1 = [0, 1, 8, 27, 64, 75, 216, 343]

plt.title('numbers squares')
plt.xlabel('numbers')
plt.ylabel('squares')
plt.grid()

plt.plot(x, y, y1,
         linewidth=4,
         linestyle='dashed')
plt.show()


