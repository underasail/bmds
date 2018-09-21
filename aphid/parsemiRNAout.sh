#! /bin/bash

# while read -r a b c d e f g h i j k l m n o p q; do
#     echo -n '>'
#     echo $a
#     echo $p
# done < $1 > animal_miRNAs.fa

while read -r a b c d e f g h; do
     echo -n '>'
     echo $d
     echo $h
done < G006_Gut_plant_filter_P_prediction > G006_Gut_plant_filter_P_prediction_precursors.fa
