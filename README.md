# vierOpEenRijIPASS

## Probleemstelling
Voor mijn IPASS heb ik een vier op een rij bot gemaakt. Dit omdat ik met mijn vader vaak spelletjes speel en wij discusseren over wat de beste zet zou moeten zijn.
Voor mijn vader heb ik deze AI gemaakt om een definitief antwoord te hebben op onze vraag.

## Gekozen Algoritme
Ik heb het Minimax algoritme gekozen. Dat een boom maakt van alle mogelijke scenario's en een score geeft aan een scenario. Hij kiest de zet die de AI het meest voordeligste scenario geeft. Voor dit algoritme heb ik een functie die alle mogelijke zetten terug geeft, een functie die een zet kan maken, een functie die een bord kan beoordelen en een score kan geven en tot slot het minimax algoritme die de beste zet onthoudt en maakt.

## Files
De Main is waar de game loops worden aangeroepen. De game loops staan weer in het bestand game_loops in de folder rules. de game loops roepen de functies aan van het bestand game 
geloceert in de folder rules. Game creeert het spel op basis van een numpy matrix en heeft hier alle functies staan waar het spel mee gemaakt is. In de game loops wordt ook 
aangeroepen het bestand Board geloceert in de layout folder. Deze class maakt de UI en zorgt ervoor dat de numpy matrix visueel wordt met een bord en rode en gele stenen.

## Hoe het Spel werkt
Als je het main bestand runt ga je het vier op een rij spel spelen. Je kunt kiezen om tegen een ander persoon te spelen of tegen de AI. Klik op een van de twee kanten van het 
scherm om een keuze te maken. Als je tegen een speler wilt spelen begint het spel meteen. Zodra vier op een rij is behaald wordt het spel afgesloten en krijg je in de terminal 
te zien wie gewonnen heeft.
als je tegen de AI speelt kun je een kleur kiezen en mag je de eerste zet doen. 
Vervolgens zou er in de terminal horen te staan dat de AI aan zet is en die denkt dan na over zijn zet.
Als de AI zijn zet heeft gedaan bent U weer aan zet. ALs vier op een rij is behaald dan komt er te staan wie gewonnen heeft en sluit het spel zich af.

