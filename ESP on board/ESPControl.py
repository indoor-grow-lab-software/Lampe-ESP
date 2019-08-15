""" PY TO ESP (LED CONTROLLER) """
# Written by Junicchi - https://github.com/Kebablord

import urllib.request
root_url = "https://192.168.1.1"  # ESP's url, ex: https://192.168.102 (Esp serial prints it when connected to wifi)

def sendRequest(url):
	n = urllib.request.urlopen(url) # send request to ESP

# Example usage
while True:
	magnitude, value = input("""Um Die LED zu kontrollieren wird eine Eingabe 
	der Form: frq, hel oder set + ein int wert von 0-2000,
	 0-4024 oder 0-1 benötigt """).split()
	if magnitude == "frq":
		sendRequest(root_url + "/FRQ_" + value)
		print("Die Frequenz der Leuchte wurde auf " + value + " aktualisiert.")
	elif magnitude == "hel":
		sendRequest(root_url + "/HEL_" + value)
		print("Die Helligkeit der Leuchte wurde auf " + value + " aktualisiert.")
	elif magnitude == "set":
		sendRequest(root_url + "/SET_" + value)
		print("Die Leuchte wurde an oder aus geschalted")
#sendRequest(root_url + int(answer))