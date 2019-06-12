#! /bin/bash

parallel --link --eta \
"~/gitclones/bmds/aphid/elimUnmatched_plant-only.py \
~/bmds/SAM_out/{1}_Myzus-only.map \
~/bmds/SAM_out/{1}_Buchnera-only.map \
~/bmds/SAM_out/{1}_plants-only.map \
~/bmds/reads/{2}_trimmed_17-35.fa \
~/bmds/reads/{1}_plants-only_corrected.fasta" \
::: G006_Gut G002_Gut BTIRed_Gut \
G006_Bac G002_Bac BTIRed_Bac \
::: G006_Gut_F G002_Gut BTIRed_Gut \
G006_Bac_F G002_Bac BTIRed_Bac
