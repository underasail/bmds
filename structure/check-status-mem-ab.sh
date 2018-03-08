#! /bin/bash

echo '##############################################'
echo '# STATUS OF ACYPI008971 STRUCTURE PREDICTION #'
echo '##############################################'
echo '# Number of structures produced:             #'
echo -n '# '
ls -lh ~/aphid/mem-ab-out.*/*.pdb | wc -l 
echo '# Number of cores running:                   #'
echo -n '# '
bjobs | grep 'RUN' | wc -l
max=0
for filename in ~/aphid/mem-ab-out.*; do 
    # echo $filename; 
    number=$(ls $filename | tail -n 1); 
    number=${number:7:3}; 
    # echo $number;
    if [ $number -gt $max ]; then
	max=$number;
	# echo $max
    fi
done
echo '# Script with max output has created:        #'
echo -n '# '
echo -n $max
echo ' structures'
echo '##############################################'