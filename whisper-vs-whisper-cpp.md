# Comparing Whisper to Whisper.cpp

## Setup Whisper

```bash
poetry install
poetry run whisper --model base.en --model_dir models/ --output_format txt --output_dir sample/ sample/jfk.wav
```

## Setup Whisper.cpp

```bash
docker run -it --rm \
  -v $PWD/models:/models \
  ghcr.io/ggerganov/whisper.cpp:main \
  "./models/download-ggml-model.sh base.en /models"
```

## Transcribe jfk.wav

The following was performed on a computer with these specs:
- Linux x86_64
- 32 GB memory
- AMD Ryzen 7 6800U with Radeon Graphics
- No GPU

To give a rough idea of what kind of performance to expect.

Whisper:
```bash
$ time poetry run whisper --model base.en --model_dir models/ --output_format txt --output_dir sample/ sample/jfk.wav
...
[00:00.000 --> 00:11.000]  And so my fellow Americans, ask not what your country can do for you, ask what you can do for your country.
...
real    0m3.771s
user    0m14.755s
sys     0m2.223s
```
Whisper.cpp is about twice as fast:
```bash
$ time docker run -it --rm \
  -v $PWD/models:/models \
  -v $PWD/sample:/audios \
  ghcr.io/ggerganov/whisper.cpp:main \
  "./main -m /models/ggml-base.en.bin -f /audios/jfk.wav"

...
[00:00:00.000 --> 00:00:11.000]   And so my fellow Americans, ask not what your country can do for you, ask what you can do for your country.
...
real    0m1.813s
user    0m0.006s
sys     0m0.014s
```
