print("FPGA- ja ASIC-ohjelmointi: Ennakkotehtävät 22.10.2018\n")

print("1. Mitä hyötyjä automaattisesta testauksesta on \n\
verrattuna manuaaliseen testaukseen?")
print ("*Helppo ja nopea suorittaa toistettavia testejä\n\
*Pidemmät testaukset voidaan esim. suorittaa yöllä\n")

print("2. Mitä haasteita testauksen automatisointi asettaa verrattuna\n\
manuaaliseen testaukseen? Pohdi näitä erityisesti kurssin\n\
sisällön kontekstissa.")
print("*Täytyy aika tarkkaan tietää, mitä halutaan testata\n\
*Tuntea työkalut, joilla testit on mahdollista suorittaa\n")

print("3. Mihin tarvitaan versionhallintaa? Pohdi asiaa testausprojektin\n\
kannalta, jossa on useita rinnakkaisia testaajia tai tiimejä. \n\
Minkälaisia haasteita saatat kohdata?")
print("*Helppo pystyä perillä mahdollisista muutoksista lokitiedostojen avulla\n\
*Kaikki vanhat versiot ovat kuitenkin tallessa, jos muutoksia tehdään välissä\n\
*Pystytään esim. testaamaan samaa asiaa kahdella eri tapaa\n\
*Tiedostot täytyy pitää aika hyvin järjestyksessä, että kaikki tiimin jäsenet\n\
ovat samassa kohtaa menossa ja kaikki ovat sitoutuneita siihen\n")

print("4. Mitä etuja Python tarjoaa kielenä sulautetun järjestelmän \n\
testaukseen verrattuna esim. C-kieleen? Mitä haasteita?")
print("*Python on nopeampi kirjoittaa kuin C\n\
*C on nopeampi ajaa kuin Python, mutta Python suoriutuu tehokkaammin\n\
*Python sisältää valmiiksi suurenmäärän testaukseen suunniteltuja kirjastoja\n")

print("5. Miten testiautomaatiota voisi soveltaa kurssilla \n\
tehtyihin suunnitteluesimerkkeihin?")
print("*Koodin pätkä voisi lukea laitteesta pelkästään saatavaa UART:ia\n\
tai SPI:tä\n\
*Laitteen koodi voitaisiin ajaa simulaattorien läpi ja tutkia suoritusaikoja\n\
*Laitteelle voisi lähettää jotain simuloitua signaalia\n")
