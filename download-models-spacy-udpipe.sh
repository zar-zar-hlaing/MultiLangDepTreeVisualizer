#!/bin/bash

models=(
	"af"
	"ar"
	"hy"
	"eu"
	"zh"
	"he"
	"hi"
	"hu"
	"id"
	"ga"
	"lv"
	"mr"
	"fa"
	"sk"
	"sl"
	"ta"
	"te"
	"tr"
	"ur"
	"vi"
)

for model in "${models[@]}"
do
   python3 -c "import spacy_udpipe; spacy_udpipe.download('$model')"
done
