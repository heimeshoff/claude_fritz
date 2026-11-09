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

Den Ablauf und alles, was noch gebaut werden soll, findest du in `PLAN.html`. Einzeln lässt sich das Audio mit `.venv/bin/python werkzeuge/vorlesen.py` erzeugen.

Da die Zusammenfassung vorgelesen wird, muss sie auch beim Hören funktionieren: ganze Sätze und keine Tabellen, Symbole oder verschachtelten Listen.

Fürs Lernen darf nichts Falsches hängen bleiben: Claude gibt nur wieder, was in den Notizen steht, ergänzt kein eigenes Rechtswissen und benennt Unklares als unklar.

## Der Plan: `PLAN.html`

`PLAN.html` ist die zentrale Quelle für alle Feature-Planungen. Sie enthält den groben Ablauf, die Meilensteine und deren Aufgaben zum Abhaken. Künftige Vorhaben und offene Entscheidungen stehen nur dort und nicht in dieser Datei.

- Lies `PLAN.html`, bevor du mit Fritz ein Feature planst oder mit einem neuen Schritt beginnst.
- Hake eine Aufgabe von dir aus ab, sobald sie wirklich erledigt ist. Offenes bleibt unmarkiert.
- Trage Ergebnisse aus Planungsgesprächen direkt ein, also neue Aufgaben, neue Meilensteine und getroffene Entscheidungen.
- Wie die Datei zu bearbeiten ist, steht in einem Kommentar am Anfang von `PLAN.html`.
- Regeln, die für den laufenden Betrieb dauerhaft gelten, kommen zusätzlich hierher, sobald das Feature fertig ist.

## Entschieden

- **Notizen:** Sie liegen als `.pdf`, `.png`, `.md` oder `.txt` im Ordner `notizen/`. Eine Datei kann mehrere AG-Tage enthalten, denn das Datum steht meist oben auf der Seite. Fritz exportiert immer nur neue Seiten.
- **Zeitraum:** Eine Notiz wird einmal zu einer Tageszusammenfassung verarbeitet und danach nach `notizen/erledigt/` verschoben.
- **Zusammenfassungen in Stufen:** Sie liegen in `zusammenfassungen/`: `tage/` (ausführlich) und `morgen/` (die fertige Folge).
- **Morgenfolge:** Sie wird täglich neu zusammengesetzt und dauert höchstens 30 Minuten, also etwa 4.000 Wörter. Sie ist nach Inhalten aufgebaut und nicht nach AG-Tagen: Was zusammengehört, steht zusammen, auch wenn es von verschiedenen Tagen stammt. AG-Tage werden dabei nicht genannt. Sie enthält nur Stoff aus den letzten sieben Tagen. Innerhalb dieser Zeit bestimmt das Alter nur die Ausführlichkeit: Die vier neuesten Tage mit Notizen kommen ausführlich, die übrigen nur mit den Kernpunkten. Zum Schluss kommen die offenen Fragen.
- **Tagesdateien:** Sie sind ein Zwischenschritt und werden nicht direkt angehört. Sie halten fest, wann welcher Stoff dran war, damit die Ausführlichkeit nach dem Alter berechnet werden kann.
- **Start:** Fritz startet die Skills von Hand. `/morgen-folge` erledigt danach Text, Prüfung und MP3 in einem Durchgang.
- **Stimme:** Das Audio erzeugt Piper mit der Stimme `de_DE-thorsten-medium`, kostenlos und lokal. Fritz hat sie im Hörtest bestätigt, auch die Aussprache von Paragrafen und Abkürzungen.
- **Audiodateien:** Sie liegen in `audio/` und kommen nicht in Git, weil das Repo sonst schnell um Gigabytes wächst. Sie lassen sich jederzeit aus den Texten neu erzeugen.
- **Git:** Code und Skills werden über Git versioniert. Echte Notizen und daraus entstandene Zusammenfassungen bleiben nur auf diesem Rechner und stehen in der `.gitignore`. Dafür gibt es keine Sicherung über GitHub.
- **Datenschutz:** Die Notizen enthalten nur AG-Stoff, also keine echten Namen oder Details aus Stationsakten. Das bleibt auch beim Mitschreiben die Regel.
- **Weg auf den Rechner:** Fritz legt die Goodnotes-Exporte von Hand in `notizen/` ab.
- **Laufort:** Claude und die Audioerzeugung laufen auf diesem Rechner. Das Handy spielt nur ab.
- **Zeitpunkt:** Fritz startet `/morgen-folge` am Abend vor dem Hören, damit die Folge am Morgen schon auf dem Handy liegt. Der Stichtag bleibt der Tag der Erzeugung, also auch das Datum im Dateinamen. Dass der Stoff beim Hören dadurch einen Tag weiter zurückreicht, ist in Ordnung.
