Ohjeet .txt-tiedostossa.

Nettisivun osoite: http://86.50.21.102/

Tässä repossa ollut .csv-tiedosto oli käytössä alkuun, mutta myöhemmin sama data on viety MySQL-serverille ja tulee luetuksi sen kautta serverille. Jätin tiedoston kuitenkin tänne varmuuden vuoksi, mikäli sitä sattuu tarvitsemaan joskus.

Viikkotehtävän tehtävänannossa oli jäänyt epäselväksi, että riittääkö, että nettisivun osoitteeseen mennessään tulisi ohjatuksi suoraan data-analysis -sivulle, 
mutta toisaalta ohjeissa luki: "Lisää pääsivulle (/) linkki, joka ohjaa tälle sivulle.", joten tein sitten yksinkertaisen etusivun, jossa on linkki, joka ohjaa data-analysis -sivulle. 
Tämän takia tuli muokattua myös Nginx Reverse Proxy configuraatiota sen verran, että locationin alla ollut "return 302 /data-analysis/;" on kommentoitu pois. Sen saa sitten takaisin käyttöön heti poistamalla kommentin, jos tarve vaatii.
