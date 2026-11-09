# CLAUDE.md

## Worum es hier geht

Dieser Ordner ist ein Workshop: **Fritz lernt, mit Claude Code zu arbeiten.** Das ist das eigentliche Ziel.

Das Notiz-Tool unten ist nur das Übungsobjekt. Im Zweifel gilt: Lieber versteht Fritz einen Schritt wirklich, als dass das Tool schneller fertig wird.

## So arbeitest du hier mit Fritz

- Sprich Deutsch mit ihm, locker und ohne unnötigen Fachjargon.
- Erkläre kurz, was du tust und warum, besonders beim ersten Auftreten eines Konzepts (z. B. Commit, Branch, Berechtigungsabfrage, Skill).
- Bau in kleinen Schritten, die er nachvollziehen und ausprobieren kann, statt alles auf einmal zu liefern.
- Wenn er selbst etwas ausprobieren kann, zeig ihm, wie es geht, statt es still für ihn zu erledigen.
- Wenn eine seiner Anweisungen unklar war, sag ihm, was du daran unklar fandest. So lernt er, gute Anweisungen zu formulieren.
- Fehler sind Lernstoff: Erkläre, was schiefging, bevor du es behebst.

## Das Übungsprojekt: Notizen zum Anhören

Fritz ist im juristischen Referendariat und schreibt an AG-Tagen Notizen zu den jeweils vierstündigen AG-Stunden. Daraus soll eine tägliche Audiofolge zum Wiederholen entstehen.

Der geplante Ablauf:

1. **Sammeln:** Fritz tippt Notizen auf dem iPad und legt sie vorerst von Hand in `notizen/` ab.
2. **Zusammenfassen:** Fritz sagt Claude, dass die Notizen zusammengefasst werden sollen.
3. **Vorlesen:** Fritz startet die Audioerzeugung selbst und spielt die Datei ab.

Da die Zusammenfassung vorgelesen wird, muss sie auch beim Hören funktionieren: ganze Sätze und keine Tabellen, Symbole oder verschachtelten Listen.

Fürs Lernen darf nichts Falsches hängen bleiben: Claude gibt nur wieder, was in den Notizen steht, ergänzt kein eigenes Rechtswissen und benennt Unklares als unklar.

## Entschieden

- **Notizen:** Jede Notiz ist eine eigene `.md`- oder `.txt`-Datei im Ordner `notizen/`. Ihr Dateiname beginnt mit dem Datum, zum Beispiel `2026-11-09-schuldrecht.md`.
- **Zeitraum:** Eine Notiz wird einmal zu einer Tageszusammenfassung verarbeitet und danach nach `notizen/erledigt/` verschoben.
- **Zusammenfassungen in Stufen:** Sie liegen in `zusammenfassungen/`: `tage/` (ausführlich), `wochen/` und `monate/` (das Wichtigste) sowie `morgen/` (die fertige Folge).
- **Morgenfolge:** Sie wird täglich neu zusammengesetzt und dauert höchstens 30 Minuten, also etwa 4.000 Wörter. Die letzten vier Tage mit Notizen kommen ausführlich, ältere Tage derselben Woche nur mit den Kernpunkten, danach ein Rückblick auf frühere Wochen und den letzten Monat und zum Schluss die offenen Fragen.
- **Rückblick:** Fritz kann gezielt die wichtigsten Inhalte einer bestimmten Woche oder eines Monats abrufen.
- **Start:** Fritz startet vorerst alles von Hand. Einen automatischen Start gibt es erst, wenn er ihn möchte.
- **Audiodateien:** Sie liegen in `audio/` und kommen nicht in Git, weil das Repo sonst schnell um Gigabytes wächst. Sie lassen sich jederzeit aus den Texten neu erzeugen.
- **Git:** Code, Skills und Testdaten werden über Git versioniert. Echte Notizen und daraus entstandene Zusammenfassungen werden nicht zu GitHub hochgeladen, solange die Datenschutzfrage unten offen ist.
- **Endziel:** Später soll die Folge auf Fritz' Android-Handy laufen. Das Handy spielt nur ab, Claude und die Audioerzeugung laufen woanders.

## Noch nicht entschieden

Diese Punkte bitte mit Fritz klären, wenn sie relevant werden, und das Ergebnis hier eintragen:

- Können in den Notizen echte Namen oder Details aus Stationsakten vorkommen? Wer kann das GitHub-Repo sehen? Das muss vor dem iPad-Abgleich geklärt sein.
- Womit wird das Audio endgültig erzeugt? Zuerst testen wir Piper, eine kostenlose Stimme, die lokal läuft.
- Mit welcher App schreibt Fritz auf dem iPad, und wie kommen die Notizen später automatisch auf den Rechner?
- Wo laufen Claude und die Audioerzeugung später, und wird die Android-App eine installierbare Webseite oder eine richtige App?
