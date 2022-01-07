"""
Stats provided by NFL Fantasy
Week 17, Top 10 WRs vs Projected Performance
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actual_points = np.array([50.10,31.40,27.90,25.10,21.70,18.50,18.20,17.30,17.10,17.10])
proj_points = np.array([11.34,10.82,10.08,15.68,7.94,17.17,0.83,9.08,2.31,13.13])
players = np.array(["J. Chase\n(CIN)","A. St. Brown\n(DET)","D. Metcalf\n(SEA)","D. Adams\n(GB)",
                    "B. Berrios\n(NYJ)","C. Kupp\n(LAR)","K. Wilkerson\n(NE)","J. Meyers\n(NE)",
                    "C. Grayson\n(TB)","H. Renfrow\n(LV)"])

plt.plot(players, actual_points, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(proj_points, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 17, Top 10 WRs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()