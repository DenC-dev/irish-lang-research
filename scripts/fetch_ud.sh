#!/usr/bin/env bash
# Download the two public Irish UD treebanks into external/ (git-ignored).
# IDT: CC BY-SA 3.0. TwittIrish: CC BY-SA 4.0. They are not redistributed here.
set -euo pipefail
mkdir -p external && cd external
for tb in UD_Irish-IDT UD_Irish-TwittIrish; do
  [ -d "$tb" ] || git clone --depth 1 "https://github.com/UniversalDependencies/$tb.git"
  git -C "$tb" rev-parse HEAD
done
