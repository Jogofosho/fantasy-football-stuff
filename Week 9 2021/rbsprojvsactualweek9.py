import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

figure(figsize=(12, 6), dpi=80)

actualPoints = [18.40,9.70,33.00,12.60,15.30,5.30,29.30,13.70,9.10]
projPoints = [19.30,18.36,18.03,17.75,17.63,15.57,15.01,14.77,13.99]

players = ['A. Kamara', 'A. Ekeler', 'J. Taylor', 'C. McCaffrey', 'N. Harris', 'A. Jones', 'N. Chubb', 'D. Cook', 'M. Carter']

plt.plot(players, actualPoints, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(projPoints, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 9, Top 10 Projected RBs vs Actual")
plt.legend()
plt.grid()
plt.show()
