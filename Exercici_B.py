import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arxiu = pd.read_csv('List of cities proper by population density11.csv', sep=',')
arxiu = arxiu.head(10)
arxiu2 = arxiu[['Population', 'Density KM2', 'Density M2']].apply(lambda x: x.str.replace(',', ''))

primer = arxiu[['City', 'Population']]
segon = arxiu[['City', 'Density KM2']]
tercer = arxiu[['City', 'Density M2']]
print(primer)
print("=====================================")
print(segon)
print("=====================================")
print(tercer)

def grafic(arxiu,arxiu2):
    plt.figure(num='Population')
    plt.pie(arxiu2['Population'], labels=arxiu['City'], autopct='%1.1f%%', startangle=90)
    plt.title('Population')
    plt.figure(num='Density KM2')
    plt.pie(arxiu2['Density KM2'], labels=arxiu['City'], autopct='%1.1f%%', startangle=90)
    plt.title('Density KM2')
    plt.figure(num='Density M2')
    plt.pie(arxiu2['Density M2'], labels=arxiu['City'], autopct='%1.1f%%', startangle=90)
    plt.title('Density M2')
    plt.show()

def main():
    grafic(arxiu,arxiu2)

if __name__ == '__main__':
    main()
