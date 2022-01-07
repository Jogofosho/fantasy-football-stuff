"""
Stats provided by NFL Fantasy
Week 17, Top 10 RBs vs Projected Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([31.50,28.10,24.20,23.00,22.70,22.60,21.30,20.00,19.20,19.10])
proj_points = np.array([12.51,15.05,11.79,11.34,8.90,9.68,7.26,12.16,11.56,14.65])
players = np.array(["R. Penny\n(SEA)","N. Harris\n(PIT)","D. Williams\n(KC)","D. Singletary\n(BUF)",
                    "R. Stevenson\n(NE)","B. Scott\n(PHI)","A. Dillon\n(GB)","E. Mitchell\n(SF)",
                    "D. Foreman\n(TEN)","D. Montgomery\n(CHI)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 17, Top 10 RBs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()
