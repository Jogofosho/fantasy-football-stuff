"""
Stats provided by NFL Fantasy
Week 14, Top 10 Projected WRs vs Actual Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([17.00,24.80,29.10,12.40,12.80,10.90,9.60,22.20,15.50,9.10])
proj_points = np.array([19.09,17.15,15.97,15.51,15.14,14.60,14.26,13.79,13.40,12.59])
players = np.array(["J. Jefferson\n(MIN)","C. Kupp\n(LAR)","D. Adams\n(GB)","D. Samuel\n(SF)",
                    "D. Johnson\n(PIT)","S. Diggs\n(BUF)","T. Hill\n(KC)","H. Renfrow\n(LV)",
                    "C. Godwin\n(TB)","M. Williams\n(LAC)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 14, Top 10 Projected WRs vs Actual Performance")
plt.legend()
plt.grid()
plt.show()


