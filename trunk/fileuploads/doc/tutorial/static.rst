***********************
Statyczny upload plików
***********************

Jest to sposób, jaki w Django był dostępny *od zawsze* (a właściwie odkąd Django obsługuje upload plików). W związku z tym, że pojawiły się niedawno (w czasie przygotowań do wydania wersji 1.0) nowe sposoby obsługi uploadowanych plików, ten sposób nieco stracił na znaczeniu, ale nadal w wielu przypadkach jest zupełnie wystarczający. Przypomnę, jakie są jego założenia.

* pliki umieszczane są w lokalizacji relatywnej do ``settings.MEDIA_ROOT``;
* ścieżkę podaje się również w postaci relatywnej do ``settings.MEDIA_ROOT``;
* ścieżka w której zostanie umieszczony plik musi być znana (niekoniecznie musi istnieć) w momencie kompilacji modułu;
* w definicji ścieżki można użyć formatowania używanego w funkcji ``time.strftime()``.

W wielu sytuacjach wystarcza to całkowicie do tego, aby przyjąć plik od użytkownika strony i udostępnić go aplikacji. Sytuacje niewystarczające zostaną omówione w dokumencie opisującym upload z użyciem dynamicznego generowania ścieżki.

Przykładowy kod
===============

Przykładowy kod aplikacji znajduje się w katalogu ``<root>/uploads`` a szablony znajdują się w katalogu ``<root>/templates/uploads``. Aplikacja ma standardową strukturę aplikacji Django:

* ``models.py``, zawierający modele (nas interesuje model ``StaticFileUpload``) i odpowiadający mu plik ``admin.py`` (z interfejsem administracyjnym klasy modelu);
* ``views.py``, zawierający widoki (interesujący nas widok to ``static()``);
* ``urls.py`` (`URLConf <http://docs.djangoproject.com/en/dev/topics/http/urls/>`_ zawierający definicję wszystkich ścieżek obsługiwanych przez aplikację);
* ``forms.py``, zawierający klasy formularzy do przyjmowania uploadu plików (nas interesuje klasa ``StaticUploadForm``).

W przypadku samodzielnego podążania za samouczkiem konieczne będzie utworzenie niektórych z powyższych plików, ponieważ programy ``django-admin.py`` i ``manage.py`` tworzą tylko podstawowy zrąb projektu i aplikacji, zawierający wyłącznie niezbędne moduły.

Kod aplikacji
=============

Samouczek rozpoczynamy od utworzenia (czyli *wymyślenia i napisania kodu*) klasy modelu. Dla naszego modelu ważne jest tylko to, by jednym z pól było pole typu ``FileField``, podobnie jak w kodzie przykładowym::

    upload = models.FileField('upload', upload_to='uploads/files')

Jedynym wymaganym argumentem konstruktora pola typu ``FileField`` jest ``upload_to``, określający ścieżkę, w której będą umieszczane odebrane pliki. Ścieżka ta zostanie *doklejona* do wartości zmiennej ``settings.MEDIA_ROOT``, tworząc razem absolutną ścieżkę do katalogu w systemie plików, w którym będą składowane pliki.

.. note ::
   Jeżeli ścieżka w ``upload_to`` zostanie podana z początkowym ukośnikiem, wtedy Django potraktuje ją jako ścieżkę bezwzględną w  systemie plików. Problem polega na tym, że automatyczny interfejs administracyjny aplikacji (``django.contrib.admin``) nie poradzi sobie z obsługą tego typu wartości i będzie ona niemożliwa do modyfikacji. Jakkolwiek kusząco by to nie wyglądało, dla własnego dobra lepiej tego nie robić.

Wartość tego argumentu może być do pewnego stopnia dynamiczna. Django umożliwia umieszczenie w niej znaczników formatowania, które przyjmuje funkcja ``time.strftime()`` z biblioteki standardowej Pythona. Odpowiednie znaczniki zostaną podstawione sformatowanymi wartościami zgodnymi z użytymi znacznikami. Zapis::

    upload = models.FileField('upload', upload_to='uploads/files/%Y/%m/%d')

spowoduje, że dostarczone pliki zostaną umieszczone w podkatalogach podzielonych na lata, miesiące i dni, kiedy plik został odebrany i tak plik odebrany 15 września 2008 roku znajdzie się w podkatalogu ``settings.MEDIA_ROOT/uploads/files/2008/09/15``. Takie *rozkładanie* plików do pewnego stopnia umożliwia uporządkowanie zasobów.

Następnym krokiem jest napisanie kodu przyjmującego uploadowany plik i umieszczającego go w odpowiednim miejscu. Większość pracy w przypadku statycznego określania ścieżki pliku wykona za nas Django. Kod ten najczęściej umieszcza się w klasie reprezentującej formularz HTML. Jest to zgodne z ideą oddzielania odpowiedzialności poszczególnych komponentów aplikacji za poszczególne działania. Klasy obsługi formularzy odpowiadają za przyjęcie od użytkownika danych i *przekonwertowanie* ich w dane, którymi posługuje się aplikacja, a więc w instancje odpowiednich modeli. W naszym przypadku jest to klasa ``StaticUploadForm``, znajdująca się w module ``forms`` przykładowej aplikacji.

Za utworzenie (i zwrócenie) instancji odpowiedniego modelu odpowiada metoda ``save()`` klasy reprezentującej formularz. W niej tworzona jest instancja klasy ``StaticFileUpload`` i ustawiane są jej atrybuty. O ile (posługując się kodem przykładowym) ustawienie atrybutu ``caption`` nie nastręcza szczególnych trudności, bo jest to zwykły atrybut typu ``unicode``, o tyle atrybut ``upload`` wymaga nieco zachodu.

Dane odebrane od użytkownika znajdują się w atrybucie ``cleaned_data`` instancji formularza. Jest to obiekt o interfejsie słownika o kluczach odpowiadających nazwom atrybutów klasy formularza. W przypadku przykładowego kodu dane dostarczonego pliku znajdują się pod kluczem ``upload``. Jest to obiekt specjalnej klasy ``UploadedFile``, która interfejsem jest zgodna z klasą ``File``, która reprezentuje plik w obiekcie ``FileField``. Aby ustawić w instancji klasy ``StaticFileUpload`` atrybut typu ``FileField``, należy wykonać jego metodę ``save()``, podając jako argumenty nazwę, pod jaką mają zostć zapisane dane plikowe, oraz same dane plikowe. W najprostszym przypadku możemy zapisać plik pod nazwą, pod jaką był uploadowany przez użytkownika, wtedy pełne wywołanie metody będzie miało postać::

    object.fieldname.save(self.cleaned_data['upload_field'].name, self.cleaned_data['upload_field'])

Tak też jest to zrobione w kodzie przykładowym.

I to już właściwie wszystko. Teraz pozostaje spojrzeć w system plików i stwierdzić, czy rzeczywiście w katalogu, który jest podany w zmiennej ``settings.MEDIA_ROOT`` została utworzona odpowiednia struktura podkatalogów i plik o odpowiedniej nazwie (takiej, jak miał plik w lokalnym systemie plików użytkowika) został utworzony w spodziewanym miejscu.

Co może się nie udać
====================

Przy statycznym określaniu ścieżki nie ma wielu rzeczy, które mogą nie zadziałać. Najczęściej spotykane błędy to omyłkowe podanie ścieżki bezwzględnej lub podanie lokalizacji, w której aplikacja nie ma uprawnień do zapisywania plików. Inne napotykane problemy wynikają z czynników zewnętrznych wobec systemu uploadu plików lub związanych z nim jedynie wirtualnie.

Możliwe modyfikacje
===================

W powyższym kodzie nie da się wprowadzić wielu zasadniczych modyfikacji. To, co było statyczne można w pewnym stopniu zdynamizować, podając znaczniki formatowania daty. Można też dodać walidację zawartości przesłanych danych, chociaż przez cały czas trzeba mieć świadomość, że dopóki posługujemy się słownikiem ``cleaned_data``, nie posiadamy pliku samego w sobie, lecz przez cały czas posługujemy się danymi binarnymi, czy to umieszczonymi w pamięci procesu, czy to w pliku tymczasowym na dysku. Można także zapisać plik pod zmienioną nazwą, jednak trzeba pamiętać o tym, że dopóki nie wykonamy metody ``save()`` instancji klasy modelu, ta instancja nie jest trwała (czyli m.in. nie posiada unikalnego identyfikatora), więc bez pewnych *myków* nie da się wprowadzić niczego, co nieco lepiej identyfikowałoby obiekt w systemie plików. A jak może wyglądać taka sztuczka?

Lepsza identyfikacja obiektów w systemie plików
-----------------------------------------------

Jak wcześniej wspomniałem, przed wywołaniem metody ``save()`` instancja nie ma trwałego charakteru. Aby uzyskać dostęp do atrybutów, które ją identyfikują jednoznacznie, trzeba albo najpierw ją zapisać, albo dostarczyć takich atrybutów samemu (klucz surogatowy jest znany dopiero **po** zakończeniu wykonywania metody ``save()``). Tą drugą sytuacją nie będziemy się zajmować, bo jest oczywista. A jak uzyskać dostęp do klucza surogatowego? Rozwiązanie jest proste, należy instancję zapisać dwukrotnie, najpierw bez ustawionego atrybutu reprezentującego plik, a następnie ponownie po ustawieniu tego atrybutu. Odpowiedni fragment metody ``save()`` klasy formularza mógłby mieć następującą postać::

    obj = StaticFileUpload(caption=self.cleaned_data['caption'])
    obj.save()
    new_filename = make_field_name(self.cleaned_data['upload_field'].name, obj.id)
    obj.uploaded_file.save(new_filename, self.cleaned_data['upload_field'])
    obj.save()

Sztuczka ta ma jednak kilka poważnych mankamentów, które mogą ją zdyskwalifikować w sytuacji *produkcyjnej*. Przede wszystkim, obiekt jest zapisywany dwukrotnie, więc muszą być wykonane dwie operacje na bazie danych: ``INSERT`` i ``UPDATE``. Nie ma to nic wspólnego z optymalizacją dostępu do bazy danych.

Inny problem jest nieco głębszej natury. Otóż, atrybut ``uploaded_file`` nie może być wymagalny, bo pierwszy zapis obiektu będzie się odbywał przed jego ustawieniem. Nietrudno wyobrazić sobie sytuację, kiedy takie wymaganie nie może zostać zaakceptowane z punktu widzenia logiki aplikacji. W takiej sytuacji trzeba spróbować z dynamicznym ustawianiem ścieżki, ale o tym traktuje :ref:`następny artykuł <ref-dynamic>`.