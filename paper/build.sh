#!/usr/bin/env bash
# Build the working paper PDF. Needs pandoc and xelatex with DejaVu fonts.
set -euo pipefail
cd "$(dirname "$0")"
pandoc sineadh.md -o sineadh.pdf --pdf-engine=xelatex -V monofont="DejaVu Sans Mono"
