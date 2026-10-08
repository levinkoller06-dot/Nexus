# Erzeugt die Sprecherspur lokal mit Piper (deutsche Stimme "Thorsten"), keine Cloud.
import json, subprocess, wave, sys, os
from piper import PiperVoice
LINES = json.load(open('narration.json', encoding='utf-8'))
voice = PiperVoice.load('voice_models/de_DE-thorsten-medium.onnx')
os.makedirs('out/voice', exist_ok=True)
for k, text in LINES.items():
    with wave.open(f'out/voice/{k}.wav', 'wb') as w:
        voice.synthesize_wav(text, w)
    with wave.open(f'out/voice/{k}.wav') as w: print(k, round(w.getnframes()/w.getframerate(),2))
