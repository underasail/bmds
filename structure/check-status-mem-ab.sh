#! /bin/bash

echo '##############################################'
echo '# STATUS OF ACYPI008971 STRUCTURE PREDICTION #'
echo '##############################################'
echo '# Number of structures produced:             #'
echo -n '# '
ls -lh /scratch/projects/acypi/aphid/mem-ab-out-parent/mem-ab-out.*/*.pdb | wc -l 
echo '# Number of cores running:                   #'
echo -n '# '
bjobs | grep 'allel' | wc -l
#max='0'
#for filename in ~/aphid/mem-ab-out.*; do 
#    # echo $filename; 
#    number=$(ls $filename | tail -n 1); 
#    number=${number:7:3}; 
#    # echo $number;
#    if [ ${number:0:2} == 00 ]; then
#	number=${number:2:1};
#    elif [ ${number:0:1} == 0 ]; then
#	number=${number:1:2}
#    fi
#    # echo $number 
#    if [ $number -gt $max ]; then
#	max=$number;
#	maxfile=$filename;
#    fi
#done
#echo '# Script with max output has created:        #'
#echo -n '# '
#echo -n $max
#echo ' structures'
#echo $maxfile
echo '##############################################'