import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cat_limpio.csv', header=None,names=['name','discoveryMethod','periodo_orbital','radio','masa'])
df['densidad'] = 5.51* df['masa']/(df['radio']**3)
sc = plt.scatter(df['radio'], df['masa'], c=df['densidad'],cmap='viridis')
plt.title('Masa vs. Radio')
plt.xlabel('Radio [R$_\oplus$]')
plt.ylabel('Masa [M$_\oplus$]')
plt.xscale('log')
plt.yscale('log')
cbar = plt.colorbar(sc)
cbar.set_label('Densidad')
plt.savefig('masa_radio.png')
