# Werkzeuge

Python-Skripte, mit denen die Videos in `hyperframes-studio/` gebaut wurden.
Sie wurden in einer temporären Cloud-Sitzung geschrieben. Die Pfade darin
zeigen auf den damaligen Arbeitsordner und müssen vor einer neuen Nutzung
angepasst werden.

## Figuren und Grafik
- `kurt.py`: Käpt'n Kurt, die gezeichnete Erzählerfigur (SVG). Mund, Augenlider und Arme sind animierbar.
- `bee.py`: die räumlich schattierte Biene für das HABEE-Video (SVG, Flügel animierbar).

## Musik und Sound (synthetisch erzeugt, numpy)
- `synth.py`: Beat für das Claude-Video mit 16 Szenen
- `music4.py`: Musik für Claude-Intro v4 (Drop, Sidechain, Hall)
- `music5.py`: Musik für die HABEE-Videos
- `music_bloom.py`: ruhige Chill-Musik mit E-Piano für Bloom Hair & Nails
- `music_porsche.py`: Elektro-Trailer-Musik mit wechselnden Übergängen für Porsche
- `buzz.py`: Bienensummen, das der Flugbahn folgt

## Szenen-Generatoren (erzeugen die index.html der Projekte)
- `gen4.py`: claude-intro-v4
- `gen_habee.py`, `gen_habee2.py`: habee-video und habee-video-v2
- `gen_bloom.py`: mybloom-video
- `gen_titanic.py` und `titanic.css`: titanic-erklaerfilm
- `gen_porsche.py`: porsche-werbung

## titanic-ton/
- `script.py`: Sprechtext und Untertitel des Titanic-Films
- `build_audio.py`: setzt die Sprachaufnahmen zusammen, berechnet die Mundbewegung und das Timing der Untertitel
- `score.py`: Filmmusik und Geräusche des Titanic-Films

Die deutsche Stimme stammt aus Piper (`pip install piper-tts`), Stimme
`de_DE-thorsten-high` von huggingface.co/rhasspy/piper-voices.

## iPhone-20-Konzept
- `iphone_phone3d.py`: das 3D-iPhone aus CSS-3D-Ebenen, drehbar, in fünf Farben (Mitternacht, Polarweiss, Gletscherblau, Sandstein, Salbei)
- `gen_iphone.py`: die 16 Szenen des iPhone-20-Konzeptvideos, auf die Takte des Songs gelegt (119 BPM)
