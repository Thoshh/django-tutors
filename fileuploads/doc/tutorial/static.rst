***********************
Statyczny upload plików
***********************

Jest to sposób, jaki w Django był dostępny *od zawsze* (a właściwie odkąd Django obsługuje upload plików). W związku z tym, że pojawiły się niedawno (w czasie przygotowań do wydania 1.0) nowe sposoby obsługi uploadowanych plików, ten sposób nieco stracił na znaczeniu, ale nadal w wielu przypadkach jest zupełnie wystarczający. Przypomnę, jakie są jego założenia.

* pliki umieszczane są w lokalizacji relatywnej do ``settings.MEDIA_ROOT``;
* ścieżkę podaje się również w postaci relatywnej do ``settings.MEDIA_ROOT``;
* ścieżka w której zostanie umieszczony plik musi być znana (niekoniecznie musi istnieć) w momencie kompilacji modułu;
* w definicji ścieżki można użyć formatowania używanego w funkcji ``time.strftime()``.

W wielu sytuacjach wystarcza to całkowicie do tego, aby przyjąć plik od użytkownika strony i udostępnić go aplikacji.

Przykładowy kod
===============

Przykładowy kod aplikacji znajduje się w katalogu ``<root>/uploads``.