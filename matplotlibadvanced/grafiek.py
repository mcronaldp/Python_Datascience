from matplotlib import pyplot as plt

# print(plt.style.available) Als je dit runt zie je welke stylen er beschikbaar zijn. A
# ls je deze gebruikt hoef je de standaard line diktes en kleuren niet te gebruiken want in de style zit een eigen kleuren pakket.
plt.style.use('fivethirtyeight')
ages_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496, 42000,46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# Plot data
plt.plot(ages_x, dev_y, color= '#5a7d9a', linewidth='3', linestyle='--', marker='.',label = 'All Devs') # Je plot de data van agex_x in de x as en de data van dev_y in de y as. Kleur zijn de hexadecimale kleur codes

py_dev_y =[45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, color='#444444', marker='.', label= 'Python') # Je plot de data van agex_x in de x as en de data van py_dev_y in de y as.


js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y, color = '#adad3b', label= 'Javascript')
plt.xlabel('Ages') # Naam voor X as
plt.ylabel('Median Salary (USD)') # Naam voor Y as
plt.title('Median Salary (USD) by Age') #Titel naam

plt.legend()
plt.grid(True) # zet een grid achter de grafiek.
plt.tight_layout() # zorgt er voor dat de layout beter staat.
plt.savefig('plot.png') # Hier kun je een path opgeven waar hij de foto op slaat.
plt.show() # Je toont de grafiek