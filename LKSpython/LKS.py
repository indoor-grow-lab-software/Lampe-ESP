import LED
def init_LED(Namen, Farben, Frequenzen, Helligkeiten, value):
    LEDs = [LED.LED(Namen[i], Farben[i], Frequenzen[i], Helligkeiten[i]) for i in range(value)]
    print(LEDs)
    return LEDs
Namen = ["eins", "zwei", "drei"]
Farben = ["rot", "blau", "UV"]
Frequenzen = [700, 1200, 1600]
Helligkeit = [1000, 2000, 4000]
A = init_LED(Namen, Farben, Frequenzen, Helligkeit, 3)
for i in A:
    print(i.get_parameter(i))
