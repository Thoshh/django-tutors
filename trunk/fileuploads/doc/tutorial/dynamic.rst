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

Przykładowy kod
===============

Przykładowy kod znajduje się w tych samych modułach, co kod do przykładów :ref:`statycznego uploadu <ref-static>`, jednak interesują nas teraz inne klasy:

* model, którego będziemy używać, to ``DynamicFileUpload``;
* w module ``views.py`` interesuje nas funkcja ``dynamic()``;
* będziemy używać formularza ``DynamicUploadForm`` z modułu ``forms.py``.

Kod aplikacji
=============

Podobnie jak w przypadku uploadu do statycznej ścieżki zaczynamy od modelu. Definicja atrybutu, w którym będziemy przechowywać dane pliku jest bardzo podobna do tej, jaką mieliśmy w przykładzie ze statycznym uploadem, jest jednak pewna różnica::

    upload = models.FileField('upload', upload_to=get_dynamic_path)

Argument ``upload_to`` jest literałem z nazwą funkcji, która wyliczy ścieżkę, w której zostanie zapisany plik. Kod tej funkcji oczywiście trzeba dostarczyć (nie ma takiej funkcji *domyślnej*). Funkcja wyliczająca ścieżkę musi przyjąć dwa argumenty: ``instance`` i ``filename``. Argument ``instance`` będzie zawierał instancję obiektu, w którym będzie zapisywany plik, natomiast ``filename`` będzie zawierać nazwę (bez ścieżki) zapisywanego pliku, podaną w metodzie ``save()`` obiektu klasy ``FileField``. Funkcja z naszego przykładu wygląda następująco::

    def get_dynamic_path(instance, filename):
        """Bit of stupidity: the dynamic element is determined by length of title"""
        return 'dynamic/%s/file/%s' % (str(len(instance.title)), filename)

Jak widać, ścieżka nadal określana jest w formie relatywnej (oczywiście, do ``settings.MEDIA_ROOT``), jednak można przy jej określaniu użyć atrybutów instancji, do której będzie dołączony plik. Zanim jednak strzelą korki od szampana trzeba sobie uświadomić, że nie wszystkie atrybuty mogą zostać użyte do tego celu. Które nie mogą? Otóż nie mogą zostać użyte te, których w momencie wykonywania tej funkcji w instancji nie ma, a nie ma na przykład autogenerowanego identyfikatora przed pierwszym zapisem obiektu, może także nie być wartości w atrybutach, dla których dopuszczalna jest wartość ``None`` (czyli tych, które w definicji swojej mają ``null=True``). W przypadku autogenerowanego identyfikatora rozwiązanie jest podobne, jak w przypadku uploadu statycznego (czyli dwukrotny zapis instancji modelu), ale z takimi samymi uwagami. W naszym przykładzie atrybut ``title`` jest wymagany, więc możemy mieć pewność, że w momencie zapisywania pliku będzie miał jakąś wartość.