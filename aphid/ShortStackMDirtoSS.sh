echo ''
echo ''
echo 'Must be in ShortStack_predictions/MIRNAs'
echo ''
echo ''

for file in ./C*; do 
    echo -n '>'; 
    cat $file | head -n 6; 
done > ShortStack_6_20-24_f_300_SRA_q28_17-25_SRR799356-58.ss

python /nethome/mct30/gitclones/bmds/aphid/ShortStackMDirtoSS.py \
ShortStack_6_20-24_f_300_SRA_q28_17-25_SRR799356-58.ss