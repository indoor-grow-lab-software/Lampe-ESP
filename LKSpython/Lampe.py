# Die Klasse Lampe erstellt.


class Lampe:


    def __init__(self, LEDs = []):
        self.LEDs = LEDs

#    def update(self):




class LED(Lampe):


    def __init__(self, name, farbe, helligkeit = 0):
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





B = LED(1,2)
A =  Lampe([1,2,3,4])

print(A.LEDs,B.name)