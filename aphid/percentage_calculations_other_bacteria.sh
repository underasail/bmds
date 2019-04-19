#! /bin/bash

#BSUB -J per_calc_ob
#BSUB -e /nethome/mct30/err/per_calc_ob.err
#BSUB -o /nethome/mct30/out/per_calc_ob.out
#BSUB -n 6
#BSUB -P acypi
#BSUB -q bigmem
#BSUB -W 24:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

script_dir=/nethome/mct30/gitclones/bmds/aphid
SAM_dir=/nethome/mct30/bmds/SAM_out
output_dir=/nethome/mct30/bmds/SAM_out/other_bacteria

parallel --link --eta \
"python $script_dir/percentage_calculations_other_bacteria.py \
$SAM_dir/{1}_Myzus-only.map \
$SAM_dir/{1}_Buchnera-only.map \
$SAM_dir/{1}_plants-only.map \
$SAM_dir/{1}_other-bacteria_full-alignment.map \
$output_dir/{1}_other_bacteria_percentages.txt" \
::: G006_Gut G002_Gut BTIRed_Gut \
G006_Bac G002_Bac BTIRed_Bac