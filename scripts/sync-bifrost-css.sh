#!/usr/bin/env bash
# Refresh the vendored Bifrost framework CSS + the bundled fonts.
set -euo pipefail

cd "$(dirname "$0")/.."

vendor="src/intility_bifrost_zensical/theme/assets/vendor"
version="$(node -p "require('./package.json').dependencies['@intility/bifrost-css']")"
echo "Syncing @intility/bifrost-css@${version}..."

tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT
curl -fsSL "https://unpkg.com/@intility/bifrost-css@${version}/dist/bifrost-all.css" -o "$tmp"

{
    echo "/* @intility/bifrost-css ${version} — vendored, do not edit. Run scripts/sync-bifrost-css.sh. */"
    sed '/@import url("https:\/\/fonts.googleapis.com/d; /@import url("https:\/\/api.fontshare.com/d' "$tmp"
} > "${vendor}/bifrost-all.css"

echo "Syncing Satoshi font..."
curl -fsSL "https://bifrost.intility.com/font/satoshi-intility-variable.woff2" \
    -o "${vendor}/fonts/satoshi-intility-variable.woff2"

# The OFL license is vendored alongside the woff2 as the license requires.
echo "Syncing JetBrains Mono font..."
curl -fsSL "https://cdn.jsdelivr.net/npm/@fontsource-variable/jetbrains-mono/files/jetbrains-mono-latin-wght-normal.woff2" \
    -o "${vendor}/fonts/jetbrains-mono-variable.woff2"
curl -fsSL "https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/OFL.txt" \
    -o "${vendor}/fonts/JetBrainsMono-OFL.txt"

echo "Done. Review the diff and commit."
