# Triviant

## Inleiding

### Wat is Triviant?

We gaan een Triviant spel maken. Triviant is een spelletje waar je vragen moet beantwoorden. Wij gaan een digitale versie maken die in de commandline (terminal) gespeeld kan worden.

### Randvoorwaarden

- Je maakt gebruik van de opentdb API.
- De vragen die je stelt zijn multiple choice vragen vanuit de API, dit kunnen 2 of 4 antwoorden zijn.

### Stappenplan

#### 1. Kijk op de website van de [opentdb API](https://opentdb.com/api_config.php) en bekijk hoe je de API kunt gebruiken.
#### 2. Maak een nieuwe python file aan en noem deze `triviant.py`.

#### 3. Maak een functie `get_question()` die een vraag ophaalt van de API en deze teruggeeft.

<details>
  <summary>Stappenplan voor stap 3</summary>

  * Gebruik de `requests` module om de API aan te roepen.
  * Gebruik de `json()` methode om de data om te zetten naar een dictionary.
     * Probeer eerst de vraag te ontleden uit de response.
       * <details><summary>Kom je er niet helemaal uit?</summary>

            vraag = response['results'][0]['question']
         </details>
  * Sla de antwoorden op in een lijst.
  * Sorteer de antwoorden zodat ze in de juiste volgorde staan.
     
       (`.sort(reverse=True)` geeft de lijst achterstevoren terug, dus True en False worden juist weergegeven. Ook staat het juiste antwoord altijd op een willekeurige plek in de lijst.)

  * Return de vraag, het juiste antwoord en de lijst met antwoorden. (Je kunt meerdere dingen returnen door ze te scheiden met een komma.)

</details>

#### 4. Functie voor het printen van vragen

   <details> 
     <summary>Stappenplan voor stap 4</summary>
   
   * Deze functie krijgt de vraag en de antwoordenlijst als argumenten.
   * Print de vraag.
   * Print de antwoordenlijst. (gebruik een for loop om de antwoorden te printen)
     * <details><summary>Kom je hier niet uit?</summary>
   
       'antwoord' en 'antwoordenlijst' zijn variabelen. Dit kunnen ook andere namen zijn.
   
            i = 1  
            for antwoord in antwoordenlijst:  
                print(f"{i}. {antwoord}")  
                i += 1
       </details>

   * Wat valt je op? Er staan in sommige vragen HTML codes ( &quot ; , &#039 ; , &amp ;  ). deze codes moet je vervangen door de juiste tekens ( " , ' , &), dit kan met een string functie die de replace() methode gebruikt.
   </details>


#### 5. Functie voor het vragen van het antwoord van de speler

<details>
  <summary>Stappenplan voor stap 5</summary>

   * Deze functie moet controlleren dat de speler een geldig antwoord geeft. (1, 2, 3 of 4)
   * Return het antwoord van de speler.
</details>

#### 6. Functie voor het controleren van het antwoord
    
   <details>
    <summary>Stappenplan voor stap 6</summary>

   * Deze functie krijgt het antwoord van de speler en het juiste antwoord als argumenten.
   * Controleer of het antwoord van de speler gelijk is aan het juiste antwoord.
   * Returned True als het antwoord goed is en False als het antwoord fout is.

   </details>

#### 7. Functie voor het spelen van het spel

   <details> 
    <summary>Stappenplan voor stap 7</summary>

   * Deze functie gaat de vraag ophalen. Hij controleert of je een vraag, antwoord en foute antwoorden hebt opgehaald. (Mocht dit niet zo zijn, dan moet hij zichzelf opnieuw aanroepen.)
   * Daarna print hij de vragen.
   * Vraagt het antwoord van de speler.
   * Controleert of het antwoord goed is en print daarna of het antwoord goed of fout is.
</details>

#### 8. Functie voor het starten van het spel (main)

   <details>
    <summary>Stappenplan voor stap 8</summary>

  * Je print eerst een welkomstbericht.
  * Vervolgens declareer je een boolean 'play_again' die op True staat.
  * Maak een while loop die blijft draaien zolang 'play_again' True is.
  * In de while roep je de functie die je in stap 7 hebt gemaakt aan.
  * Vraag aan de speler of hij nog een keer wil spelen.
  * Als de speler 'ja' zegt, blijft 'play_again' True en speelt het spel opnieuw.
  * Als de speler 'nee' zegt, zet je 'play_again' op False en stopt het spel. Geef dan een bedankberichtje terug.
</details>

### Bonus

Probeer in je spel eens uit hoe je meerdere spelers kunt laten spelen. Hier kun je gebruik maken van de dictionary om de naam van de speler en zijn score bij te houden. De spelers krijgen om de beurt een vraag en kunnen punten verdienen.
