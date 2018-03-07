#! /bin/bash

echo '##############################################'
echo '# STATUS OF ACYPI008971 STRUCTURE PREDICTION #'
echo '##############################################'
echo 'Number of structures produced:               #'
ls -lh ~/aphid/mem-ab-out.*/*.pdb | wc -l 
echo 'Number of cores running:                     #'
bjobs | grep 'RUN' | wc -l
max=0
for filename in ~/aphid/mem-ab-out.*; do 
    # echo $filename; 
    number=$(ls $filename | tail -n 1); 
    number=${number:7:3}; 
    # echo $number;
    if expr $number > $max;
    then
	max=$number;
    fi
done
echo 'Script with max output has created:          #'
echo -n $max
echo ' structures'
echo '##############################################'