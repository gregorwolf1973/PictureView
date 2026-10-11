# Changelog

## 0.11

- Oberfläche für das Handy überarbeitet: einspaltige Ansicht, große
  Navigationsbuttons ohne Beschriftung, Wischen auf dem Bild (links = älter,
  rechts = neuer), Zeitleiste als aufklappbares Bottom-Sheet.
- Bilder starten immer beim neuesten Bild. „Älter“ und „Neuer“ laufen streng
  chronologisch durch alle Bilder, ohne Sprung zwischen den Tagen. Die
  Zeitleiste zeigt Tage und Bilder in derselben Reihenfolge (neueste zuerst).
- Dateinamen werden nicht mehr angezeigt. Stattdessen stehen Uhrzeit und Datum
  (mit „Heute“/„Gestern“) über dem Bild und in der Zeitleiste.
- Tastatur: → älter, ← neuer, Pos1 neuestes, Ende ältestes, Esc schließt die
  Zeitleiste.
- Beim automatischen Nachladen bleibt das angezeigte Bild ausgewählt, auch wenn
  neue Bilder dazugekommen sind; die Statistik im Kopf wird mit aktualisiert.

## 0.10

- Pillow wird nicht mehr installiert. Die Bibliothek wurde im Addon nirgends
  verwendet; das Image wird dadurch kleiner und baut schneller.
- Basis-Image von Alpine 3.19 auf Alpine 3.22 gehoben (Python bleibt 3.12).
- Versionsangaben in den README-Dateien auf den aktuellen Stand gebracht.
