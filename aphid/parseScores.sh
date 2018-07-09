#! /bin/bash

grep "^>scaffold_" result_1_miranda_targets_0.out | sort | uniq -c > result_1_miranda_targets_0_scores.out

cat result_1_miranda_targets_0_scores.out | cut -f3 > result_1_miranda_targets_0_scores2.out