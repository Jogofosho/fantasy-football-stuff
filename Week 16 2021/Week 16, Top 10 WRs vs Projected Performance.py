"""
Stats provided by NFL Fantasy
Week 16, Top 10 WRs vs Projected Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([37.40,28.40,26.00,23.90,23.60,22.50,21.50,20.20,18.00,18.00])
proj_points = np.array([12.64,15.31,12.69,2.07,14.40,5.27,11.94,12.20,9.45,11.61])
players = np.array(["T. Higgins\n(CIN)","D. Adams\n(GB)","A. Brown\n(TEN)","I. McKenzie\n(BUF)",
                    "D. Samuel\n(SF)","B. Pringle\n(KC)","A. St. Brown\n(DET)","J. Waddle\n(MIA)",
                    "A. Cooper\n(DAL)","S. Diggs\n(BUF)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 16, Top 10 WRs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()
