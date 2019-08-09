import Lampe

Farben = ['rot', 'blau', 'blau', 'rot', 'weiß', 'ir', 'blau', 'rot', 'blau',
          'uv', 'weiß', 'gruen', 'rot', 'weiß', 'blau', 'rot']
Namen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Helligkeit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def init_Lampe(Namen, Farben, Helligkeiten, value):
    """

    :param Namen: Eine Liste mit Namen von einer Menge von LEDs
    :param Farben: Eine Liste mit Farben von einer Menge von LEDs
    :param Helligkeiten: Eine Liste mit Helligkeit von einer Menge von LEDs
    :param value: Ein Integer-Wert für die Anazhl an LEDs
    :return: Eine Liste mit Objekten der Klasse LED, wobei die Eigenschaften
     des i-ten Objekte denen des i-ten Listenelments entsprechen
    """
    L = Lampe.Lampe([Lampe.LED(Namen[i], Farben[i], Helligkeiten[i])
                     for i in range(value)])
    print(L)
    return L

def tagsim(LEDs,fade,should):
    """
    :param should: der Sollwert für die helligkeit
    :param fade: Die steigung der aktualisierungs Funktion, je kleiner desto
     steiler.
    :param LEDs: Eine Liste mit Objekten der Klasse LED
    :return:
    """

    i = 0
    while i <= should:
        if i%fade == 0:
            for LED in LEDs:
                if LED.farbe == "rot":
                    LED.helligkeit = i
                if LED.farbe == "blau":
                    LED.helligkeit = i
                if LED.farbe == "gruen":
                    LED.helligkeit = i
                if LED.farbe == "weiß":
                    LED.helligkeit = i
                if LED.farbe == "uv":
                    LED.helligkeit = i
                if LED.farbe == "ir":
                    LED.helligkeit = i
                # LED.update()
        i+=1
        print([LED.get(LED) for LED in LEDs])


###############################################################################
                                    #TEST#
###############################################################################

Namen = []
Fraben = []
Helligkeiten = []
for i in range(16):
    if i in [0,3,7,12,15]:
        Fraben.append("rot")
        Helligkeiten.append(0)
        Namen.append(i)
    if i in  [1,2,8,14]:
        Fraben.append("blau")
        Helligkeiten.append(0)
        Namen.append(i)
    if i in [4,6,10,13]:
        Fraben.append("weiß")
        Helligkeiten.append(0)
        Namen.append(i)
    if i in [9]:
        Fraben.append("uv")
        Helligkeiten.append(0)
        Namen.append(i)
    if i in [5]:
        Fraben.append("ir")
        Helligkeiten.append(0)
        Namen.append(i)
    if i in [11]:
        Fraben.append("gruen")
        Helligkeiten.append(0)
        Namen.append(i)
print(Fraben)
print(Namen)
print(Helligkeiten)

A = init_Lampe(Namen, Farben,  Helligkeit, 16)
tagsim(A.LEDs, 52,1024)
# for i in A:
#     print(i.get(i))
