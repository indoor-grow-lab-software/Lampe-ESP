# Die Klasse LED erstellt.
class LED:


    def __init__(self, name, farbe, helligkeit):
        """

        :param name: Der Name der LED z.b. 1 oder eins
        :param farbe: Die Farbe der LED
        :param helligkeit: Die Helligkeit der LED
        """

        self.name = name
        self.farbe = farbe
        self.helligkeit = helligkeit

    def get(self, objekt):
        """

        :param objekt: Eine LED
        :return: die aktuellen Parameter der LED
        """
        #Die aktuellen Werte einer LED werden in Form eine dictionarys zurück gegeben.
        return {objekt.name: "Name", objekt.farbe : "Farbe", objekt.helligkeit : "Helligkeit"}

#    def update(self):







