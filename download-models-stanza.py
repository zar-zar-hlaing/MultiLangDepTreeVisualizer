#pip install stanza
#pip install spacy-stanza

import os
import stanza
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
stanza_model_dir = os.path.join(BASE_DIR, "models", "stanza_models")

models = [
    "gl",
    "grc",
    "be",
    "lzh",
    "cop",
    "fo",
    "got",
    "is",
    "la",
    "lv",
    "mt",
    "pcm",
    "nn",
    "no",
    "sme",
    "cu",
    "fro",
    "orv",
    "sr",
    "hyw",
    "cy",
    "wo",
    "gd",
    "sa",
    "qtd",
    "ug",
]

for model in models:
    stanza.download(model, model_dir = stanza_model_dir)
