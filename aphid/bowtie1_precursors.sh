#! /bin/bash

for file in *_T_index.1.ebwt; do 
    echo
    echo ${file%.1.ebwt}
    parallel --link --eta --tmpdir ~/tmp \
    "bowtie -v 1 -f -S --seedlen 10 -p 4 -a \
    /nethome/mct30/bmds/index/plant_precursors/precursors/${file%.1.ebwt} \
    /nethome/mct30/bmds/reads/{2}_trimmed_17-35.fa \
    /nethome/mct30/bmds/SAM_out/precursors{1}_${file%_index.1.ebwt}_bowtie1_a_v1_T.map" \
    ::: G006_Gut G002_Gut BTIRed_Gut \
    ::: G006_Gut_F G002_Gut BTIRed_Gut
done
