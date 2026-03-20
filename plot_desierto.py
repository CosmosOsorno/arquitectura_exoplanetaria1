import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cat_limpio.csv', header=None,names=['name','discoveryMethod','periodo_orbital','radio','masa'])
plt.scatter(df['masa'],df['periodo_orbital'],alpha=0.2)
plt.title('Periodo Orbital vs. Masa')
plt.xlabel('Masa [M$_\oplus$]')
plt.ylabel('Periodo Orbital')
plt.xscale('log')
plt.yscale('log')
plt.savefig('desierto.png')