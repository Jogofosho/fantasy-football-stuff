"""
Stats provided by NFL Fantasy
Week 15, Top 10 Projected WRs vs Actual Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([30.20,12.70,13.40,7.30,4.70,26.80,7.90,16.90,11.50,3.30])
proj_points = np.array([20.57,20.18,18.45,14.80,14.65,13.61,13.51,13.42,13.05,12.72])
players = np.array(["C. Kupp\n(LAR)","J. Jefferson\n(MIN)","D. Adams\n(GB)","D. Johnson\n(PIT)",
                    "H. Renfrow\n(LV)","T. Hill\n(KC)","C. Godwin\n(TB)","D. Samuel\n(SF)",
                    "S. Diggs\n(BUF)","T. Higgins\n(CIN)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 15, Top 10 Projected WRs vs Actual Performance")
plt.legend()
plt.grid()
plt.show()