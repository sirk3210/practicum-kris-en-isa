import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.array(pd.read_excel(r'c:\Users\Lenovo\Documents\uni\1e jaar\inleidend practicum\quarter 2\druk ballon\druk_metting.xlsx', header=None).transpose())

temps = data[1, :]
hoogtes = data[0, :]/10



#start 280ml

diam_beker = 7.66 # cm
diam_deksel = 6.77 # cm
opp_water = 1/4 * np.pi * (diam_beker**2 - diam_deksel**2) #cm2

volumes = (np.asarray(hoogtes) - hoogtes[0]) * opp_water
temps_abs = np.asarray(temps) + 273
coef = np.polyfit(temps_abs, volumes, 1)
func = np.poly1d(coef)
print(func(0))
plt.plot(temps_abs, volumes, 'ob')
plt.plot(temps_abs, func(temps_abs), '--r')
plt.xlabel('Temperature [K]')
plt.ylabel('Volume [ccm]')
plt.show()

temps = data[3,:][0:8]
hoogtes = data[2,:][0:8]/10
print(temps)
print(hoogtes)

volumes = (np.asarray(hoogtes) - hoogtes[0]) * opp_water
temps_abs = np.asarray(temps) + 273
coef = np.polyfit(temps_abs, volumes, 1)
func = np.poly1d(coef)
print(func(0))
plt.plot(temps_abs, volumes, 'ob')
plt.plot(temps_abs, func(temps_abs), '--r')
plt.xlabel('Temperature [K]')
plt.ylabel('Volume [ccm]')
plt.show()