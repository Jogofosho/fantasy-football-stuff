import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

figure(figsize=(10, 6), dpi=80)

actualPoints = [37.80, 33.00, 29.30, 25.50, 18.80, 18.40, 16.60, 16.50, 15.30]
projPoints = [10.86, 18.03, 15.01, 12.84, 6.20, 19.30, 11.51, 10.49, 11.39]

players = ['J. Conner', 'J. Taylor', 'N. Chubb', 'J. Mixon', 'N. Hines', 'A. Kamara', 'C. Patterson', 'M. Gordon', 'D. Freeman']

plt.plot(players, actualPoints, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(projPoints, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.legend()
plt.show()
