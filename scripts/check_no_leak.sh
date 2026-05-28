#!/usr/bin/env bash
# Pre-commit guard: refuse commits that leak project-specific identifiers
# into the public xrayctl repository. Update FORBIDDEN as new projects adopt
# xrayctl and want extra protection — only generic identifiers belong here.
set -euo pipefail

FORBIDDEN_RE='(ninjiu|h3cloud|h3llo-cloud|dublin|panel\.ninjiu|veeskelaam@|REMNAWAVE_ADMIN_PASSWORD=)'

# Files staged or passed as args.
files=("$@")
if [ "${#files[@]}" -eq 0 ]; then
  mapfile -t files < <(git diff --cached --name-only --diff-filter=ACMR)
fi

violations=0
self_path="${BASH_SOURCE[0]}"
self_real=$(cd "$(dirname "$self_path")" && pwd)/$(basename "$self_path")

for f in "${files[@]}"; do
  [ -f "$f" ] || continue
  # Skip the guard script itself — its regex would always match.
  f_real=$(cd "$(dirname "$f")" 2>/dev/null && pwd)/$(basename "$f")
  if [ "$f_real" = "$self_real" ]; then
    continue
  fi
  if grep -nIE "$FORBIDDEN_RE" "$f" >/dev/null 2>&1; then
    echo "leak: $f"
    grep -nIE "$FORBIDDEN_RE" "$f" | head -5
    violations=$((violations + 1))
  fi
done

if [ "$violations" -gt 0 ]; then
  echo
  echo "Refusing commit: $violations file(s) contain project-specific data."
  echo "If a match is a false positive, update FORBIDDEN_RE in $0."
  exit 1
fi
