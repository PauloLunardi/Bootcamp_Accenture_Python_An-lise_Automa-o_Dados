# speech_recognition precisa ser instalado por padrão no ambiente

Instale o pacote no seu ambiente local (Windows/Linux/Mac):

    !pip install SpeechRecognition
    !pip install pyaudio

No Windows, às vezes é preciso instalar o PyAudio via binário .whl (porque a compilação falha).

Exemplo: baixar de PyAudio wheels e instalar com:

    pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl

Depois rode o script no VS Code ou no terminal, aí sim o microfone funciona.
