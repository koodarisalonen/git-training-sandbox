#!/usr/bin/env python
# -*- coding: utf-8 -*-
hellostring = "FPGA- ja ASIC-piirien suunnittelu ja testaus 22.10.2018 Ennakkotehtävien vastaukset, by Henri Keinonen"
print(hellostring)
print("==========\n\n")

answers = [
	{"question": "1. Mitä hyötyjä automaattisesta testauksesta on verrattuna manuaaliseen testaukseen?",
	"answer" : "Prosessi voidaan toistaa nopeasti ja virheettömästi useita kertoja ilman ihmisen interkatiota."},
	{"question": "2. Mitä haasteita testauksen automatisointi asettaa verrattuna manuaaliseen testaukseen? Pohdi näitä erityisesti kurssin sisällön kontekstissa.", "answer" : "Täytyy suunnitella testausprosessi huolellisesti ja tuntea testattava kohde jotta saadaan oikeat tulokset."},
	{"question": "3. Mihin tarvitaan versionhallintaa? Pohdi asiaa testausprojektin kannalta, jossa on useita rinnakkaisia testaajia tai tiimejä. Minkälaisia haasteita saatat kohdata?", 
	"answer" : "Muutoksia on helppo seurata ja palauttaa, uusimmat tiedot ovat nopeasti saatavilla ja syntyy vähemmän ristiriitoja eri kontribuoijien välillä.\nHaasteita voi syntyä mikäli jäsenet eivät päivitä muutoksi riittävän usein, tai dokumentaatio on puutteellista."},
	{"question": "4. Mitä etuja Python tarjoaa kielenä sulautetun järjestelmän testaukseen verrattuna esim. C-kieleen? Mitä haasteita?", 
	"answer" : "Pythonin kirjoittaminen ja ajaminen on nopeaa kielen rakenteesta ja suorituksesta johtuen ja pythonille löytyy valmiiksi toteutuksia testaukseen.\nPython ei ole yhtä tehokas kieli ajon aikana verrattuna käännettyihin kieliin, joten suuret, nopeutta vaativat testausautomaatiot voivat olla hitaita. Python soveltuu huonommin laitteistoläheiseen matalan tason ohjelmointiin."},
	{"question": "5. Miten testiautomaatiota voisi soveltaa kurssilla tehtyihin suunnitteluesimerkkeihin?", 
	"answer" : "Manuaalista datan käsittelyä voisi nopeuttaa testiautomaation avulla ja yhdistää useita testejä yhdeksi kokonaisuudeksi joka voidaan ajaa automaattisesti. Testiautomaation tulokset voitaisiin helposti esittää ihmiselle ymmärettävässä muodossa ja verrata odotettuihin tuloksiin automaattisesti."}
]

for row in answers:
	print "Kysymys {}\n\nVastaus: {}\n-----\n".format(row["question"],row["answer"])
raw_input('Press enter key to exit')
