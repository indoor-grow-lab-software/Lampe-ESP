import LED
def init_LED(Namen, Farben, Frequenzen, Helligkeiten, value):
    """

    :param Namen: Eine Liste mit Namen von einer Menge von LEDs
    :param Farben: Eine Liste mit Farben von einer Menge von LEDs
    :param Frequenzen: Eine Liste mit Frequenzen von einer Menge von LEDs
    :param Helligkeiten: Eine Liste mit Helligkeit von einer Menge von LEDs
    :param value: Ein Integer-Wert für die Anazhl an LEDs
    :return: Eine Liste mit Objekten der Klasse LED, wobei die Eigenschaften des i-ten Objekte denen des i-ten Listenelments entsprechen
    """
    LEDs = [LED.LED(Namen[i], Farben[i], Frequenzen[i], Helligkeiten[i]) for i in range(value)]
    print(LEDs)
    return LEDs


########################################################################################################################
                                                    #TEST#
########################################################################################################################
# def tagsim(LEDs):
#     for LED in LEDs:
#         if LED.farbe == "rot":
#
# Namen = ["eins", "zwei", "drei"]
# Farben = ["rot", "blau", "UV"]
# Frequenzen = [700, 1200, 1600]
# Helligkeit = [1000, 2000, 4000]
# A = init_LED(Namen, Farben, Frequenzen, Helligkeit, 3)
# for i in A:
#     print(i.get_LED(i))
