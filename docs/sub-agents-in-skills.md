# Sub-Agents in Skills

Ein Sub-Agent ist ein eigener Helfer, dem Claude eine Aufgabe übergibt. Er arbeitet für sich und meldet am Ende nur sein Ergebnis zurück.

## Welche Agent-Typen es gibt

Die Liste hängt davon ab, welche Plugins installiert sind und welche eigenen Agents es gibt. Sie zeigt den Stand vom 9. November 2026. Den aktuellen Stand siehst du mit dem Befehl `/agents`.

### Eingebaute Agents

- `general-purpose`: der Allrounder, der recherchieren, Dateien ändern und mehrstufige Aufgaben erledigen kann.
- `Explore`: sucht schnell quer durch viele Dateien, ändert aber nichts.
- `Plan`: entwirft einen Umsetzungsplan und ändert ebenfalls nichts.
- `claude-code-guide`: beantwortet Fragen zu Claude Code und zur Claude-API.
- `statusline-setup`: richtet die Statuszeile ein, ist also sehr speziell.
- `claude`: ein Auffang-Agent für alles, wofür es keinen passenderen gibt.
- `fork`: eine Kopie der laufenden Sitzung, die den bisherigen Gesprächsverlauf kennt. Alle anderen starten ohne dieses Wissen und kennen nur ihren Auftrag.

### Eigene Agents

Eigene Agents liegen als Dateien im Ordner `.claude/agents/`. Dort wird auch festgelegt, welche Werkzeuge sie benutzen dürfen.

In diesem Projekt gibt es bisher keinen. Die Hörprobe war früher ein eigener Agent und ist jetzt der Skill `hoerprobe`.

### Agents aus Plugins

Sie heißen immer `plugin:agent`. Bisher kommen alle aus dem Plugin `agentheim`:

- `agentheim:architect`
- `agentheim:orchestrator`
- `agentheim:researcher`
- `agentheim:research-reviewer`
- `agentheim:strategic-modeler`
- `agentheim:tactical-modeler`
- `agentheim:verifier`
- `agentheim:worker`

## So nutzt du einen Agent im Skill

### Variante 1: Den Auftrag in den Skill-Text schreiben

Das ist der einfachste Weg. Der Skill läuft normal im Gespräch und gibt nur einen Teil der Arbeit ab:

```markdown
Starte für jede Notiz einen eigenen Subagenten vom Typ `general-purpose` und lass ihn die Notiz zusammenfassen.
```

So arbeitet `/notizen-zusammenfassen`.

### Variante 2: Den ganzen Skill als Sub-Agent laufen lassen

Dafür steht im Kopfbereich der `SKILL.md`, dass der Skill abgetrennt laufen soll und mit welchem Agent:

```yaml
---
name: mein-skill
description: ...
context: fork
agent: Explore
---
```

So arbeitet `/hoerprobe`. Der ganze Skill läuft abgetrennt, kennt das bisherige Gespräch nicht und prüft dadurch mit frischem Blick.

## Empfehlung für den Anfang

Nimm Variante 1, wenn der Skill nur einen Teil der Arbeit abgibt und das Gespräch danach weitergeht. Nimm Variante 2, wenn die ganze Aufgabe für sich stehen kann und nur das Ergebnis zählt.
