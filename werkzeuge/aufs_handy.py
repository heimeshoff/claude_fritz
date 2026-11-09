#!/usr/bin/env python3
"""Legt eine MP3-Datei in den Ordner, den Syncthing aufs Handy abgleicht.

    .venv/bin/python werkzeuge/aufs_handy.py audio/2026-11-09.mp3

Danach bleiben dort nur die neuesten Folgen liegen. Das Archiv in audio/ bleibt unberührt.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

PROJEKT = Path(__file__).resolve().parent.parent
AUDIO_ORDNER = PROJEKT / "audio"
HANDY_ORDNER = AUDIO_ORDNER / "handy"
ANZAHL_FOLGEN = 3


def abbrechen(meldung):
    print(f"Fehler: {meldung}", file=sys.stderr)
    sys.exit(1)


def kopieren(quelle):
    # Erst außerhalb des Abgleichordners kopieren: So schickt Syncthing nie eine halbe Datei los.
    zwischendatei = AUDIO_ORDNER / f".{quelle.stem}.handy.tmp"
    try:
        shutil.copyfile(quelle, zwischendatei)
        os.replace(zwischendatei, HANDY_ORDNER / quelle.name)
    finally:
        zwischendatei.unlink(missing_ok=True)


def aufraeumen():
    # Der Name beginnt mit dem Datum, also sortiert der Name auch nach Alter.
    folgen = sorted(HANDY_ORDNER.glob("*.mp3"), key=lambda datei: datei.stem)
    alte_folgen = folgen[:-ANZAHL_FOLGEN]
    for folge in alte_folgen:
        folge.unlink()
    return alte_folgen


def main():
    parser = argparse.ArgumentParser(description="Legt eine MP3-Datei in den Ordner fürs Handy.")
    parser.add_argument("mp3", type=Path, help="die MP3-Datei, zum Beispiel audio/2026-11-09.mp3")
    args = parser.parse_args()

    if not args.mp3.is_file():
        abbrechen(f"Die Datei gibt es nicht: {args.mp3}")
    # Den Ordner bewusst nicht selbst anlegen: Syncthing würde einen neuen, leeren Ordner nicht abgleichen.
    if not (HANDY_ORDNER / ".stfolder").exists():
        abbrechen(f"Der Syncthing-Ordner fehlt: {HANDY_ORDNER}")

    kopieren(args.mp3)
    print(f"Fürs Handy abgelegt: {HANDY_ORDNER / args.mp3.name}")
    for folge in aufraeumen():
        print(f"Vom Handy entfernt: {folge.name}")


if __name__ == "__main__":
    main()
