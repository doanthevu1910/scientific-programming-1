import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('CarRideData.csv', sep=',')

df_1 = df[df.speed > 50]

plt.plot(df_1.lat, df_1.long, 'green')

df_2 = df[df.speed < 50]

plt.plot(df_2.lat, df_2.long, 'red')

plt.show()
