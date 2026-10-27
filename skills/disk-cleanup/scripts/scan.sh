#!/usr/bin/env bash
# Read-only disk usage survey for the disk-cleanup skill. Deletes nothing.
set -u

GIT_ROOT="${1:-$HOME/git}"
TOP="${TOP:-12}"

section() { printf '\n=== %s ===\n' "$1"; }
sizes() { du -sh "$@" 2>/dev/null | sort -rh | head -"$TOP"; }

section "Free space"
df -h /System/Volumes/Data 2>/dev/null | tail -1

section "Home (top-level)"
sizes "$HOME"/* "$HOME"/.[!.]*

section "~/.cache"
sizes "$HOME"/.cache/*

section "~/Library/Caches"
sizes "$HOME"/Library/Caches/*

section "~/Library/Application Support"
sizes "$HOME"/Library/Application\ Support/*

section "Known big items"
sizes "$HOME/Library/Application Support/Claude/vm_bundles" \
  "$HOME/Library/Application Support/Google/Chrome/OptGuideOnDeviceModel" \
  "$HOME/Library/Application Support/Google/GoogleUpdater/crx_cache" \
  "$HOME/Library/Logs/JetBrains" "$HOME/.npm" "$HOME/.m2" "$HOME/Library/pnpm" \
  "$HOME/.colima" "$HOME/.sdkman/tmp" "$HOME/Library/Java/JavaVirtualMachines"/*

section "Claude Code versions (running: $(readlink "$(command -v claude)" 2>/dev/null | xargs basename 2>/dev/null))"
ls -1 "$HOME/.local/share/claude/versions" 2>/dev/null

section "Repo build/dependency dirs under $GIT_ROOT"
find "$GIT_ROOT" -maxdepth 4 -type d \( -name node_modules -o -name .venv -o -name venv -o -name .next \
  -o -name target -o -name dist -o -name build -o -name .mypy_cache -o -name .pytest_cache \
  -o -name .ruff_cache -o -name .gradle -o -name .turbo \) -prune -print0 2>/dev/null \
  | xargs -0 du -sh 2>/dev/null | sort -rh | head -40

section "Running dev servers (skip their build dirs)"
pgrep -fl "next dev|next start|mvn|gradle|uvicorn|gunicorn|vite|mypy" || echo "none"

section "Docker"
if command -v docker >/dev/null && docker info >/dev/null 2>&1; then
  docker system df
  docker images --format '{{.Repository}}:{{.Tag}}  {{.Size}}  {{.CreatedSince}}'
  echo "-- running:"; docker ps --format '{{.Image}}  {{.Names}}'
else
  echo "docker not running"
fi

section "Large files (>50M) outside Library/personal folders"
find "$HOME" -xdev \( -path "$HOME/Library" -o -path "$HOME/Downloads" -o -path "$HOME/Documents" \
  -o -path "$HOME/.Trash" -o -path "$HOME/Pictures" -o -path "$HOME/Movies" -o -path "$HOME/Music" \
  -o -path "$HOME/.colima" -o -name node_modules -o -name .venv -o -name .git \) -prune \
  -o -type f -size +50M -print0 2>/dev/null | xargs -0 du -h 2>/dev/null | sort -rh | head -25

section "Personal folders (TCC may block; needs Full Disk Access)"
for d in Downloads Documents Desktop .Trash; do
  du -sh "$HOME/$d" 2>&1 | sed 's/^du: //'
done
