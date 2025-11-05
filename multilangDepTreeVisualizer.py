#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multilingual Syntax Tree Visualizer
-----------------------------------
Generates dependency tree visualizations (SVG) for 80+ languages using:
- spaCy
- spaCy-UDPipe
- spaCy-Stanza
- spaCy-Thai

Usage Example:
    python3 multilangDepTreeVisualizer.py \
        --lang en \
        --text "This is a test sentence." \
        --merge_chunks 1 \
        --merge_punct 0 \
        --out output.svg
"""

#region Imports
import os
import sys
import spacy
import spacy_thai
import spacy_udpipe
import spacy_stanza
from spacy import displacy
import argparse
#endregion

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
stanza_model_dir = os.path.join(BASE_DIR, "models", "stanza_models")

#region Language Initialization
def load_language_model(language: str, stanza_model_dir: str = stanza_model_dir):
    """
    Load the appropriate NLP pipeline for a given language code.
    """
    language = language.lower()

    try:
        if language == "th":
            return spacy_thai.load()
        elif language in [
            "fr", "de", "es", "it", "pt", "ru", "ja", "zh", "ko",
            "nl", "sv", "da", "fi", "pl", "ro", "el", "hr", "lt",
            "nb", "uk", "ca"
        ]:
            return spacy.load(f"{language}_core_news_sm")
        elif language in ["en"]:
            return spacy.load("en_core_web_sm")
        elif language in ["zh-hans", "zh-cn"]:
            return spacy.load("zh_core_web_sm")
        elif language in ["pt-br", "pt-pt"]:
            return spacy.load("pt_core_news_sm")
        elif language in ["id", "ms"]:
            return spacy_udpipe.load("id")
        elif language in [
            "af", "ar", "bg", "cs", "et", "he", "hi", "hu", "mr", "fa",
            "sk", "sl", "ta", "te", "tr", "ur", "vi"
        ]:
            return spacy_udpipe.load(language)
        else:
            return spacy_stanza.load_pipeline("xx", lang=language, model_dir=stanza_model_dir, download_method=None)
    except Exception as e:
        print(f"Could not load model for '{language}': {e}", file=sys.stderr)
        sys.exit(1)
#endregion


#region Phrase and Punctuation Merging
def merge_phrases(doc, language):
    """Merge noun chunks for supported languages."""
    try:
        with doc.retokenize() as retokenizer:
            for np in doc.noun_chunks:
                attrs = {
                    "tag": np.root.tag_,
                    "lemma": np.root.lemma_,
                    "ent_type": np.root.ent_type_
                }
                retokenizer.merge(np, attrs=attrs)
    except Exception:
        pass
    return doc


def merge_punct(doc):
    """Merge consecutive punctuation marks."""
    try:
        spans = []
        for word in doc[:-1]:
            if not (word.is_punct and doc[word.i + 1].is_punct):
                continue
            start = word.i
            end = start + 1
            while end < len(doc) and doc[end].is_punct:
                end += 1
            span = doc[start:end]
            spans.append((span, word.tag_, word.lemma_, word.ent_type_))
        with doc.retokenize() as retokenizer:
            for span, tag, lemma, ent_type in spans:
                retokenizer.merge(span, attrs={"tag": tag, "lemma": lemma, "ent_type": ent_type})
    except Exception:
        pass
    return doc
#endregion


#region Visualization
UPOS_COLORS = {
    "ADJ": "#FF5733", "ADP": "#33C1FF", "ADV": "#FF33A8", "AUX": "#8D33FF",
    "CCONJ": "#33FFBD", "DET": "#FFC733", "INTJ": "#FF8333", "NOUN": "#FF5733",
    "NUM": "#33FFF0", "PART": "#A833FF", "PRON": "#FF33E1", "PROPN": "#FF3333",
    "PUNCT": "#B0B0B0", "SCONJ": "#33FF6E", "SYM": "#9D33FF", "VERB": "#33FF57",
    "X": "#808080"
}


def render_dependency_svg(doc, merge_punct_state, merge_chunks_state):
    """Render dependency visualization as SVG with POS color styling."""
    options = {
        "bg": "#000000",
        "color": "white",
        "offset_x": 100,
        "collapse_punct": merge_punct_state,
        "collapse_phrases": merge_chunks_state,
    }

    svg = displacy.render(doc, style="dep", options=options, jupyter=False)
    for pos, color in UPOS_COLORS.items():
        svg = svg.replace(f'>{pos}<', f' style="fill:{color}">{pos}<')
    return svg


def render_dependency_svg_from_text(text, lang, merge_punct_state=0, merge_chunks_state=1):
    """
    Convenience wrapper to render a dependency SVG directly from text input.
    This allows calling from another script.
    """
    nlp = load_language_model(lang)
    nlp.max_length = 2_000_000

    doc = nlp(text.strip())
    if merge_chunks_state:
        doc = merge_phrases(doc, lang)
    if merge_punct_state:
        doc = merge_punct(doc)

    return render_dependency_svg(doc, merge_punct_state, merge_chunks_state)
#endregion


#region Main
def main():
    parser = argparse.ArgumentParser(
        description="Generate multilingual dependency tree visualizations (SVG) using spaCy, spaCy-UDPipe, spaCy-Stanza, or spaCy-Thai."
    )
    parser.add_argument("--lang", required=True, help="Language code (e.g., en, fr, de, th, zh, ar, vi, etc.)")
    parser.add_argument("--text", required=True, help="Input text to visualize (string only).")
    parser.add_argument("--merge_chunks", type=int, choices=[0, 1], default=1, help="Merge noun chunks (1=yes, 0=no)")
    parser.add_argument("--merge_punct", type=int, choices=[0, 1], default=0, help="Merge punctuation (1=yes, 0=no)")
    parser.add_argument("--out", help="Output SVG file path (default: print to stdout).")

    args = parser.parse_args()

    output_svg = render_dependency_svg_from_text(
        args.text,
        args.lang,
        merge_punct_state=args.merge_punct,
        merge_chunks_state=args.merge_chunks
    )

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output_svg)
        print(f"Saved syntax tree visualization to: {args.out}")
    else:
        print(output_svg)
#endregion


#region Entry Point
if __name__ == "__main__":
    main()
#endregion

