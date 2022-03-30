#!/usr/bin/env bash
obtained_version="$(git branch --show-current | cut --delimiter='v' --fields=2)"
expected_version="$(grep version setup.py | cut -d '"' -f 2)"
if [ "${obtained_version}" = "${expected_version}" ]; then
  echo "."
  exit 0
else
  echo "Versión en la rama: v{obtained_version}"
  echo "Versión en 'setup.py': v{expected_version}"
  echo "FAIL: Las versiones no coinciden"
  exit 1
fi
