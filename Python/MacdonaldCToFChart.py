#C9/5+32.000=F
'''
print("""
Celsius   Fahrenheit    |    Fahrenheit      Celsius
0             32.000    |    20               -6.667
2             35.600    |    25               -3.889
...
98           208.400    |    265             129.444
100          212.000    |    270             132.222
""")
'''

leftc2f=[]
rightc2f=[]
for i in range(0,102,2):        #makes the interval go up by 2
    leftc2f.append(i)
    rightc2f.append(i*9/5+32)           #calculates celsius to fahrenheit

leftf2c=[]
rightf2c=[]
for i in range(20,275,5):           #this makes the interval go up by 5
    leftf2c.append(i)
    rightf2c.append(((i-32)*(5))/9)         #calculates fahrenheit to celsius

print('Celsius\tFahrenheit\t|\tFahrenheit\tCelsius')        #puts it into a table
for i in range(0,51):
    print('%.1d\t%.3f\t\t|\t%.1d\t\t%.3f'%(leftc2f[i],rightc2f[i],leftf2c[i],rightf2c[i]))      #puts 3 decimal places in the print out
   


'''
# ch_4_jrn8_ex6.py
# Celsius to Fahrenheit Table

# Print the table headings.             #https://gist.github.com/AnMcCbusiness/ee0d8dc9a1b0f1a823164f10c4053305
print('Farenheit\t Celsius')
print('------------------------')

# Print the degree comparisons 0-20 Celsius to Farenheit
for celsius in range(0, 21):
    farenheit = 9 / 5 * celsius + 32
    print(format(farenheit, '.1f'), '\t\t', celsius)
'''