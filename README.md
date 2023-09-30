# Dokumentacja Job Scraper

Autors: [TheFlowersAI]
Data: [30.09.2023]

## Wprowadzenie

Job_Scraper to skrypt służący do scrapowania ofert pracy z wybranych stron internetowych. Ten skrypt umożliwia pobieranie ofert pracy z różnych stron internetowych, przetwarzanie ich i wyświetlanie istotnych informacji o każdej z ofert.

## TODO

Czas nie pozwala na wykonanie całego projektu jako jeden z najważniejszych elementów uznaliśmy webscrapping, zatem na początku skupiliśmy się na nim. Do wersji ostatecznej zaimplementowany zostanie algorytm sztucznej inteligencji analizujacy na jakich ofertach spędziłeś najwięcej czasu, aby dopasować oferty pod twoje zainteresowania, oraz analizę rynku pracy przy pomocy modelu, który pozwoli na predykcję przyszłych potrzeb rynku pracy.

## Wymagane Biblioteki

Przed użyciem tego skryptu, upewnij się, że zainstalowałeś następujące biblioteki za pomocą polecenia `pip install [biblioteka]`:

- requests: Biblioteka do wykonywania zapytań HTTP.
- BeautifulSoup: Biblioteka do analizy i przetwarzania stron internetowych.
- pyshorteners: Biblioteka do skracania adresów URL.

## Konfiguracja

Aby użyć tego skryptu, musisz dostarczyć link do strony internetowej zawierającej oferty pracy. Następnie uruchom skrypt, który przeszuka oferty pracy na podanej stronie i wyświetli istotne informacje o każdej ofercie.

## Użycie

### Przykładowe Użycie:

1. Zdefiniuj link do strony internetowej zawierającej oferty pracy w zmiennej `PAGE_LINK`.
2. Uruchom skrypt za pomocą polecenia `python nazwa_skryptu.py`.

## Klasa JobScraper

### `get_source_code(source_page_link: str) -> BeautifulSoup`

Ta metoda pobiera źródłowy kod strony internetowej.

### `get_job_offert_links()`

Ta metoda wyszukuje i zbiera linki do ofert pracy na stronie internetowej.

### `process_job_offert(offert)`

Ta metoda przetwarza i wyświetla informacje o pojedynczej ofercie pracy.

## Funkcje Pomocnicze

### `create_job_dict(ad_title, location, salary, working_time, workplace, position, offer_link) -> dict`

Ta funkcja tworzy słownik zawierający informacje o ofercie pracy.

### `extract_salary(salary_element)`

Ta funkcja wyciąga informacje o wynagrodzeniu z oferty pracy.

### `extract_working_time(source)`

Ta funkcja wyciąga informacje o czasie pracy.

### `extract_ad_title(source)`

Ta funkcja wyciąga tytuł oferty pracy.

### `extract_location(source)`

Ta funkcja wyciąga informacje o lokalizacji oferty pracy.

### `extract_workplace(source)`

Ta funkcja wyciąga informacje o miejscu pracy.

### `extract_position(source)`

Ta funkcja wyciąga informacje o rodzaju zatrudnienia.

## Główna Funkcja

Funkcja `main()` uruchamia skrypt, przeszukuje oferty pracy i wyświetla informacje o nich.
