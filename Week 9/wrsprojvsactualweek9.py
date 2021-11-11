import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actualPoints = np.array([15.00,7.20,5.90,5.30,11.50,8.80,15.50,9.20,6.70,7.30])
projPoints = np.array([18.90,17.32,15.37,15.31,15.22,15.21,14.97,14.86,14.11,13.41])

players = np.array(["C. Kupp", "D. Adams", "J. Chase", "T. Hill", "S. Diggs", "D. Samuel",
           "J. Jefferson", "D. Johnson", "A.J. Brown", "C. Beasley"])

plt.plot(players, actualPoints, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(projPoints, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 9, Top 10 Projected WRs vs Actual")
plt.legend()
plt.grid()
plt.show()







