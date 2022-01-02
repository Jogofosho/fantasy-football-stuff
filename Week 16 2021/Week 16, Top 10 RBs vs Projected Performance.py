"""
Stats provided by NFL Fantasy
Week 16, Top 10 RBs vs Projected Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([30.20,28.50,28.30,27.90,25.90,22.70,20.10,20.00,19.50,16.70])
proj_points = np.array([10.06,12.57,11.16,11.21,15.21,12.33,13.36,10.91,11.38,11.78])
players = np.array(["J. Jackson\n(LAC)","J. Mixon\n(CIN)","D. Harris\n(NE)","R. Burkhead\n(HOU)",
                    "N. Chubb\n(CLE)","C. Edmonds\n(ARI)","D. Montgomery\n(CHI)","S. Michel\n(LAR)",
                    "R. Penny\n(SEA)","E. Elliott\n(DAL)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 16, Top 10 RBs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()