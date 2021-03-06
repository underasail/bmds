#! /bin/bash

#BSUB -J per_calc_ob_v
#BSUB -e /nethome/mct30/err/per_calc_ob_v.err
#BSUB -o /nethome/mct30/out/per_calc_ob_v.out
#BSUB -n 2
#BSUB -P acypi
#BSUB -q bigmem
#BSUB -W 24:00
#BSUB -R span[ptile=16]
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
output_dir_ob=/nethome/mct30/bmds/SAM_out/other_bacteria
output_dir_vr=/nethome/mct30/bmds/SAM_out/viruses2

mkdir -p $output_dir_ob $output_dir_vr

parallel --link --eta \
"python $script_dir/percentage_calculations_other_bacteria.py \
$SAM_dir/{1}_Myzus-only.map \
$SAM_dir/{1}_Buchnera-only.map \
$SAM_dir/{1}_plants-only.map \
$SAM_dir/{1}_other_bacteria_HF_2018_corrected.map \
$output_dir_ob/{1}_other_bacteria_percentages_HF_2018_corrected.txt" \
::: G006_Gut G002_Gut BTIRed_Gut \
G006_Bac G002_Bac BTIRed_Bac


parallel --link --eta \
"python $script_dir/percentage_calculations_other_bacteria.py \
$SAM_dir/{1}_Myzus-only.map \
$SAM_dir/{1}_Buchnera-only.map \
$SAM_dir/{1}_plants-only.map \
$SAM_dir/{1}_viruses2_corrected.map \
$output_dir_vr/{1}_viruses2_w1mm_all-data-included_corrected.txt" \
::: G006_Gut G002_Gut BTIRed_Gut \
G006_Bac G002_Bac BTIRed_Bac