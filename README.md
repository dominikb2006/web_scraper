# Web scraper

## Application for loading text and pictures from a URL with option of downloading them.

### PL:
### Opis:

Mikroserwis został stworzony na dockerze w Unixie w technologii Django oraz Postgres.

Moja przyszła praca inżynierska zostanie stworzona właśnie w tych
technologiach, które zresztą ostatnimi czasy rozwijałem, dlatego
stwierdziłem, że napisanie tego krótkiego projektu w tej technologi
będzie dla mnie dobrym sprawdzianem i utrwaleniem nabytej wiedzy.

### Aby uruchomić aplikację należy:
1. Pobrać repozytorium oraz uruchomić dockera.
2. Postawić Kontenery:
    ```
    $ docker-compose build 
    $ docker-compose up
    ```
3. Wejść w nowym oknie komend do Kontenera oraz postawić bazę danych:
    ```
    $ docker-compose exec web_scraper_backend python manage.py makemigrations web_scraper_app
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

    _Et voilà!_

**Funkcjonalność:**
- W zakładce `Home` po wprowadzeniu adresu URL (dalej jako `źródłowy URL`):
    * System sprawdza poprawność wprowadzonego adresu
    * System pobiera oraz zapisuje w bazie tekst z źródłowego URL (bez kodu HTML oraz JS)
    * System pobiera oraz zapisuje w bazie wszystkie obrazki z źródłowego URL
- W zakładce `List Texts` system zwraca wszystkie elementy tekstowe z bazy danch w tabeli `źródłowy URL | Tekst danej strony` w kolejności od najnowszego
- W zakładce `List Images` system zwraca wszystkie zapisane obrazy z bazy danych w tabeli `źródłowy URL | Obrazek | Lokalny adres w Kontenerze | Oryginalny adres URL obrazka` w kolejności od najnowszego
- Klikając zakładkę `Download Texts` pobieramy tabelę w formacie .CSV z danymi z bazy danych dot. tekstu (w formacie jak `List Texts`, tylko bez `order_by`)
- Klikając zakładkę `Download Images` pobieramy obrazy z folderu `/media/` z Kontenera, w którym znajdują się wszystkie obrazy z dazy danych
  
**Kod:**
- w `web_scraper_app/utils.py` znajdują się funkcje spradzające poprawność adresu URL, pobierające cały tekst oraz listę obrazków ze strony
- w `web_scraper_app/models.py` znajdują się modele bazodanowe
- w `web_scraper_app/views.py` znajdują się stworzone widoki
- w `web_scraper_app/templates/` znajdują się templatki HTMLowe
- w `web_scraper_app/tests.py` znajdują się testy
    
**Do poprawy lub zmiany:**
- czasem w adresie URL obrazka pojawiają się nietypowe znaki, np. przecinek. Wtedy Aplikacja ich nie zapisuje
- nie można zapisać zdjęć ze stron, które nie dają możliwości ich zapisania
- czasem strony blokują pobieranie informacji (np blablacar)
- format CSV dla ściąganej tabeli z tekstem chyba nie jest najlepszy, ponieważ bardzo duże ilości tekstu pojawiają się w jednej komórce, przez co niektóre Aplikacje typu `LibreOffice` nie chcą ich ładować.
Z drugiej strony te dane nie będą obrabiane w typowym 'Excelu', więc możliwe, że ten format będzie spełniał swoje zadanie.
- można podzielić pobierany tekst ze stron do bazy danych na fragmenty, np. `Head | <Wnętrze Head>`, `Body | <Wnętrze Body>`, `p | <Wnętrze p>`, etc.
- użycie form może poprawić późniejszą obróbkę i czytelność kodu
- wszystkie operacje działały w miare szybko, dlatego nie dodawałem operacji `Sprawdzenia statusu zleconego zadania` 
- więcej testów
**Wnioski:**

Podczas pisania powyższej aplikacji powtórzyłem oraz utrwaliłem stawianie Kontenerów w Dockerze oraz ogólnie pisanie Aplikacji w Django.
Nauczyłem się pisać postawowe testy w Django oprujące na widokach, modelach i API. Poznałem wiele nowych bibliotek, jak `BeautifulSoup`, `requests`, czy `urllib`. Praca z dokumentacją tych bibliotek oraz Django połączona z szukaniem
rozwiązań na wszelakich forach uważam za kształcące doświadczenie,
które poprawiło moją zdolność w pracy nad kodem i które na pewno w niedalekiej przyszłości użyję ponownie.
Jestem zadowolny w mojej pracy i uważam, że wyczerpuje zadane problem.

```
1. Opis zadania
Zadanie polega na stworzeniu mikroserwisu wspierającego pracę
programistów zajmujących się uczeniem maszynowym. System ma pomóc
w gromadzeniu i udostępnianiu informacji pobranych z sieci. Główną
funkcjonalnością systemu jest pobieranie tekstu oraz obrazków ze
stron internetowych. 
2. Funkcjonalność 
    • Zlecenie pobrania tekstu z danej strony internetowej i zapis jej w systemie. 
    • Zlecenie pobrania wszystkich obrazków z danej strony i zapis ich w systemie. 
• Sprawdzenie statusu zleconego zadania. 
    • Możliwość pobrania stworzonych zasobów (tekstu i obrazków). 
3. Architektura 
    • Zadanie polega na zaprojektowaniu i zaimplementowaniu REST API dla tego systemu. 
    • Mikroserwis powinien być napisany w języku Python. 
    • Rozwiązanie powinno zawierać testy automatyczne. 
    • Uruchomienie mikroserwisu powinno być maksymalnie zautomatyzowane (preferowane użycie Dockera lub podobnych narzędzi). 
4. FAQ 
    • Czy wymagane jest wykonanie Javascriptu w celu uzyskania tekstu/obrazków na stronie? Nie, pobieramy tylko statyczne zasoby. 
    • Czy z tekstu pobieranego ze stron powinien usuwać tagi HTML i kod Javascript? Tak. 
    • Czy napisanie frontendu jest częścią zadania? Nie. 
    • Czy można założyć, że pobieranie tekstu/obrazków ze strony jest szybkie? Nie, pobieranie może trwać bardzo długo. 
    • Pisząc o stronie internetowej mamy na myśli pojedynczy dokument HTML /konkretny URL (i obrazki w nim zalinkowane). 
5. Kryteria sukcesu: 
    • Właściwa architektura dla tego problemu 
• Poprawnie zaprojektowane i zaimplementowane API (niekoniecznie dogłębna implementacja) 
    • Automatyzacja systemu 
    • Testy systemu 
    • Pisemny komentarz od autora na temat rozwiązania. Może być w stylu retro (co poszło ok, co nie ok, co do zmiany) 
Rozwiązanie proszę umieścić jako prywatne repozytorium na Githubie, udostępnione dla użytkownika FeedbackSemantive oraz przesłać link do niego. 
```