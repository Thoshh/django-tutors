.. _ref-uploadhandlers:

**************************************************
Zarządzanie przyjmowaniem plików (Upload Handlers)
**************************************************

Przez długi czas jedynym sposobem zarządzania danymi plikowymi odbieranymi przez Django od serwera HTTP był sposób, który trudno nazwać wydajnym: zawartość całego pliku była wczytywana do pamieci procesu z przekazanego żądania HTTP i następnie kopiowana we wskazane miejsce. Na szczęście dzięki tytanicznej pracy developerów Django nie jest to już jedyny sposób. W czasie *drogi do 1.0* przebudowano całe zaplecze obsługi uploadu plików, zmieniając przy tym sposób, w jaki Django przyjmuje dane od serwera HTTP. Obecna sytuacja przedstawia się następująco:

* jeżeli plik jest mniejszy, niż pewien ustalony rozmiar (domyślnie jest to 2.5MB), dane są nadal ładowane do pamięci procesu i obsługiwane tak, jak to miało miejsce dotychczas;
* jeżeli rozmiar pliku jest większy, niż ustalony rozmiar o którym wspomniałem wcześniej, dane są przechowywane w tymczasowej lokalizacji (pliku) na dysku, a następnie w sposób wydajny przemieszczane do ostatecznej lokalizacji;
* dane mogą być zapisywane i odczytywane także we fragmentach, jeżeli serwer HTTP potrafi przekazać dane w ten sposób (a większość potrafi);
* można zdefiniować własny sposób obsługi uploadowanych danych, np. po to, by informację o postępie odbierania pliku pokazać *na froncie* przy użyciu jakiegoś asynchronicznego mechanizmu.

Ten samouczek traktuje właśnie o sposobach przyjmowania danych plikowych od serwera HTTP przy użyciu własnego mechanizmu.

