#Convert Fahrenheit to Celsius
print("Fahrenheit to Celsius converter")
fahrreq = input("temperature in fahrenheit? ")
try:
    fahr = float(fahrreq)
except:
    fahr = -1

if fahr == -1:
    print("error, please enter value as a number")
    exit()

else:
    cel = (fahr - 32) * 5/9
print("temperature is " , cel ,"degrees celsius.")

#Convert Celsius to Fahrenheit
print("Celsius to Fahrenheit converter")
celreq = input("temperature in celsius? ")
try:
    cel = float(celreq)
except:
    cel = -1
if cel == -1:
    print("error, please enter value as a number")
    exit()

else:
    fahrr = (cel * 9/5) + 32
print('Temperature in Celsius is', fahrr)