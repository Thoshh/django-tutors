.. _ref-dynamic:

*****************************
Dynamiczne określanie ścieżki
*****************************

Od niedawna (oficjalnie od wydania wersji 1.0 Django) jako argument ``upload_to`` w konstruktorze ``FileField`` można podawać nazwę obiektu wykonywalnego, który przyjmując odpowiednie argumenty, zwróci ścieżkę, w której zostanie zapisany plik. Ta część samouczka dotyczy dawania większej ilości dynamiki do określania miejsca, gdzie będzie składowany odebrany plik.

Założenia nieco się zmieniły względem sposobu obsługi ze :ref:`statycznie zdefiniowaną ścieżką <ref-static>`, ale nie diametralnie:

* funkcja wyliczająca ścieżkę do zapisania danych w pliku musi przyjąć 2 argumenty: ``instance`` i ``filename``, a jej wynikiem ma być kompletna ścieżka wraz z nazwą pliku;
* pliki umieszczane są w lokalizacji relatywnej do ``settings.MEDIA_ROOT``;
* ścieżkę podaje się również w postaci relatywnej do ``settings.MEDIA_ROOT``.

Jak widać, ograniczeń jest trochę mniej i nie są one aż tak drastyczne, jednak wymaganie dostępności zasobów dla aplikacji nadal jest przestrzegane bardzo ściśle, i ta dostępność musi mieć charakter lokalny.