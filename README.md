# Web scraper

## Application for loading text and pictures from a URL with option of downloading them.

### PL:
### Opis:

Mikroserwis został stworzony na dockerze w Unixie w technologii Django oraz Postgres.

### Aby uruchomić aplikację należy:
1. Pobrać repozytorium oraz uruchomić dockera.
2. Postawić Kontenery:
    ```
    $ docker-compose build 
    $ docker-compose up
    ```
3. Przez nowe okno komend postawić bazę danych:
    ```
    $ docker-compose exec web_scraper_backend python manage.py migrate
    ```
    (Opcjonalnie) Stworzyć Superusera:
    ```
    $ docker-compose exec web_scraper_backend python manage.py createsuperuser
    ```
    (Opcjonalnie) Uruchomić testy:
    ```
    $ docker-compose exec web_scraper_backend python manage.py test
    ```
4. Uruchomić przeglądarkę i wpisać adres `localhost:8000`

    ##    _Et voilà!_

**Funkcjonalność:**
- W zakładce `Home` po wprowadzeniu adresu URL (dalej jako `źródłowy URL`):
    * System sprawdza poprawność wprowadzonego adresu
    * System pobiera oraz zapisuje w bazie tekst z źródłowego URL (usuwając kod HTML oraz JS)
    * System pobiera oraz zapisuje w bazie wszystkie obrazki z źródłowego URL
- W zakładce `List Texts` system zwraca wszystkie elementy tekstowe z bazy danch w tabeli `źródłowy URL | Tekst danej strony` w kolejności od najnowszego
- W zakładce `List Images` system zwraca wszystkie zapisane obrazy z bazy danych w tabeli `źródłowy URL | Obrazek | Lokalny adres w Kontenerze | Oryginalny adres URL obrazka` w kolejności od najnowszego
- Klikając zakładkę `Download Texts` pobieramy tabelę w formacie .CSV z danymi z bazy danych dot. tekstu (w formacie jak `List Texts`, tylko bez `order_by`)
- Klikając zakładkę `Download Images` pobieramy obrazy z folderu `/media/` z Kontenera, w którym znajdują się wszystkie obrazy z dazy danych
  
**Kod:**
- w `web_scraper_app/utils.py` znajdują się funkcje sprawdzające poprawność adresu URL, pobierające cały tekst oraz listę obrazków ze strony
- w `web_scraper_app/models.py` znajdują się modele bazodanowe
- w `web_scraper_app/views.py` znajdują się stworzone widoki
- w `web_scraper_app/templates/` znajdują się template HTMLowe
- w `web_scraper_app/tests.py` znajdują się testy
    
**Do poprawy lub zmiany:**
- czasem w adresie URL obrazka pojawiają się nietypowe znaki, np. przecinek. Wtedy Aplikacja ich nie zapisuje
- nie można zapisać zdjęć ze stron, które są chronione przed zapisem
- część Aplikacji zwraca RESTowy response, część renderuje HTML. Można w całości użyć RESTa
- czasem strony blokują pobieranie informacji (np. blablacar)
- format CSV dla ściąganej tabeli z tekstem chyba nie jest najlepszy, ponieważ bardzo duże ilości tekstu pojawiają się w jednej komórce, przez co niektóre Aplikacje typu `LibreOffice` nie chcą ich ładować.
Z drugiej strony te dane nie będą obrabiane w typowym 'Excelu', więc możliwe, że ten format będzie spełniał swoje zadanie.
- możnaby podzielić pobierany tekst ze stron do bazy danych na fragmenty, np. `Head | <Wnętrze Head>`, `Body | <Wnętrze Body>`, `p | <Wnętrze p>`, etc.
- wszystkie operacje działały w miare szybko, dlatego nie dodawałem operacji `Sprawdzenia statusu zleconego zadania` 
- więcej testów