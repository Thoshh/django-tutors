.. _ref-storage:

****************************************
Przechowywanie plików (Storage Backends)
****************************************

Wraz z wydaniem wersji 1.0 trwałe dane o charakterze plikowym nie muszą już być przechowywane w lokalnie dostępnym systemie plików, w lokalizacji relatywnej do :const:`settings.MEDIA_ROOT`. Wraz z przebudową podsystemu przechowywania programiści uzyskali pełną kontrolę nad tym, gdzie umieścić zasób tak, by aplikacja była w stanie go udostępnić. Od wersji 1.0 nie ma żadnych przeszkód, aby zasoby przechowywać w zewnętrznych systemach, jak różnego rodzaju systemy CDN (*Content Delivery Network*) czy popularna usługa Amazon S3 (*Simple Storage Service*).

Zagadnienie to nie należy do podstawowych i mogę się założyć, że większość programistów rzadko będzie się z nim stykała, przynajmniej do momentu kiedy ich serwisy zaczną wymagać tego, by ich zasoby dostarczać w taki właśnie sposób (jak się można domyślić, małych serwisów na pewno to nie dotyczy). Warto jednak zapoznać się z tym zagadnieniem, choćby po to, by wiedzieć jak ramówka zarządza przechowywaniem i udostępnianiem zasobów plikowych.

W przykładowym kodzie zaimplementujemy specjalny system przechowywania plików, który zachowuje je w postaci strumienia binarnego w *zamarynowanym* (pickled) słowniku. Bez sensu? Owszem, ale przynajmniej będzie widać, jak się to robi.
