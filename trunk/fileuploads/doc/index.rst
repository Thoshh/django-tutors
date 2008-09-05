.. fileuploads documentation master file, created by sphinx-quickstart on Tue Sep  2 20:56:29 2008.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

============
Wprowadzenie
============

Żaden szanujący się serwis webowy nie może się obyć bez *uploadu* plików. Oczekuje się zwykle, że użytkownicy serwisu będą w znaczący sposób uczestniczyć w dostarczaniu zawartości, a do tego potrzebny jest wydajny i rozszerzalny sposób obsługi *uploadu* plików i następnie zarządzania dostarczoną zawartością.

Historycznie `Django <http://www.djangoproject.com/>`_ nie było najlepszym graczem na tym polu. Nie to, żeby *uploady* były traktowane po macoszemu - nie były one tej samej jakości, co reszta ramówki. Na usprawiedliwienie można przyjąć, że *upload* plików jest bardzo trudny i niewdzięczny do obsłużenia. Przez długi czas uploadowane pliki były następnie w całości ładowane do pamięci procesu serwera, niejednokrotnie powodując monstrualne zużycie zasobów. Jak kłopotliwe to może być, wiedzą wszyscy, którzy swoje serwisy hostują na współdzielonych serwerach z ograniczeniem zasobów. Innym ograniczeniem był sposób składowania dostarczonej zawartości - wyłącznie relatywnie do ustawienia ``MEDIA_ROOT``.

Na szczęście pod koniec *drogi do 1.0* Django uzyskało kilka rzeczy, które ułatwiają obsługę *uploadów*: *podłączalne* klasy zarządzające odbieraniem zawartości (*upload handlers*), dynamiczne generowanie ścieżek przechowywania zawartości, a także klasy realizujące przechowywanie obiektów (*storage classes*). Ten samouczek ma wprowadzić czytelnika w świat tych wszystkich nowości i sprawić, że przestaną być *dziwne*, a zaczną należeć do normalnej narzędziówki, używanej w codziennej pracy.

W kolejnych rozdziałach zostaną omówione zarówno tradycyjne sposoby uploadowania plików (odcinek 1), jak i bardziej *wykręcone*, np. z dynamicznym określaniem ścieżki (odcinek 2). W dalszych częściach opisane zostaną bardziej zaawansowane aspekty. W odcinku 3 omówione zostaną własne klasy zarządzające odbieraniem plików (*Upload Handlers*). Odcinek 4 zostanie poświęcony alternatywnym metodom przechowywania plików (*Storage Backends*).

Zawartość:

.. toctree::
   :maxdepth: 2
   
   tutorial/static.rst
   tutorial/dynamic.rst
   tutorial/handlers.rst
   tutorial/storage.rst

Indeksy i spisy
===============

* :ref:`search`

