#! /bin/bash

while read -r a b c d e f g h; do
    echo -n '>'
    echo $c
    echo $g
done < G006_Gut_plant_filter_P_prediction
