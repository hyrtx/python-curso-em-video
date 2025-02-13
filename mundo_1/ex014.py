'''
Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
'''

temp_celsius = float(input("Informe a temperatura em °C: "))
temp_fahrenheit = temp_celsius * 1.8 + 32

print(f"A temperatura de {temp_celsius}°C corresponde a {temp_fahrenheit}°F.")