import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

# Plotam toate valorile
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(data['Durata'], label='Durata')
plt.plot(data['Puls'], label='Puls')
plt.title('Toate valorile')
plt.legend()

# Plotam primele 4 valori
plt.subplot(3, 1, 2)
plt.plot(data['Durata'][:4], marker='o', linestyle='-', color='b', label='Durata')
plt.plot(data['Puls'][:4], marker='o', linestyle='-', color='r', label='Puls')
plt.title('Primele 4 valori')
plt.legend()

# Plotam ultimele 10 valori pentru coloanele 'Durata' și 'Puls'
plt.subplot(3, 1, 3)
plt.plot(data['Durata'][-10:], marker='o', linestyle='-', color='g', label='Durata')
plt.plot(data['Puls'][-10:], marker='o', linestyle='-', color='m', label='Puls')
plt.title('Ultimele 10 valori pentru Durata și Puls')
plt.legend()

# Afișam graficee
plt.tight_layout()
plt.show()