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

UploadHandler
=============

Jest to klasa (dziedzicząca z :class:`django.core.files.uploadhandler.FileUploadHandler`), której zadaniem jest *zrobić coś z uploadowanymi danymi*. Domyślnie Django w ustawieniu :const:`settings.FILE_UPLOAD_HANDLERS` ma krotkę złożoną z dwóch klas: :class:`django.core.files.uploadhandler.MemoryFileUploadHandler` i :class:`django.core.files.uploadhandler.TemporaryFileUploadHandler`. Uploadowane dane przechodzą przez nie właśnie w tej kolejności i w zależności od funkcji mogą one zapisać gdzieś plik lub zrobić z coś innego z danymi (te dostarczane z Django odbierają dane i zapisują je we wskazanej lokalizacji jako plik).

Ponieważ czasem może być potrzeba obsłużenia uploadu w pojedynczym przypadku w inny sposób, obiekt ``request`` dostępny w każdym widoku w aplikacji Django (i w wielu innych miejscach również) posiada jako jeden ze swoich atrybutów listę handlerów, które mają obowiązywać podczas odbierania plików w wybranym fragmencie kodu. Dla bezpieczeństwa zwykle umieszcza się odpowiednią linię kodu na początku funkcji, ale ważne jest to, żeby lista handlerów została ustawiona zanim nasz kod spróbuje uzyskać dostęp do ``request.POST`` lub ``request.FILES`` (w tym momencie już jest *po ptokach*). Ponieważ jest to lista i klasy umieszczane w niej przetwarzają dane po kolei, zazwyczaj obiekty własnych klas handlerów umieszcza się na jej początku::

    request.upload_handlers.insert(0, LoggingUploadHandler())

Kod aplikacji
=============

Ponieważ głównym obiektem naszego zainteresowania nie są modele i ich zachowania, do przechowywania odebranych danych wykorzystany zostanie znana już funkcja :func:`static` z modułu :mod:`views`, ubierzemy ją tylko w trochę wrapującego kodu i umieścimy ją pod oddzielnym URL-em. Kod, który jest obiektem naszego zainteresowania to klasa :class:`LoggingUploadHandler` z modułu :mod:`files`. Implementuje ona wszystkie wymagane metody interfejsu klasy :class:`FileUploadHandler` (są to :meth:`FileUploadHandler.receive_data_chunk`, która odpowiada za odebranie danych i :meth:`FileUploadHandler.file_complete`, która kończy przetwarzanie odebranych danych) i dodatkowo kilka innych, które przydadzą się nam w dziele logowania (na :obj:`sys.stdout`) postępu odbierania pliku od serwera HTTP.

Wymagane metody
+++++++++++++++

.. method:: FileUploadHandler.receive_data_chunk(raw_data, start)

   Metoda odpowiada za odebranie kolejnego kawałka danych od serwera HTTP. Argument ``raw_data`` zawiera odebrane bajty, a argument ``start`` pozycję w strumieniu wejściowym. Wywoływana jest przy każdym odebranym fragmencie danych. Domyślnie ten *kawałek* będzie miał 64KB, ale we własnych klasach można to zmienić ustawiając inaczej wartość atrybutu :attr:`chunk_size`. Zwrócenie ``raw_data`` z tej metody spowoduje przekazanie przetwarzania fragmentu danych do kolejnego handlera, jeżeli natomiast w tej metodzie wywołany zostanie wyjątek :exc:`StopUpload` lub :exc:`SkipFile`, wtedy odbieranie danych zostanie przerwane (w drugim przypadku cała odebrana zawartość zostanie odrzucona).
 
.. method:: FileUploadHandler.file_complete(file_size)

   Metoda ta jest wywoływana po odebraniu wszystkich danych od serwera HTTP. Z tej metody trzeba zwrócić albo obiekt klasy :class:`UploadedFile` (i wtedy przetwarzanie się zakończy), albo ``None`` i wtedy rezultat uploadu zostanie zwrócony z kolejnych handlerów.

Metody opcjonalne
+++++++++++++++++

Nie będę opisywał tu wszystkich metod, a jedynie te, które zaimplementowane są w przykładowej klasie :class:`LoggingUploadHandler`, po dokładny opis całego interfejsu klasy odsyłam do `odpowiedniego rozdziału w dokumentacji Django <http://docs.djangoproject.com/en/dev/topics/http/file-uploads/#optional-methods>`_.

.. method:: FileUploadHandler.new_file(field_name, file_name, content_type, content_length, charset)

   Metoda ta jest wywoływana przed rozpoczęciem odbierania danych nowego pliku. W kodzie przykładowym jest używana do zresetowania licznika pobranych bajtów i ustawienia rozmiaru pobieraniego pliku.

.. method:: FileUploadHandler.handle_raw_input(input_data, META, content_length, boundary, encoding=None)

   Metoda ta umożliwia całkowite przechwycenie wszystkich danych i dowolną modyfikację procesu obsługi odebranego pliku. W kodzie przykładowym używana jest do ustawienia rozmiaru pobieranego pliku (inne miejsca nie są *godne zaufania*).

Spodziewany efekt i co można z tym zrobić?
++++++++++++++++++++++++++++++++++++++++++

Działanie aplikacji można zaobserwować w oknie terminala z uruchomionym serwerem developerskim Django - w miarę odbierania danych od serwera, aplikacja wypisuje postęp pobierania na standardowym wejściu.

A do czego może się nam to przydać? A chociażby do tego, żeby zrobić wskaźnik postępu uploadowania pliku (obiekt pożądania wielu developerów aplikacji webowych...).
