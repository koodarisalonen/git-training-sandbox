#!/usr/bin/env python3.4

def main():
	print("Moro Hervanta!")
	
'''
Osan 2 vastaukset
Mitä hyötyjä automaattisesta testauksesta on verrattuna manuaaliseen testaukseen?

Automaattinen testaus on parempi tapa tehdä triviaaleja toistuvia testejä, joille on selkeä määrittely, sekä pitkäkestoisia testejä kuten toiminnan vakauden testaus.

Mitä haasteita testauksen automatisointi asettaa verrattuna manuaaliseen testaukseen? Pohdi näitä erityisesti kurssin sisällön kontekstissa.

Testiautomaation ylläpito voi käydä rankaksi, jos projektin speksit muuttuvat sen aikana. 
Se myös sitouttaa kehitystiimin ottamaan testiautomaation huomioon jo kehitysvaiheessa tai osallistumaan ylläpitoon.

Mihin tarvitaan versionhallintaa? Pohdi asiaa testausprojektin kannalta, jossa on useita rinnakkaisia testaajia tai tiimejä. Minkälaisia haasteita saatat kohdata?

Versionhallinta mahdollistaa koodin osien käyttämisen ristiin projektien ja tiimien välillä, samalla säilyttäen omat kokonaisuudet. 
Se myös mahdollistaa ajettavan ja kehitettävän koodin pitämisen erillään. TL;DR *Pukeutuu kaapuun ja huutaa: "DEVOPS!"* 

Mitä etuja Python tarjoaa kielenä sulautetun järjestelmän testaukseen verrattuna esim. C-kieleen? Mitä haasteita?

Python ja muut scriptauskielet ovat helppo tapa tehdä laajojakin toiminnallisuuksia nopeasti ja ylläpidettävästi. 
C:llä asioita joutuisi määrittelemään valtavat määrät pienen toiminnallisuudenkin tekemiseksi. 
Toisaalta Pythonilla ei päästä tarkistelemaan asioita suoraan hardware-tasolla(ellei toteuteta jotain rajapintaa erikseen esim. C:llä). 

Miten testiautomaatiota voisi soveltaa kurssilla tehtyihin suunnitteluesimerkkeihin?

Jos testi on hyvin määritelty, se tarjoaa suoraan pseudokoodin testiscriptin luomiseksi.
 
'''

if __name__== "__main__":
  main()