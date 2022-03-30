#!/usr/bin/env bash
obtained_version="$(git branch --show-current | cut -d 'v' -f 2)"
expected_version="$(grep version setup.py | cut -d '"' -f 2)"
if [ "${obtained_version}" = "${expected_version}" ]; then
  echo "."
  exit 0
else
  echo "F"
  echo "FAIL: Las versiones no coinciden"
  exit 1
fi
