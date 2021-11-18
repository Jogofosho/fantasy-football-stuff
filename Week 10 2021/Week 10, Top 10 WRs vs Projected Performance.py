# Stats provided by NFL Fantasy
# Week 10, Top 10 WRs vs Projected Performance

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80)

actualPoints = np.array([27.80,26.20,25.60,24.00,22.10,20.60,18.40,17.70,16.30,14.10])
projPoints = np.array([15.41,14.85,12.30,14.00,5.54,11.24,14.30,18.32,6.80,10.73])
players = np.array(["D. Samuel\n(SF)","S. Diggs\n(BUF)","C. Lamb\n(DAL)","T. Hill\n(KC)",
                    "K. Bourne\n(NE)","D. Smith\n(PHI)","J. Jefferson\n(MIN)","C. Kupp\n(LAR)",
                    "B. Edwards\n(LV)","H. Renfrow\n(LV)"])

plt.plot(players, actualPoints, 'o', c = 'g', label = 'Actual Points', ms = 6)
plt.plot(projPoints, 'o', c = 'r', label = 'Projected Points', ms = 6)
plt.title("Week 10, Top 10 WRs vs Projected Performance")
plt.legend()
plt.grid()
plt.show()




