#Die Klasse LED erstellt.
class LED:

    #Ein Objekt der Klasse wird mit den Parametern Name, Farbe, Frequenz und Helligkeit intialisiert.
    def __init__(self, name, farbe, frequenz, helligkeit):
        self.name = name
        self.farbe = farbe
        self.frequenz = frequenz
        self.helligkeit = helligkeit

    def get_parameter(self): 
        return self.name, self.farbe, self.frequenz, self.helligkeit


def init_LED(Namen, Farben, Frequenzen, Helligkeiten, value):
    LEDs = []
    for i in range(value-1):
        LED(Namen[i], Farben[i], Frequenzen[i], Helligkeiten[i])
        LEDs.append()

    print(LEDs)
        
    
    
