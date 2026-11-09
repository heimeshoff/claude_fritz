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

1. **Sammeln:** Fritz schreibt Notizen in Goodnotes auf dem iPad, exportiert sie als PDF oder PNG und legt sie vorerst von Hand in `notizen/` ab.
2. **Zusammenfassen:** Fritz sagt Claude, dass die Notizen zusammengefasst werden sollen.
3. **Morgenfolge:** Fritz startet `/morgen-folge`. Der Skill schreibt den Text, lässt ihn von der Hörprobe prüfen und legt die MP3 in `audio/` ab. Einzeln geht das Audio auch mit `.venv/bin/python werkzeuge/vorlesen.py`.
4. **Anhören:** Fritz spielt die MP3 selbst ab.

Da die Zusammenfassung vorgelesen wird, muss sie auch beim Hören funktionieren: ganze Sätze und keine Tabellen, Symbole oder verschachtelten Listen.

Fürs Lernen darf nichts Falsches hängen bleiben: Claude gibt nur wieder, was in den Notizen steht, ergänzt kein eigenes Rechtswissen und benennt Unklares als unklar.

## Entschieden

- **Notizen:** Sie liegen als `.pdf`, `.png`, `.md` oder `.txt` im Ordner `notizen/`. Eine Datei kann mehrere AG-Tage enthalten, denn das Datum steht meist oben auf der Seite. Fritz exportiert immer nur neue Seiten.
- **Zeitraum:** Eine Notiz wird einmal zu einer Tageszusammenfassung verarbeitet und danach nach `notizen/erledigt/` verschoben.
- **Zusammenfassungen in Stufen:** Sie liegen in `zusammenfassungen/`: `tage/` (ausführlich), `wochen/` und `monate/` (das Wichtigste) sowie `morgen/` (die fertige Folge).
- **Morgenfolge:** Sie wird täglich neu zusammengesetzt und dauert höchstens 30 Minuten, also etwa 4.000 Wörter. Sie ist nach Inhalten aufgebaut und nicht nach AG-Tagen: Was zusammengehört, steht zusammen, auch wenn es von verschiedenen Tagen stammt. AG-Tage werden dabei nicht genannt. Sie enthält nur Stoff aus den letzten sieben Tagen. Innerhalb dieser Zeit bestimmt das Alter nur die Ausführlichkeit: Die vier neuesten Tage mit Notizen kommen ausführlich, die übrigen nur mit den Kernpunkten. Zum Schluss kommen die offenen Fragen.
- **Tagesdateien:** Sie sind ein Zwischenschritt und werden nicht direkt angehört. Sie halten fest, wann welcher Stoff dran war, damit die Ausführlichkeit nach dem Alter berechnet werden kann.
- **Rückblick:** Noch nicht gebaut, Fritz hat das vorerst zurückgestellt. Wochen- und Monatsrückblicke soll es später nur auf Wunsch und nicht in der Morgenfolge geben. Auch darin wird nach Inhalten gegliedert.
- **Start:** Fritz startet die Skills vorerst von Hand. `/morgen-folge` erledigt danach Text, Prüfung und MP3 in einem Durchgang. Einen automatischen Start am Morgen gibt es erst, wenn er ihn möchte.
- **Stimme:** Das Audio erzeugt Piper mit der Stimme `de_DE-thorsten-medium`, kostenlos und lokal. Fritz hat sie im Hörtest bestätigt, auch die Aussprache von Paragrafen und Abkürzungen.
- **Audiodateien:** Sie liegen in `audio/` und kommen nicht in Git, weil das Repo sonst schnell um Gigabytes wächst. Sie lassen sich jederzeit aus den Texten neu erzeugen.
- **Git:** Code und Skills werden über Git versioniert. Echte Notizen und daraus entstandene Zusammenfassungen bleiben nur auf diesem Rechner und stehen in der `.gitignore`. Dafür gibt es keine Sicherung über GitHub.
- **Datenschutz:** Die Notizen enthalten nur AG-Stoff, also keine echten Namen oder Details aus Stationsakten. Das bleibt auch beim Mitschreiben die Regel.
- **Weg auf den Rechner:** Fritz legt die Goodnotes-Exporte weiter von Hand in `notizen/` ab. Automatisiert wird das erst, wenn es ihn im Alltag wirklich stört.
- **Laufort:** Claude und die Audioerzeugung laufen auf diesem Rechner. Das Handy spielt nur ab.
- **Endziel und Weg aufs Handy:** Später soll die Folge auf Fritz' Android-Handy laufen. Die fertige MP3 wird dafür automatisch in einen Ordner auf dem Handy kopiert, nur vom Rechner aufs Handy, und dort mit einer vorhandenen Player-App abgespielt. Rechner und Handy müssen dafür kurz gleichzeitig an und im selben WLAN sein. Eine eigene App oder Webseite ist nicht nötig.
- **Zeitpunkt:** Fritz startet `/morgen-folge` am Abend vor dem Hören, damit die Folge am Morgen schon auf dem Handy liegt. Der Stichtag bleibt der Tag der Erzeugung, also auch das Datum im Dateinamen. Dass der Stoff beim Hören dadurch einen Tag weiter zurückreicht, ist in Ordnung.

## Noch nicht entschieden

Diese Punkte bitte mit Fritz klären, wenn sie relevant werden, und das Ergebnis hier eintragen:

- Mit welchem Programm wird der Ordner auf das Handy kopiert, und mit welcher Player-App hört Fritz? Syncthing und AntennaPod sind Kandidaten. Für Syncthing muss vorher geklärt werden, welche Android-Version noch gepflegt wird.
- Wie bleiben alte Folgen vom Handy fern? Naheliegend ist ein eigener Abgleichordner nur mit den letzten paar Folgen statt des ganzen Ordners `audio/`.
