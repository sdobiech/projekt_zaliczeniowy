# Projekt zaliczeniowy w ramach studiów podyplomowych Tester oprogramowania


## Celem projektu było przetestowanie logowania na stronie internetowej castorama.pl z wykorzystaniem narzędzia Selenium Webdriver. Podczas logowania sprawdzano walidację hasła.


### Projekt opiera się na języku programownia Python oraz korzysta z bibliotek unittest, selenium oraz time.  


Środowisko wykorzystane do tworzenia testu:
Chrome wersja 90.0.4430.212
Ubuntu: 20.04 LTS.

Warunki wstępne:
1. Uruchomiona przeglądarka
2. Na stronie https://www.castorama.pl
3. Użytkownik niezalogowany

Kroki:
1. Zaakceptuj politykę cookies
2. Kliknij Logowanie i rejestracja
3. Wpisz Adres e-mail (w części Rejestracja)
4. Wpisz hasło (w części Rejestracja; brak dużych liter, znaków specjalnych, zbyt krótkie)
5. Powtórz hasło
6. Zaznacz oświadczenie o zapoznaniu z regulaminem
7. Kliknij Załóż konto

Oczekiwany rezultat:
Użytkownik dostaje informację: "Hasło powinno składać się co najmniej z 8 znaków: dużej litery, małej litery, cyfry lub znaku specjalnego (!\'^£$%&*()}{@#~?><>,|=_+¬-])."

Warunki końcowe:
Konto nie zostaje założone


W przyszłości skrypt można rozbudować np. o kontrolę poprawności adresu e-mail czy poprawność działania na innych przeglądarkach.

Komentarz: Projekt został napisany w czerwcu 2021. W chwili obecnej zmieniły się lokalozatory na testowanej stronie - projekt wymaga aktuazliacji.
