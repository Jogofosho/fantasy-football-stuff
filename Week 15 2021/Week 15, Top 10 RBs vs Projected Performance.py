"""
Stats provided by NFL Fantasy
Week 15, Top 10 RBs vs Projected Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([25.20,23.00,18.90,16.30,16.20,16.10,15.80,15.60,15.50,14.70])
proj_points = np.array([5.71,16.84,10.87,15.10,15.48,10.11,16.57,10.12,14.62,11.52])
players = np.array(["D. Johnson\n(MIA)","J. Taylor\n(IND)","J. Wilson\n(SF)","J. Robinson\n(JAX)",
                    "A. Ekeler\n(LAC)","D. Singletary\n(BUF)","N. Chubb\n(CLE)","M. Sanders\n(PHI)",
                    "A. Gibson\n(WAS)","E. Elliott\n(DAL)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 15, Top 10 RBs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()

