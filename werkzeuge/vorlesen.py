#!/usr/bin/env python3
"""Macht aus einer Textdatei eine MP3-Datei.

Neueste Morgenfolge vorlesen:
    .venv/bin/python werkzeuge/vorlesen.py

Bestimmte Textdatei vorlesen:
    .venv/bin/python werkzeuge/vorlesen.py zusammenfassungen/morgen/2026-11-09.md

Ohne Angabe eines Ziels landet die Audiodatei in audio/.
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

PROJEKT = Path(__file__).resolve().parent.parent
MORGEN_ORDNER = PROJEKT / "zusammenfassungen" / "morgen"
AUDIO_ORDNER = PROJEKT / "audio"

# Diese Werte kannst du nach dem Hörtest anpassen.
STIMME = PROJEKT / "stimmen" / "de_DE-thorsten-medium.onnx"
TEMPO = 0.85  # 1.0 ist normal, größer ist langsamer, kleiner ist schneller
PAUSE_SATZ = 0.35  # Sekunden zwischen zwei Sätzen
PAUSE_ABSATZ = 0.9  # Sekunden zwischen zwei Absätzen
MP3_BITRATE = "64k"  # reicht für Sprache und hält die Datei klein


def abbrechen(meldung):
    print(f"Fehler: {meldung}", file=sys.stderr)
    sys.exit(1)


def neueste_folge():
    folgen = sorted(MORGEN_ORDNER.glob("*.md"), key=lambda datei: datei.stem)
    if not folgen:
        abbrechen(f"In {MORGEN_ORDNER} liegt noch keine Morgenfolge.")
    return folgen[-1]


def vorlesen(text, ziel):
    # Die Vorlese-Software steckt in .venv, deshalb wird sie erst hier geladen.
    try:
        from piper import PiperVoice, SynthesisConfig
    except ImportError:
        abbrechen("Piper fehlt. Starte das Skript mit: .venv/bin/python werkzeuge/vorlesen.py")

    if not STIMME.exists():
        abbrechen(f"Die Stimme fehlt: {STIMME}")

    stimme = PiperVoice.load(str(STIMME))
    einstellungen = SynthesisConfig(length_scale=TEMPO)
    abtastrate = stimme.config.sample_rate

    # Erst in eine Zwischendatei schreiben: Bricht etwas ab, bleibt keine kaputte MP3 zurück.
    zwischendatei = ziel.with_name(f".{ziel.stem}.tmp.mp3")
    ffmpeg = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error",
         "-f", "s16le", "-ar", str(abtastrate), "-ac", "1", "-i", "-",
         "-codec:a", "libmp3lame", "-b:a", MP3_BITRATE, str(zwischendatei)],
        stdin=subprocess.PIPE,
    )

    def stille(sekunden):
        # Eine Probe ist zwei Bytes groß.
        return b"\x00\x00" * int(abtastrate * sekunden)

    absaetze = [a.strip() for a in re.split(r"\n\s*\n", text) if a.strip()]
    bytes_gesamt = 0
    try:
        for nummer, absatz in enumerate(absaetze, start=1):
            print(f"Absatz {nummer} von {len(absaetze)} ...", flush=True)
            for teil in stimme.synthesize(" ".join(absatz.split()), syn_config=einstellungen):
                daten = teil.audio_int16_bytes + stille(PAUSE_SATZ)
                ffmpeg.stdin.write(daten)
                bytes_gesamt += len(daten)
            pause = stille(PAUSE_ABSATZ)
            ffmpeg.stdin.write(pause)
            bytes_gesamt += len(pause)
        ffmpeg.stdin.close()
        fehlercode = ffmpeg.wait()
    except BaseException:
        ffmpeg.kill()
        ffmpeg.wait()
        zwischendatei.unlink(missing_ok=True)
        raise

    if fehlercode != 0:
        zwischendatei.unlink(missing_ok=True)
        abbrechen("ffmpeg konnte die MP3-Datei nicht erzeugen.")

    os.replace(zwischendatei, ziel)
    return bytes_gesamt / 2 / abtastrate


def main():
    parser = argparse.ArgumentParser(description="Macht aus einer Textdatei eine MP3-Datei.")
    parser.add_argument("text", nargs="?", type=Path,
                        help="Textdatei, ohne Angabe die neueste Morgenfolge")
    parser.add_argument("ziel", nargs="?", type=Path,
                        help="MP3-Datei, ohne Angabe in audio/ unter dem Namen der Textdatei")
    args = parser.parse_args()

    quelle = args.text or neueste_folge()
    if not quelle.is_file():
        abbrechen(f"Die Datei gibt es nicht: {quelle}")

    text = quelle.read_text(encoding="utf-8")
    if not text.strip():
        abbrechen(f"Die Datei ist leer: {quelle}")

    ziel = args.ziel or AUDIO_ORDNER / f"{quelle.stem}.mp3"
    ziel.parent.mkdir(parents=True, exist_ok=True)

    print(f"Lese vor: {quelle}")
    dauer = vorlesen(text, ziel)
    print(f"Fertig: {ziel}")
    print(f"Länge: etwa {round(dauer / 60)} Minuten")


if __name__ == "__main__":
    main()
