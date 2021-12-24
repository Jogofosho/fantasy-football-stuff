"""
Stats provided by NFL Fantasy
Week 15, Top 10 WRs vs Projected Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(14, 6), dpi=80)

actual_points = np.array([30.20,26.80,25.70,23.00,19.90,19.50,19.10,18.30,18.10,16.90])
proj_points = np.array([20.57,13.61,11.07,7.96,9.01,9.28,9.91,8.20,7.10,13.42])
players = np.array(["C. Kupp\n(LAR)","T. Hill\n(KC)","B. Cooks\n(HOU)","G. Davis\n(BUF)",
                    "C. Kirk\n(ARI)","A. St. Brown\n(DET)","R. Gage\n(ATL)","M. Valdez-Scantling\n(GB)",
                    "T. Boyd\n(CIN)","D. Samuel\n(SF)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 15, Top 10 WRs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()
