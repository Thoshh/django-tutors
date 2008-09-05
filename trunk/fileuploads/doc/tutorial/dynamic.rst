=============================
Dynamiczne określanie ścieżki
=============================

Od niedawna jako argument ``upload_to`` w konstruktorze ``FileField`` można podawać nazwę obiektu wykonywalnego, który przyjmując odpowiednie argumenty, zwróci ścieżkę, w której zostanie zapisany plik.