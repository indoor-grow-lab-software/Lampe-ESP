# Die Klasse LED erstellt.
class LED:


    def __init__(self, name, farbe, frequenz, helligkeit):
        """

        :param name: Der Name der LED z.b. 1 oder eins
        :param farbe: Die Farbe der LED
        :param frequenz: Die Frequenz der LED
        :param helligkeit: Die Helligkeit der LED
        """

        self.name = name
        self.farbe = farbe
        self.frequenz = frequenz
        self.helligkeit = helligkeit

    def get_LED(self, objekt):
        """

        :param objekt: Eine LED
        :return: die aktuellen Parameter der LED
        """
        #Die aktuellen Werte einer LED werden in Form eine dictionarys zurück gegeben.
        return {objekt.name: "Name", objekt.farbe : "Farbe", objekt.frequenz : "Frequenz", objekt.helligkeit : "Helligkeit"}

#    def update_LED(self):







