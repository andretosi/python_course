#!/usr/bin/env bash
set -euo pipefail

mkdir -p lezione1_lab/appunti
cd lezione1_lab/appunti

touch note.txt
printf 'gatto\nlimone\n' > note.txt
cp note.txt note_backup.txt
mv note.txt note_importanti.txt
rm note_backup.txt

ls
cat note_importanti.txt
