"""
Stats provided by NFL Fantasy
Week 14, Top 10 RBs vs Projected Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(14, 6), dpi=80)

actual_points = np.array([34.70,29.00,26.30,23.90,23.10,22.50,21.20,20.80,20.00,17.70])
proj_points = np.array([16.40,14.08,4.85,15.33,9.82,15.49,16.18,14.52,11.63,11.58])
players = np.array(["D. Cook\n(MIN)","J. Conner\n(ARI)","R. Penny\n(SEA)","N. Harris\n(PIT))",
                    "M. Gordon\n(DEN)","A. Kamara\n(NO)","L. Fournette\n(TB)","J. Williams\n(DEN)",
                    "A. Jones\n(GB)","C. Edwards-Helaire\n(KC)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 14, Top 10 RBs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()





