#! /bin/bash

#BSUB -J "ACYPI8971_membrane_abinitio_parallel[46-78]"
#BSUB -e /nethome/mct30/err/ACYPI8971_membrane_abinitio_parallel_%I.err
#BSUB -o /nethome/mct30/out/ACYPI8971_membrane_abinitio_parallel_%I.out
#BSUB -n 1
#BSUB -q general
#BSUB -R "rusage[mem=1500]"
#BSUB -W 165:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu

# Job title, error output, standard output, number of cores,
# queue, cores per node, RAM per core in MB, run time limit, 
# send email when jobs begins, send email with stats when job finished, 
# email

# $LSB_JOBINDEX goes from 1 to 32 for each job

mkdir /nethome/mct30/aphid/mem-ab-out.$LSB_JOBINDEX

/nethome/mct30/rosetta/rosetta_bin_linux_2017.08.59291_bundle/\
main/source/bin/membrane_abinitio2.static.linuxgccrelease \
-abinitio:membrane \
-in:file:fasta /nethome/mct30/aphid/acypi8971_prot.fa \
-in:file:frag3 /nethome/mct30/aphid/robetta/aat000_03_05.200_v1_3 \
-in:file:frag9 /nethome/mct30/aphid/robetta/aat000_09_05.200_v1_3 \
-in:file:spanfile /nethome/mct30/aphid/acypi8971_octopus.span \
-in:file:lipofile /nethome/mct30/aphid/acypi8971.lips4 \
-in:path:database \
/nethome/mct30/rosetta/rosetta_bin_linux_2017.08.59291_bundle/main/database \
-score:find_neighbors_3dgrid \
-membrane:no_interpolate_Mpair \
-membrane:Menv_penalties \
-membrane:normal_cycles 40 \
-membrane:normal_mag 15 \
-membrane:center_mag 2 \
-out:membrane_pdb true \
-out:pdb \
-out:path /nethome/mct30/aphid/mem-ab-out.$LSB_JOBINDEX/ \
-out:file:silent \
/nethome/mct30/aphid/mem-ab-out.$LSB_JOBINDEX/ACYPI008971_silent.$LSB_JOBINDEX.out \
-out:file:scorefile \
/nethome/mct30/aphid/mem-ab-out.$LSB_JOBINDEX/ACYPI008971_score.$LSB_JOBINDEX.sc \
-out:nstruct 315
# Membrane ab initio application,
# Protein sequence in fasta format, Octopus transmembrane prediction, 
# Lipophilicity prediction, 3-residue fragments, 9-residue fragments, 
# Path to rosetta database, 
# Use a 3D lookup table for residue neighbors calculations, 
# Switch off the interpolation between the two layers for the Mpair term, 
# Switch on the following penalties:
#     * no non-helical secondary structure fragments in predicted 
#       transmembrane helical regions in the hydrophobic layer of the membrane.
#     * no N- and C- termini residues of predicted transmembrane helical 
#       regions in the hydrophobic layer of the membrane.
#     * no transmembrane helices with orientation >45 degrees relative to the 
#       membrane normal vector.
# Speed settings for Monte Carlo based membrane normal and center search
# Include a 30 nm membrane in the output
# Output file
# Number of times to process each input PDB
# Total number of decoys to produce
# Number of output structures (32 cores * 315 iterations = 10,080 structures)
# Silent output file