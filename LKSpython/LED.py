# Die Klasse LED erstellt.
class LED:

    # Ein Objekt der Klasse wird mit den Parametern Name, Farbe, Frequenz und Helligkeit intialisiert.
    def __init__(self, name, farbe, frequenz, helligkeit):
        self.name = name
        self.farbe = farbe
        self.frequenz = frequenz
        self.helligkeit = helligkeit

    def get_parameter(self, objekt):
        return {objekt.name: "Name", objekt.farbe : "Farbe", objekt.frequenz : "Frequenz", objekt.helligkeit : "Helligkeit"}






