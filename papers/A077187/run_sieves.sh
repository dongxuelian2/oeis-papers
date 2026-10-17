#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
c++ -O3 -std=c++17 one_shot_gmp_b8.cpp -lgmpxx -lgmp -o one_shot_gmp_b8
./one_shot_gmp_b8 1 183 >gmp_1_183.tsv &
./one_shot_gmp_b8 184 366 >gmp_184_366.tsv &
./one_shot_gmp_b8 367 549 >gmp_367_549.tsv &
./one_shot_gmp_b8 550 728 >gmp_550_728.tsv &
wait
cat gmp_1_183.tsv gmp_184_366.tsv gmp_367_549.tsv gmp_550_728.tsv | sort -n -k1,1 >all_486_gmp.tsv
test "$(wc -l <all_486_gmp.tsv)" -eq 486
awk '$4!=1 {print}' all_486_gmp.tsv
