# Dependency Tree Visualizer Tool

The **Dependency Tree Visualizer Tool** processes multilingual text or files to generate **syntactic dependency trees** for each sentence. It highlights the grammatical relationships between tokens (words) using Universal POS (UPOS) tags and provides **fully color-coded SVG visualizations**. The tool supports **over 70 languages** using spaCy, spaCy-UDPipe, spaCy-Stanza, and spaCy-Thai, depending on the language and availability of models. It is designed for large-scale text processing, allowing integration with other NLP pipelines and real-time visualization.

---

## Key Features

### Flexible Input Handling

* Processes both single-line text and multi-line text files with ease.

### Large Text Support

* Handles very large texts (up to 2,000,000 characters) without errors (`nlp.max_length = 2_000_000`).

### Optional Preprocessing

* Supports merging of **noun chunks** and **punctuation spans** to simplify dependency trees for clearer visualization.

### Color-Coded Dependency Trees

* Generates SVG dependency trees with color-coded Universal POS tags for each sentence.

### Pipeline Integration

* Integrates seamlessly with existing NLP pipelines to enhance downstream tasks such as:

  * **POS Tagging**: Validate and debug automated part-of-speech assignments.
  * **Named Entity Recognition (NER)**: Disambiguate entities using syntactic relationships.
  * **Sentiment Analysis**: Analyze modifier-target relationships for aspect-based sentiment.
  * **Lemmatization & Morphology**: Verify correct base forms in context-sensitive scenarios.
  * **Feature Engineering**: Extract syntactic structures (subject-verb-object, head-modifier pairs) for ML models.

### Visualization-Ready

* Preprocessing options like noun chunk and punctuation merging provide clean, readable SVGs suitable for reporting, dashboards, or presentations.

---

## Supported Languages & Pipelines

| No. | Language Code         | Language            | Pipeline   | Noun Chunk Merge |
| --- | --------------------- | ------------------- | ---------- | ---------------- |
| 1   | af                    | Afrikaans           | UDPipe     | ❌                |
| 2   | ar                    | Arabic              | UDPipe     | ❌                |
| 3   | hy                    | Armenian            | UDPipe     | ❌                |
| 4   | eu                    | Basque              | UDPipe     | ❌                |
| 5   | bg                    | Bulgarian           | UDPipe     | ❌                |
| 6   | ca                    | Catalan             | spaCy      | ✅                |
| 7   | zh / zh-hans / zh-cn  | Simplified Chinese  | spaCy      | ❌                |
| 8   | zht / zh-hant / zh-hk | Traditional Chinese | UDPipe     | ❌                |
| 9   | hr                    | Croatian            | spaCy      | ❌                |
| 10  | cs                    | Czech               | UDPipe     | ❌                |
| 11  | da                    | Danish              | spaCy      | ❌                |
| 12  | nl                    | Dutch               | spaCy      | ✅                |
| 13  | en                    | English             | spaCy      | ✅                |
| 14  | et                    | Estonian            | UDPipe     | ❌                |
| 15  | fi                    | Finnish             | spaCy      | ❌                |
| 16  | fr                    | French              | spaCy      | ❌                |
| 17  | de                    | German              | spaCy      | ❌                |
| 18  | el                    | Greek               | spaCy      | ✅                |
| 19  | gl                    | Galician            | Stanza     | ❌                |
| 20  | grc                   | Ancient Greek       | Stanza     | ❌                |
| 21  | be                    | Belarusian          | Stanza     | ❌                |
| 22  | lzh                   | Classical Chinese   | Stanza     | ❌                |
| 23  | cop                   | Coptic              | Stanza     | ❌                |
| 24  | fo                    | Faroese             | Stanza     | ❌                |
| 25  | got                   | Gothic              | Stanza     | ❌                |
| 26  | is                    | Icelandic           | Stanza     | ❌                |
| 27  | la                    | Latin               | Stanza     | ❌                |
| 28  | lv                    | Latvian             | UDPipe     | ❌                |
| 29  | mt                    | Maltese             | Stanza     | ❌                |
| 30  | pcm                   | Naija               | Stanza     | ❌                |
| 31  | nn                    | Norwegian Nynorsk   | Stanza     | ❌                |
| 32  | no                    | Norwegian           | Stanza     | ❌                |
| 33  | sme                   | North Sami          | Stanza     | ❌                |
| 34  | cu                    | Old Church Slavonic | Stanza     | ❌                |
| 35  | fro                   | Old French          | Stanza     | ❌                |
| 36  | orv                   | Old East Slavic     | Stanza     | ❌                |
| 37  | sr                    | Serbian             | Stanza     | ❌                |
| 38  | gd                    | Scottish Gaelic     | Stanza     | ❌                |
| 39  | sa                    | Sanskrit            | Stanza     | ❌                |
| 40  | qtd                   | Turkish German      | Stanza     | ❌                |
| 41  | hyw                   | Western Armenian    | Stanza     | ❌                |
| 42  | cy                    | Welsh               | Stanza     | ❌                |
| 43  | wo                    | Wolof               | Stanza     | ❌                |
| 44  | ug                    | Uyghur              | Stanza     | ❌                |
| 45  | he                    | Hebrew              | UDPipe     | ❌                |
| 46  | hi                    | Hindi               | UDPipe     | ❌                |
| 47  | hu                    | Hungarian           | UDPipe     | ❌                |
| 48  | id / ms               | Indonesian / Malay  | UDPipe     | ❌                |
| 49  | ga                    | Irish               | UDPipe     | ❌                |
| 50  | it                    | Italian             | spaCy      | ✅                |
| 51  | ja                    | Japanese            | spaCy      | ✅                |
| 52  | ko                    | Korean              | spaCy      | ✅                |
| 53  | lt                    | Lithuanian          | spaCy      | ❌                |
| 54  | mk                    | Macedonian          | spaCy      | ❌                |
| 55  | mr                    | Marathi             | UDPipe     | ❌                |
| 56  | nb                    | Norwegian           | spaCy      | ❌                |
| 57  | fa                    | Persian             | UDPipe     | ✅                |
| 58  | pl                    | Polish              | spaCy      | ❌                |
| 59  | pt / pt-br / pt-pt    | Portuguese          | spaCy      | ❌                |
| 60  | ro                    | Romanian            | spaCy      | ❌                |
| 61  | ru                    | Russian             | spaCy      | ❌                |
| 62  | sk                    | Slovak              | UDPipe     | ❌                |
| 63  | sl                    | Slovenian           | UDPipe     | ❌                |
| 64  | es                    | Spanish             | spaCy      | ❌                |
| 65  | sv                    | Swedish             | spaCy      | ❌                |
| 66  | ta                    | Tamil               | UDPipe     | ❌                |
| 67  | te                    | Telugu              | UDPipe     | ❌                |
| 68  | th                    | Thai                | spaCy-Thai | ❌                |
| 69  | tr                    | Turkish             | UDPipe     | ✅                |
| 70  | uk                    | Ukrainian           | spaCy      | ❌                |
| 71  | ur                    | Urdu                | UDPipe     | ❌                |
| 72  | vi                    | Vietnamese          | UDPipe     | ❌                |

---

## Workflow Overview

1. **Load Language Model**

   * Based on the `--lang` argument, the tool loads the appropriate NLP pipeline:

     * spaCy core models for modern, high-resource languages
     * spaCy-UDPipe for additional languages
     * spaCy-Stanza for historical/low-resource languages
     * spaCy-Thai for Thai text

2. **Merge Phrases and Entities**

   * Applies `merge_noun_chunks` and `merge_entities` if `merge_chunks_state` is enabled
   * Skips languages that do not support noun chunk merging

3. **Token-level Parsing**

   * Generates raw tokenized output
   * Optionally merges noun chunks and/or entities
   * Optionally merges punctuation spans

4. **Dependency Tree Visualization**

   * Generates SVG visualizations via `displacy.render()`
   * Supports custom UPOS color mapping
   * Options:

     * `merge_punct`: collapse consecutive punctuation
     * `collapse_phrases`: collapse noun chunks and entities
     * `compact`: compact layout
     * `bg`: background color
     * `color`: text color

---

## Configuration Parameters

| Parameter              | Description                                           | Default / Notes                                                                 |
| ---------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------- |
| lang                   | Language code to determine pipeline                   | Provided via `--lang` argument                                                 |
| merge_chunks           | 0 (disabled) or 1 (enabled); merges noun chunks       | Provided via `--merge_chunks` argument; default = 1                             |
| merge_punct            | 0 (disabled) or 1 (enabled); merges punctuation spans | Provided via `--merge_punct` argument; default = 0                              |
| stanza_model_dir       | Directory for Stanza models                           | `/opt/omniscien/tools/wfs/syntaxparser/stanza_models/`                         |
| nlp.max_length         | Maximum text length                                   | 2,000,000 characters                                                            |
| noun_chunks_langLst    | Languages supporting noun chunk merging               | See script (e.g., ['ca', 'nl', 'en', 'el', 'it', 'ja', 'fa', 'tr', ...])       |
| no_noun_chunks_langLst | Languages without noun chunk merging                  | See script (e.g., ['de', 'es', 'fr', 'pt', 'sv', 'no', 'fi', 'da', ...])       |
| stdin_markers          | Input type detection                                  | `@LSFILEPATHLS@` (file input), `@LSENDOFFTEXTINPUTLS@` (direct text input)     |


---

## Requirements

### Python Version

* Python 3.9+ (recommended)

### Dependencies

```bash
pip install spacy spacy-udpipe spacy-stanza spacy-thai stanza
```

**Notes:**

* Stanza models should be pre-downloaded in `stanza_model_dir`.
* Thai processing requires `spacy_thai`.

### Pre-download Models

Before running the **Multilingual Syntax Tree Visualizer**, you must pre-download the required models.  
These scripts only need to be run **once**.

---

#### 1. spaCy Core Models

**Script:** `download-models-spacy.sh`

```bash
#!/bin/bash

models=(
"ca_core_news_sm" "zh_core_web_sm" "hr_core_news_sm" "da_core_news_sm"
"nl_core_news_sm" "en_core_web_sm" "fi_core_news_sm" "fr_core_news_sm"
"de_core_news_sm" "el_core_news_sm" "it_core_news_sm" "ja_core_web_sm"
"ko_core_news_sm" "mk_core_news_sm" "nb_core_news_sm" "pl_core_news_sm"
"pt_core_news_sm" "ro_core_news_sm" "ru_core_news_sm" "es_core_news_sm"
"sv_core_news_sm" "uk_core_news_sm"
)

for model in "${models[@]}"; do
  python3 -m spacy download "$model"
done
```

**Description:**  
High-resource language models for spaCy.

**Usage:**

```bash
bash download-models-spacy.sh
```

---

#### 2. spaCy-UDPipe Models

**Script:** `download-models-spacy-udpipe.sh`

```bash
#!/bin/bash

models=("af" "ar" "hy" "eu" "zh" "he" "hi" "hu"
        "id" "ga" "lv" "mr" "fa" "sk" "sl"
        "ta" "te" "tr" "ur" "vi")

for model in "${models[@]}"; do
   python3 -c "import spacy_udpipe; spacy_udpipe.download('$model')"
done
```

**Description:**  
Additional language models for spaCy-UDPipe (mainly low-resource languages).

**Usage:**

```bash
bash download-models-spacy-udpipe.sh
```

---

#### 3. Stanza Models

**Script:** `download-models-stanza.py`

```python
import os
import stanza

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
stanza_model_dir = os.path.join(BASE_DIR, "models", "stanza_models")

models = [
"gl", "grc", "be", "lzh", "cop", "fo", "got", "is", "la", "lv", "mt",
"pcm", "nn", "no", "sme", "cu", "fro", "orv", "sr", "hyw", "cy", "wo",
"gd", "sa", "qtd", "ug"
]

for model in models:
    stanza.download(model, model_dir=stanza_model_dir)
```

**Description:**  
Used for low-resource, historical, or specialty languages with Stanza.

**Usage:**

```bash
python3 download-models-stanza.py
```

---

## Running the Tool

### Command-line Usage

```bash
python3 multilangDepTreeVisualizer.py --lang <language_code> --text "<your_text>" [--merge_chunks 0|1] [--merge_punct 0|1] [--out <output_file.svg>]
```

### Parameters

| Parameter        | Description                                            | Default / Notes                 |
| ---------------- | ------------------------------------------------------ | ------------------------------- |
| `--lang`         | Language code (e.g., en, fr, de, th, zh, ar, vi, etc.) | **Required**                    |
| `--text`         | Input text to visualize (string only)                  | **Required**                    |
| `--merge_chunks` | Merge noun chunks (1 = yes, 0 = no)                    | `1`                             |
| `--merge_punct`  | Merge consecutive punctuation marks (1 = yes, 0 = no)  | `0`                             |
| `--out`          | Output SVG file path                                   | Prints SVG to stdout if omitted |

### Example 1: Direct text input

```bash
python3 multilangDepTreeVisualizer.py \
    --lang en \
    --text "She quickly ran to the store before it closed." \
    --merge_chunks 1 \
    --merge_punct 0 \
    --out output.svg
```

This will generate a dependency tree visualization and save it as `output.svg`.

### Example 2: Using default options (merge noun chunks, no punctuation merge, print to stdout)

```bash
python3 multilangDepTreeVisualizer.py --lang en --text "This is a test sentence."
```

Output will be printed to the console as SVG content.

---

## Use Cases

* **Dependency Tree Visualization:** Visualize token-level syntactic dependencies and POS tags for any supported language.
* **Corpus Analysis:** Examine sentence structure, tokenization, noun chunks, and entity relationships.
* **Text Preprocessing for NLP:** Produces tokenized, POS-tagged, and optionally merged noun chunk/entity-level text for downstream tasks.
* **Multilingual Support:** Modern, low-resource, and historical languages with spaCy, spaCy-UDPipe, spaCy-Stanza, and spaCy-Thai.

---

## Notes

* Ensure all models are installed before running.
* Large texts require sufficient memory; the tool splits input text into chunks.
* Noun chunk and entity merging is language-specific.
* SVG layout may vary if punctuation or phrases are merged.
* Adjust rendering parameters (`compact`, `bg`, `color`) for high-resolution output.

---

## Project Structure

```
📦 MultilangDepTreeVisualizer
 ┣ 📜 download-models-spacy.sh
 ┣ 📜 download-models-spacy-udpipe.sh
 ┣ 📜 download-models-stanza.py
 ┣ 📂 examples
 ┃   ┗ 📜 sample_output.svg
 ┣ 📜 LICENSE
 ┣ 📜 multilangDepTreeVisualizer.py
 ┗ 📜 README.md


```

---

## License

This project is released under the **MIT License**.

---

## Author

Developed by **Zar Zar Hlaing**

---

## References

1. [spaCy Documentation](https://spacy.io/usage)
2. [Stanza NLP](https://stanfordnlp.github.io/stanza/)
3. [spaCy-UDPipe](https://github.com/KoichiYasuoka/spacy-udpipe)
4. [DisplaCy Visualizer](https://spacy.io/usage/visualizers)
5. [Thai NLP with spaCy-Thai](https://github.com/PyThaiNLP/spacy-thai)
