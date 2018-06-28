#! /bin/bash

while read -r a b c d e f g h i j k l m n o p q; do
    echo -n '>'
    echo $a
    echo $p
done < result_2.csv > result_2.fa

# while read -r a b c d e f g h; do
#      echo -n '>'
#      echo $d
#      echo $g
# done < G006_Gut_plant_filter_P_prediction > G006_Gut_plant_filter_P_prediction.fa
