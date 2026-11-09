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

Der geplante Ablauf:

1. **Sammeln:** Fritz schreibt Notizen und legt sie in diesem Ordner ab.
2. **Zusammenfassen:** Claude fasst die Notizen zusammen.
3. **Vorlesen:** Die Zusammenfassung wird als Audio ausgegeben. Dieser Schritt kommt später.

Da die Zusammenfassung vorgelesen wird, muss sie auch beim Hören funktionieren: ganze Sätze und keine Tabellen, Symbole oder verschachtelten Listen.

## Entschieden

- **Notizen:** Jede Notiz ist eine eigene `.md`- oder `.txt`-Datei im Ordner `notizen/`.
- **Zeitraum:** Eine Zusammenfassung umfasst alle Notizen, die noch nicht zusammengefasst wurden. Danach werden sie nach `notizen/erledigt/` verschoben.
- **Zusammenfassungen:** Sie liegen in `zusammenfassungen/`.
- **Git:** In diesem Trainingsprojekt wird alles über Git synchronisiert, auch Notizen, Zusammenfassungen und später die Audiodateien.

## Noch nicht entschieden

Diese Punkte bitte mit Fritz klären, wenn sie relevant werden, und das Ergebnis hier eintragen:

- Wann genau werden die Notizen zusammengefasst? Bisher startet Fritz das von Hand mit dem Skill `/notizen-zusammenfassen`.
- Wo werden Audiodateien gespeichert?
- Womit wird das Audio erzeugt?
