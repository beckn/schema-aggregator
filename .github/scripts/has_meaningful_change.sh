#!/usr/bin/env bash
# Prints "true" or "false": whether the currently staged changes include
# anything besides a .sync/manifest-*.json "last_synced" timestamp bump.
# sync_sources.py rewrites that timestamp on every run regardless of
# whether the actual upstream content changed, so a staged diff limited to
# those lines shouldn't be treated as a real content change downstream.
set -euo pipefail

meaningful=false
while IFS= read -r file; do
  case "$file" in
    .sync/manifest-*.json)
      if git diff --cached -- "$file" \
          | grep -E '^[+-]' | grep -v '^+++ \|^--- ' | grep -qvE '^[+-]\s*"last_synced":'; then
        meaningful=true
      fi
      ;;
    *)
      meaningful=true
      ;;
  esac
done < <(git diff --cached --name-only)

echo "$meaningful"
