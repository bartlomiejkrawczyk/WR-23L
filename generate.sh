#!/bin/bash

set -euo pipefail

INPUT="README.md"
CONFIG="wr-metadata.yaml"
OUTPUT="output.pdf"

help () {
    cat << EOF
Usage: generate.sh [OPTION]...
    -h --help        Display this message
    -p --packages    Install necessary packages first
    -s --submodules  Fetch all necessary submodules for pdf generation
    -i --input       Specify input markdown file
    -c --config      Specify input configuration file
    -o --output      Specify output pdf file
EOF
exit 0;
}

install () {
    sudo apt install texlive-full pandoc pandoc-citeproc -y
}

fetch_submodule () {
    git submodule update --init --recursive
}

while [[ $# -gt 0 ]]; do
  case $1 in
    -h|--help)
        help
        ;;
    -s|--submodule)
        fetch_submodule
        shift
        ;;
    -p|--packages)
        install
        shift
        ;;
    -i|--input)
        INPUT="$2"
        shift
        shift
        ;;
    -c|--config)
        CONFIG="$2"
        shift
        shift
        ;;
    -o|--output)
        OUTPUT="$2"
        shift
        shift
        ;;
  esac
done

mkdir -p output/

cd wut-thesis-pandoc

pandoc ../$INPUT \
    --verbose \
    --standalone \
    --syntax-definition include/python.xml \
    --biblatex -o ../output/$OUTPUT \
    --listings \
    --highlight=tango \
    --metadata-file=../$CONFIG \
    --pdf-engine=latexmk \
    --from markdown \
    --template include/wut-template.tex

cd ..